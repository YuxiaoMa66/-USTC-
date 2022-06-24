import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.nn.init as init

class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        
        self.conv0 = nn.Conv2d(3, 32, 3, stride = 1, padding = 1) #(64*64*3) -> (64*64*32)
        self.bn0 = nn.BatchNorm2d(32)
        
        # ####################### task 1.1 ##########################
        # self.relu0 = nn.ReLU()
        # self.mp = nn.MaxPool2d(2) # 池化之后的size变成(32*32*32)
        #  O = （I - K + 2P）/ S +1
        
        # self.conv1 = nn.Sequential(nn.Conv2d(32, 64, 5, stride = 1, padding = 0),
        #                            nn.Dropout(0.5),
        #                            nn.BatchNorm2d(64),                         
        #                            nn.ReLU(),
        #                            nn.MaxPool2d(2)) # -> (14*14*64)
        # self.conv2 = nn.Sequential(nn.Conv2d(64, 512, 3, stride = 1, padding = 1), 
        #                            nn.Dropout(0.5),
        #                            nn.BatchNorm2d(512),
        #                            nn.ReLU(),
        #                            nn.MaxPool2d(2)) #  -> (7*7*512)
        # self.conv3 = nn.Sequential(nn.Conv2d(512, 512, 2, stride = 1, padding = 0), 
        #                            nn.Dropout(0.5), 
        #                            nn.BatchNorm2d(512),
        #                            nn.ReLU(),
        #                            nn.MaxPool2d(2)) #  (3*3*512)
        # self.dense = nn.Sequential(nn.Linear(3*3*512, 3*3*512),
        #                            nn.ReLU(),
        #                            nn.Dropout(0.5),
        #                            nn.Linear(3*3*512,200))  
        # 发现这样准确率太低了0.37emm
        
        self.bn0 = nn.BatchNorm2d(32)
        
        ######################## task 1.1 ##########################
        self.conv1 = nn.Conv2d(32, 64, 2, stride = 1, padding=1)
        self.bn1 = nn.BatchNorm2d(64)

        self.conv2 = nn.Conv2d(64, 192, 2, stride=1, padding=1)
        self.bn2 = nn.BatchNorm2d(192)

        self.conv3 = nn.Conv2d(192, 256, 2, stride=1, padding=1)
        self.bn3 = nn.BatchNorm2d(256)
        
        self.conv4 = nn.Conv2d(256, 256, 3, stride=1, padding=1)
        self.bn4 = nn.BatchNorm2d(256)

        # 池化层
        self.maxpool = nn.MaxPool2d(3, 2)

        # 全连接层
        # self.fc1 = nn.Linear(192*3*3, 192*3*3)
        self.fc2 = nn.Linear(256*3*3, 200)

                              
                                    
                                    

        ########################    END   ##########################
        self.dropout = nn.Dropout(0.15)
                
    def forward(self, input):
        x = F.relu(self.bn0(self.dropout(self.conv0(input))))
        
        ######################## task 1.2 ##########################
        x = self.maxpool(x)
        # # print(x.size())
        # x = self.conv1(x)
        # # print(x.size())
        # x = self.conv2(x)
        # # print(x.size())
        # x = self.conv3(x)
        # # print(x.size())
        # x = x.view(-1, 3*3*512)
        # x = self.dense(x)
        
        x = F.relu(self.bn1(self.dropout(self.conv1(x))))
        x = self.maxpool(x)
        # print(x.size())

        x = F.relu(self.bn2(self.dropout(self.conv2(x))))
        x = self.maxpool(x)
        # print(x.size())

        x = F.relu(self.bn3(self.dropout(self.conv3(x))))
        x = self.maxpool(x)
        # print(x.size())
        
        x = F.relu(self.bn4(self.dropout(self.conv4(x))))
        
        # print(x.size())
        
        # x = F.relu(self.dropout(self.fc1(x.view(-1, 192*3*3))))
        x = self.fc2(x.view(-1, 256*3*3))


        
        # Tips x = x.view(-1, 3*3*512)
        ########################    END   ##########################

        return x
    
# c = CNN()
# x = torch.randn([64,3,64,64])
# x = c(x)
# print(x.size())