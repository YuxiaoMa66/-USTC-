import torch
import numpy as np
import matplotlib.pyplot as plt


def sigmoid(x):
    return 1.0 / (1 + np.exp(-x))


def diff_sigmoid(x):
    return sigmoid(x) * (1 - sigmoid(x))


class MLP_manual:
    def __init__(self, input, n1_in, n2_in, n_out, learning_rate, epochs, activation=sigmoid):

        self.input = input
        self.n1_in = n1_in  #第一个隐藏层的维数
        self.n2_in = n2_in  #第二个隐藏层的维数
        self.n_out = n_out
        self.learning_rate = learning_rate
        self.epochs = epochs    # 迭代次数
        self.activation = activation    # 激活函数
        self.w1 = np.random.randn(self.input, self.n1_in)
        self.w2 = np.random.randn(self.n1_in, self.n2_in)
        self.w3 = np.random.randn(self.n2_in, self.n_out)


    def softmax(self, X):
        return np.exp(X - np.max(X)) / np.sum(np.exp(X - np.max(X)))

    def cross_entropy(self, X, y):
        m = y.shape[0]
        softmax = self.softmax(X)
        L = np.zeros((m, 1))
        for i in range(m):
            h = softmax[i, y[i]]
            L[i][0] = -np.log(h)
        loss = np.sum(L) / m
        return loss

    def grad_cross_entropy(self, X, y):
        m = y.shape[0]
        grad = self.softmax(X)
        grad[range(m), y] -= 1
        grad = grad / m
        return grad

    def train(self, inputs, targets):
        show_loss = np.zeros((self.epochs, 2))
        for epoch in range(self.epochs):
            # Forward
            hidden1_inputs = np.dot(inputs, self.w1)
            hidden1_outputs = self.activation(hidden1_inputs)
            hidden2_inputs = np.dot(hidden1_outputs, self.w2)
            hidden2_outputs = self.activation(hidden2_inputs)
            final_inputs = np.dot(hidden2_outputs, self.w3)
            final_outputs = self.activation(final_inputs)
            # BP
            loss = self.cross_entropy(final_outputs, targets)
            show_loss[epoch, 0] = epoch
            show_loss[epoch, 1] = loss

            # w3
            ls3 = final_outputs
            m = targets.shape[0]
            ls3[range(m), targets.astype('int64')] -= 1
            grad_w3 = np.dot(hidden2_outputs.T, ls3)

            # w2
            s2 = hidden2_outputs * (1.0 - hidden2_outputs)
            grad_w2 = np.dot(hidden1_outputs.T, (np.dot(ls3, self.w3.T) * s2))

            # w1
            s1 = hidden1_outputs * (1.0 - hidden1_outputs)
            grad_w1 = np.dot(inputs.T, (np.dot((np.dot(ls3, self.w3.T) * s2), self.w2.T) * s1))
            print("w3:")
            print(self.w3)

            print("grad:")
            print(grad_w3)

            # 梯度下降
            self.w3 -= self.learning_rate * grad_w3
            self.w2 -= self.learning_rate * grad_w2
            self.w1 -= self.learning_rate * grad_w1


        plt.plot(show_loss[:, 0], show_loss[:, 1])
        plt.xlabel('epochs')
        plt.ylabel('loss')
        plt.show()
        print('grad_W1 : \n', grad_w1)
        print('grad_W2 : \n', grad_w2)
        print('grad_W3 : \n', grad_w3)





    def pred(self, inputs):
        hidden1_inputs = np.dot(inputs, self.w1)
        hidden1_outputs = self.activation(hidden1_inputs)
        hidden2_inputs = np.dot(hidden1_outputs, self.w2)
        hidden2_outputs = self.activation(hidden2_inputs)
        final_inputs = np.dot(hidden2_outputs, self.w3)
        final_outputs = self.activation(final_inputs)
        return final_outputs


# 数据
x = np.random.rand(100, 5)
y = np.random.rand(100, 1)
y = [int(3*i) for i in y]
y = np.array(y).reshape(100, 1)

# 输入
input = 5
n1_in = 4
n2_in = 4
n_out = 3
epochs = 100
learning_rate = 0.01

# 构建MLP模型
model = MLP_manual(input, n1_in, n2_in, n_out, learning_rate, epochs, sigmoid)

model.train(x, y)

x_test = x

pred = model.pred(x_test)
print(pred)