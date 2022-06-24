import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.nn.init as init

class ResNetLayer(nn.Module):
    def __init__(self, in_feature_maps, out_feature_maps, downsample = True):
        super(ResNetLayer, self).__init__()

        self.stride = 2 if downsample == True else 1
        self.conv0 = nn.Conv2d(in_feature_maps, out_feature_maps, 3, stride = self.stride, padding = 1)
        self.bn0 = nn.BatchNorm2d(out_feature_maps)
        self.conv1 = nn.Conv2d(out_feature_maps, out_feature_maps, 3, stride = 1, padding = 1)
        self.bn1 = nn.BatchNorm2d(out_feature_maps)

        self.skipconn_cnn = nn.Conv2d(in_feature_maps, out_feature_maps, kernel_size=1, stride=self.stride, padding = 0)
        self.skipconn_bn = nn.BatchNorm2d(out_feature_maps)

    def forward(self, input):
        ######################## task 2.1 ##########################
        x = F.relu(self.bn0(self.conv0(input)))
        x = self.bn1(self.conv1(x))
        r = self.skipconn_bn(self.skipconn_cnn(input))
        x = x+r
        x = F.relu(x)
        return x

        #pass
        ########################    END   ##########################


class ResNet(nn.Module):
    def __init__(self):
        super(ResNet, self).__init__()
        
        self.conv0 = nn.Conv2d(3, 64, 3, stride = 1, padding = 1) #(64*64*3) -> (64*64*64)
        self.bn0 = nn.BatchNorm2d(64)
        
        ######################## task 2.2 ##########################
        self.conv1 = nn.Sequential(nn.MaxPool2d(kernel_size=3,stride=2,padding=1),
                                   ResNetLayer(64,64,False),
                                   ResNetLayer(64,64,False),
                                   ResNetLayer(64,64,False))
        self.conv2 = nn.Sequential(ResNetLayer(64,128,True),
                                   ResNetLayer(128,128,False),
                                   ResNetLayer(128,128,False),
                                   ResNetLayer(128,128,False))
        self.conv3 = nn.Sequential(ResNetLayer(128,256,True),
                                   ResNetLayer(256,256,False),
                                   ResNetLayer(256,256,False),
                                   ResNetLayer(256,256,False))
        self.conv4 = nn.Sequential(ResNetLayer(256,512,True),
                                   ResNetLayer(512,512,False),
                                   ResNetLayer(512,512,False))
        self.avg_pool = nn.AdaptiveAvgPool2d(1)
        self.fc = nn.Linear(512, 200)



        ########################    END   ##########################

        self.dropout = nn.Dropout(0.15)

    def forward(self, input):
        x = F.relu(self.bn0(self.dropout(self.conv0(input))))
        
        ######################## task 2.3 ##########################
        x = self.conv1(x)
        # print(x.size())
        x = self.conv2(x)
        # print(x.size())
        x = self.conv3(x)
        # print(x.size())
        x = self.conv4(x)
        # print(x.size())
        out = self.avg_pool(x)
        out = self.dropout(out)
        out = out.view((x.shape[0],-1))

        out = self.fc(out)
        ########################    END   ##########################

        return out
    
cnn = ResNet()
x = torch.randn([64, 3, 64, 64])
x = cnn(x)
print(x.size())