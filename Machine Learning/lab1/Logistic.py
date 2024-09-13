import numpy as np
import pandas as pd
import time

class LogisticRegression:

    def __init__(self, penalty="l2", gamma=0, fit_intercept=True):
        err_msg = "penalty must be 'l1' or 'l2', but got: {}".format(penalty)
        assert penalty in ["l2", "l1"], err_msg

    def sigmoid(self, x):
        """The logistic sigmoid function"""
        return 1/(1+np.exp(-x))
    
    def model(self, X, theta):
        return self.sigmoid(np.dot(X, theta.T))
    
    def cost(self, X, y, theta):
        # 利用对数似然计算损失
        left = np.multiply(-y, np.log(self.model(X, theta)))
        right = np.multiply(1 - y, np.log(1 - self.model(X, theta)))
        return np.sum(left - right) / (len(X))

    def gradient(self, X, y, theta):
        # 梯度计算函数
        grad = np.zeros(theta.shape)
        error = (self.model(X, theta)- y)
        grad = np.dot(X.T, error)/len(X)
        
        return grad



    

    def fit(self, X, y,lr=0.01, tol=1e-7, max_iter=1e7):
        """
        Fit the regression coefficients via gradient descent or other methods 
        """
        one = np.ones(X.shape[0])
        X = np.c_[one,X]
        theta = np.zeros(X.shape[1])
        
        #梯度下降求解
    
        init_time = time.time()
        i = 0 # 迭代次数
        k = 0 # batch
        grad = np.zeros(theta.shape)
        costs = [self.cost(X, y, theta)] # 损失值

        while True:
    
            # k += batchSize #取batch数量个数据
            # if k<=len(X):
            #     grad = self.gradient(X[k-batchSize:k], y[k-batchSize:k], theta)
            # else: 
            #     grad = self.gradient(X[k-batchSize:len(X)], y[k-batchSize:len(X)], theta)
            grad = self.gradient(X, y, theta)
            theta = theta - lr*grad # 参数更新
            costs.append(self.cost(X, y, theta)) # 计算新的损失
            
            i += 1 
            if i % 2000 == 0:
                print(f'第%d次'%i)
                print(f'\tTrain Loss: {costs[-1]:.3f} ')
                t = time.time() - init_time
                print(f'用时%f秒'%t)
            if ((i>2) and (abs(costs[-1]-costs[-2])<1e-10)):
                break
            if  ((i>max_iter) or (np.linalg.norm(grad)<tol)):
                break
        self.theta = theta
        self.costs = costs
        return theta, costs

        
    def predict(self, X):
        """
        Use the trained model to generate prediction probabilities on a new
        collection of data points.
        """
        theta = self.theta
        y = self.model(X, theta)
        return y
        
# LogitRegression = LogisticRegression()
# x = np.array([[1,1],[1,1]])
# b = np.array([1,1])
# print(LogitRegression.cost(x,b.T,b)) 
# print(LogitRegression.gradient(x,b,b))  

