import numpy as np
import math
from collections import Counter
from process_data import load_and_process_data
from evaluation import get_micro_F1,get_macro_F1,get_acc

class NaiveBayes:
    '''参数初始化
    Pc: P(c) 每个类别c的概率分布
    Pxc: P(c|x) 每个特征的条件概率
    '''
    def __init__(self):
        self.Pc={}
        self.Pxc={}

    '''
    通过训练集计算先验概率分布p(c)和条件概率分布p(x|c)
    建议全部取log，避免相乘为0
    '''
    def fit(self,traindata,trainlabel,featuretype):
        '''
        需要你实现的部分
        '''
        X = np.mat(traindata)
        C = np.mat(trainlabel)
        #print(C.min())发现最小值是1，最大值是3
        tol = np.size(C, 0)
        #用拉普拉斯平滑计算
        P = np.zeros((3,1))
        for k in range(3):
            P[k,0] = (np.sum(C == k+1)+1) / (tol+3)
        #print(X[:,0].min())X的第一列为1到3的离散型数据
        A = np.hstack((X,C))
        PX1 = np.zeros((3,3))
        for i in range(3):
            for j in range(3):
                PX1[i,j] = (np.sum((A[:,0]==i+1) & (A[:,8]==j+1)) +1) / (tol+3)
        #对于连续型数据，考虑用正态分布,计算均值和方差
        B = np.zeros((7,6))     #第奇数列是均值，第偶数列是方差
        for k in range(7):
            for i in range(3):
                tem = (A[:, 8] == (i + 1))
                cont = np.sum(tem == True)
                m = 0
                temp = np.zeros((cont,9))
                for j in range(tol):
                    if(A[j,8] == (i+1)):
                        temp[m,:] = A[j,:]
                        m = m+1
                B[k, 2 * (i)] = np.mean(temp[:, k + 1])
                B[k, 2 * (i + 1)-1] = np.var(temp[:, k + 1])
        #用一个8*9的矩阵统一一下
        PX = np.zeros((1,9))
        for i in range(3):
            PX[0,i] = PX1[i,0]
            PX[0,i+3] = PX1[i,1]
            PX[0,i+6] = PX1[i,2]
        temp = np.zeros((7,3))
        BX = np.hstack((B,temp))
        PX = np.vstack((PX,BX))
        self.Pc = P
        self.Pxc = PX


    '''
    根据先验概率分布p(c)和条件概率分布p(x|c)对新样本进行预测
    返回预测结果,预测结果的数据类型应为np数组，shape=(test_num,1) test_num为测试数据的数目
    feature_type为0-1数组，表示特征的数据类型，0表示离散型，1表示连续型
    '''
    def predict(self,features,featuretype):
        '''
        需要你实现的部分
        '''
        P = self.Pc
        PX = self.Pxc
        X = features
        m = np.size(X,0)
        y = np.zeros((m,1))
        for k in range(m):
            temp1 = np.zeros((3,1))
            temp2 = np.zeros((8,3))
            for i in range(8):
                if i==0:
                    for h in range(3):
                        if (X[k,0] == h+1):
                            for j in range(3):
                                temp2[0,j] = PX[0,j]
                else:
                    for j in range(3):
                            temp2[i,j] = 1/((2*math.pi*PX[i,2 * (j + 1)-1])**0.5) * math.exp(-(X[k,i]-PX[i,2*(j)])**2 / (2*PX[i,2 * (j + 1)-1]))
            for l in range(3):
                temp1[l,0] = P[l,0]
                for h in range(8):
                    temp1[l,0] = temp1[l,0]*temp2[h,l]
            c = np.argmax(temp1)+1
            y[k,0] = c
        y = np.array(y)
        return y


def main():
    # 加载训练集和测试集
    train_data,train_label,test_data,test_label=load_and_process_data()
    feature_type=[0,1,1,1,1,1,1,1] #表示特征的数据类型，0表示离散型，1表示连续型

    Nayes=NaiveBayes()
    Nayes.fit(train_data,train_label,feature_type) # 在训练集上计算先验概率和条件概率

    pred=Nayes.predict(test_data,feature_type)  # 得到测试集上的预测结果

    # 计算准确率Acc及多分类的F1-score
    print("Acc: "+str(get_acc(test_label,pred)))
    print("macro-F1: "+str(get_macro_F1(test_label,pred)))
    print("micro-F1: "+str(get_micro_F1(test_label,pred)))

main()