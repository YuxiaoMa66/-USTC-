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
        self.mlp1 =
        self.mpl2 =
        self.skip_connection =
        self.layernorm = nn.functional.layer_norm(self.skip_connection,hidden_dim)
        ########################################################################

    def forward(self, x):
        ########################################################################

        ########################################################################


class MLPMixer(nn.Module):
    def __init__(self, patch_size, hidden_dim, depth):
        super(MLPMixer, self).__init__()
        assert 28 % patch_size == 0, 'image_size must be divisible by patch_size'
        assert depth > 1, 'depth must be larger than 1'
        ########################################################################
        #这里写Pre-patch Fully-connected, Global average pooling, fully connected
        self.Pre_patch =
        self.Fully_connected =
        self.Global_average_pooling =
        self.fully_connected =
        ########################################################################


    def forward(self, data):
        ########################################################################
        #注意维度的变化
        
        ########################################################################


def train(model, train_loader, optimizer, n_epochs, criterion):
    model.train()
    for epoch in range(n_epochs):
        for batch_idx, (data, target) in enumerate(train_loader):
            data, target = data.to(device), target.to(device)
            ########################################################################
            #计算loss并进行优化
            optimizer.zero_grad()   #清空
            pre_out = model(data)   #预测
            loss = criterion(pre_out, target)   #计算交叉熵
            loss.backward()  #反向传播
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
            num_correct += (pre_out == target).sum().item()  #检查
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
    model = MLPMixer(patch_size = , hidden_dim = , depth = ).to(device) # 参数自己设定，其中depth必须大于1
    # 这里需要调用optimizer，criterion(交叉熵)
    model.to(device)
    optimizer = torch.optim.Adam(model.parameters(),lr=learning_rate)
    criterion = nn.functional.cross_entropy()
    ########################################################################
    
    train(model, train_loader, optimizer, n_epochs, criterion)
    test(model, test_loader, criterion)