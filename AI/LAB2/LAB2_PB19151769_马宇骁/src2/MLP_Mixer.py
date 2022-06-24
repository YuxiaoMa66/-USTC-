import torch
import torch.nn as nn
from torchvision import transforms
from torchvision.datasets import MNIST
#禁止import除了torch以外的其他包，依赖这几个包已经可以完成实验了

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

class Mixer_Layer(nn.Module):
    def __init__(self, patch_size, hidden_dim):
        super(Mixer_Layer, self).__init__()
        ########################################################################
        #这里需要写Mixer_Layer（layernorm，mlp1，mlp2，skip_connection）
        self.token_dim = (28 // patch_size) ** 2
        self.channel_dim = 14
        n = hidden_dim
        self.mlp1 = nn.Sequential(
            nn.Linear(self.token_dim, n),
            nn.GELU(),
            GELUnn.Dropout(0),  # 防止或减轻过拟合
            nn.Linear(n,self.token_dim),
            nn.Dropout(0)
        )
        self.mpl2 = nn.Sequential(
            nn.Linear(self.channel_dim, n),
            nn.GELU(),
            GELUnn.Dropout(0),  # 防止或减轻过拟合
            nn.Linear(n,self.channel_dim),
            nn.Dropout(0)
        )
        self.layernorm = nn.LayerNorm(self.channel_dim)
        ########################################################################

    def forward(self, x):
        ########################################################################
        x = self.layernorm(x).transpose(1,2)
        xt = self.mlp1(x)
        xskip = self.layernorm((x + xt).transpose(1,2))
        xc = self.mpl2(xskip)
        xm = xskip + xc
        return  xm
        ########################################################################


class MLPMixer(nn.Module):
    def __init__(self, patch_size, hidden_dim, depth):
        super(MLPMixer, self).__init__()
        assert 28 % patch_size == 0, 'image_size must be divisible by patch_size'
        assert depth > 1, 'depth must be larger than 1'
        ########################################################################
        #这里写Pre-patch Fully-connected, Global average pooling, fully connected
        self.image_channel = 1  # MNIST数据集图片维度
        self.channel_dim = 14  # 通道数(嵌入维度，
        self.class_num = 10  # 分类标签数(0~9)

        self.Pre_patch = nn.Conv2d(in_channeLs=self.image_channel, out_channeLs=self.channel_dim, kernel_size=patch_size, stride=patch_size)
        self.mixlayers = nn.Sequential(*[Mixer_Layer(patch_size, hidden_dim) for _ in range(depth)])
        self.norm = nn.LayerNorm(self.channel_dim)
        self.fully_connected = nn.Linear(self.channel_din, self.class_num)
        self.global_pool = torch.nean

        ########################################################################


    def forward(self, data):
        ########################################################################
        #注意维度的变化
        x = self.Pre_patch(data)
        x = x.flatten(2).transpose(1, 2)  # 展平
        x = self.mixlayers(x)
        x = self.norm(x)
        x = self.gLobal_pool(x, dim = 1)
        x = self.fully_connected(x)
        return x

        ########################################################################


def train(model, train_loader, optimizer, n_epochs, criterion):
    model.train()
    for epoch in range(n_epochs):
        for batch_idx, (data, target) in enumerate(train_loader):
            data, target = data.to(device), target.to(device)
            ########################################################################
            #计算loss并进行优化
            optimizer.zero_grad()
            pre_out = model(data)
            loss = criterion(pre_out, target)
            loss.backward()
            optimizer.step()
            ########################################################################
            if batch_idx % 100 == 0:
                print('Train Epoch: {}/{} [{}/{}]\tLoss: {:.6f}'.format(
                    epoch, n_epochs, batch_idx * len(data), len(train_loader.dataset), loss.item()))


def test(model, test_loader, criterion):
    model.eval()
    test_loss = 0.
    num_correct = 0 #correct的个数
    with torch.no_grad():
        for data, target in test_loader:
            data, target = data.to(device), target.to(device)
        ########################################################################
        #需要计算测试集的loss和accuracy
            pre_out = model(data)
            loss = criterion(pre_out, target)
            test_loss += loss.item() * data.size(0)
            num_correct += (pre_out == target).sum().item()  # 检查
        test_loss /= len(test_loader.dataset)
        accuracy = num_correct / len(test_loader.dataset)
        ########################################################################
        print("Test set: Average loss: {:.4f}\t Acc {:.2f}".format(test_loss.item(), accuracy))




if __name__ == '__main__':
    n_epochs = 5
    batch_size = 128
    learning_rate = 1e-3

    transform = transforms.Compose(
        [transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,))])

    trainset = MNIST(root = './data', train=True, download=True, transform=transform)
    train_loader = torch.utils.data.DataLoader(trainset, batch_size=batch_size, shuffle=True, num_workers=2, pin_memory=True)

    testset = MNIST(root = './data', train=False, download=True, transform=transform)
    test_loader = torch.utils.data.DataLoader(testset, batch_size=batch_size, shuffle=False, num_workers=2, pin_memory=True)

    
    ########################################################################
    model = MLPMixer(patch_size = 14, hidden_dim = 2, depth = 3).to(device) # 参数自己设定，其中depth必须大于1
    # 这里需要调用optimizer，criterion(交叉熵)
    model.to(device)
    optimizer = torch.optim.Adam(model.parameters(),lr=learning_rate)
    criterion = nn.functional.cross_entropy()
    ########################################################################
    
    train(model, train_loader, optimizer, n_epochs, criterion)
    test(model, test_loader, criterion)