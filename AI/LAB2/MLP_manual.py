import torch
import torch.nn as nn
import numpy as np

def sigmoid(x):
    return 1.0 /(1 + np.exp(-x))

def diff_sigmoid(x):
    return (1 - sigmoid(x)) * sigmoid(x)

'''


        targets_1 = np.zeros((targets.shape[0], self.output_div)) + 0.01
        for i in range(len(targets)):
            targets_1[i][targets[i]] = 0.99
        output_errors = targets_1 - final_outputs
        
        
'''


class MLP:
    def __init__(self, input_div, hidden1_div, hidden2_div, output_div, learning_rate, epochs, activation_function=sigmoid):
        # 2层隐藏层
        self.input_div = input_div
        self.hidden1_div = hidden1_div
        self.hidden2_div = hidden2_div
        self.output_div = output_div

        # 权重更新时的学习率
        self.learning_rate = learning_rate

        # 初始化权重
        self.w1 = np.random.randn(self.input_div, self.hidden1_div)

        self.w2 = np.random.randn(self.hidden1_div, self.hidden2_div)

        self.w3 = np.random.randn(self.hidden2_div, self.output_div)

        # 迭代次数
        self.epochs = epochs

        # 激活函数
        self.activation_function = activation_function

    def softmax(self, X):
        exps = np.exp(X - np.max(X))
        return exps / np.sum(exps)

    def cross_entropy(self, X, y):
        '''
        X: 全连接层给出的结果 (num_examples x num_classes)
        y: 样本标签 (num_examples x 1)
        '''
        m = y.shape[0]
        p = self.softmax(X)
        log_likelihood = -np.log(p[range(m), y])
        loss = np.sum(log_likelihood) / m
        return loss

    def grad_cross_entropy(self, X, y):
        m = y.shape[0]
        grad = self.softmax(X)
        grad[range(m), y] -= 1
        grad = grad / m
        return grad

    def train(self, inputs, targets):
        for epoch in range(self.epochs):
            # 前向传播
            hidden1_inputs = np.dot(inputs, self.w1)
            hidden1_outputs = self.activation_function(hidden1_inputs)
            hidden2_inputs = np.dot(hidden1_outputs, self.w2)
            hidden2_outputs = self.activation_function(hidden2_inputs)
            final_inputs = np.dot(hidden2_outputs, self.w3)
            final_outputs = self.activation_function(final_inputs)
            # 反向传播,BP算法
            loss = self.cross_entropy(final_outputs, targets)
            print(loss)
            # w3梯度
            ls3 = final_outputs
            m = targets.shape[0]
            ls3[range(m), targets] -= 1
            grad_w3 = np.dot(hidden2_outputs.T, ls3)

            # w2梯度
            s2 = hidden2_outputs * (1.0 - hidden2_outputs)
            grad_w2 = np.dot(hidden1_outputs.T, (np.dot(ls3, self.w3.T) * s2))

            # w1梯度
            s1 = hidden1_outputs * (1.0 - hidden1_outputs)
            grad_w1 = np.dot(inputs.T, (np.dot((np.dot(ls3, self.w3.T) * s2) ,self.w2.T) * s1))
            print("w3:")
            print(self.w3)

            print("grad:")
            print(grad_w3)
            ''''
            output_errors = self.grad_cross_entropy(final_outputs, targets)
            hidden2_errors = np.dot(output_errors, self.w3.T)
            hidden1_errors = np.dot(hidden2_errors, self.w2.T)

            # 梯度下降更新w
            self.w3 -= self.learning_rate * np.dot(hidden2_outputs.T, (output_errors * final_outputs * (1.0 - final_outputs)))

            self.w2 -= self.learning_rate * np.dot(hidden1_outputs.T, (hidden2_errors * hidden2_outputs * (1.0 - hidden2_outputs)))

            self.w1 -= self.learning_rate * np.dot(inputs.T, (hidden1_errors * hidden1_outputs * (1.0 - hidden1_outputs)))
            '''

            # 梯度下降更新

            self.w3 -= self.learning_rate * grad_w3
            self.w2 -= self.learning_rate * grad_w2
            self.w1 -= self.learning_rate * grad_w1


    def pred(self, inputs):
        hidden1_inputs = np.dot(inputs, self.w1)
        hidden1_outputs = self.activation_function(hidden1_inputs)
        hidden2_inputs = np.dot(hidden1_outputs, self.w2)
        hidden2_outputs = self.activation_function(hidden2_inputs)
        final_inputs = np.dot(hidden2_outputs, self.w3)
        final_outputs = self.activation_function(final_inputs)
        return final_outputs
# 数据
x = np.random.rand(100, 5)
y = np.random.rand(100, 1)
y = [int(3*i) for i in y]
y = np.array(y).reshape(100, 1)

# 输入
input_div = 5
hidden1_div = 4
hidden2_div = 4
output_div = 3
epochs = 10
learning_rate = 0.3

# 构建MLP模型
model = MLP(input_div,hidden1_div, hidden2_div, output_div, learning_rate,epochs, sigmoid)

model.train(x, y)

x_test = x

pred = model.pred(x_test)
#print(pred)