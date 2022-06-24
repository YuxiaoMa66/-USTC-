import numpy as np
import cvxopt #用于求解线性规划
from process_data import load_and_process_data
from evaluation import get_micro_F1,get_macro_F1,get_acc


#根据指定类别main_class生成1/-1标签
def svm_label(labels,main_class):
    new_label=[]
    for i in range(len(labels)):
        if labels[i]==main_class:
            new_label.append(1)
        else:
            new_label.append(-1)
    return np.array(new_label)

# 实现线性回归
class SupportVectorMachine:

    '''参数初始化 
    lr: 梯度更新的学习率
    Lambda: L2范数的系数
    epochs: 更新迭代的次数
    '''
    def __init__(self,kernel,C,Epsilon):
        self.kernel=kernel
        self.C = C
        self.Epsilon=Epsilon

    '''KERNEL用于计算两个样本x1,x2的核函数'''
    def KERNEL(self, x1, x2, kernel='Poly', d=2, sigma=1):
        #d是多项式核的次数,sigma为Gauss核的参数
        K = 0
        if kernel == 'Gauss':
            K = np.exp(-(np.sum((x1 - x2) ** 2)) / (2 * sigma ** 2))
        elif kernel == 'Linear':
            K = np.dot(x1,x2)
        elif kernel == 'Poly':
            K = np.dot(x1,x2) ** d
        else:
            print('No support for this kernel')
        return K

    '''
    根据训练数据train_data,train_label（均为np数组）求解svm,并对test_data进行预测,返回预测分数，即svm使用符号函数sign之前的值
    train_data的shape=(train_num,train_dim),train_label的shape=(train_num,) train_num为训练数据的数目，train_dim为样本维度
    预测结果的数据类型应为np数组，shape=(test_num,1) test_num为测试数据的数目
    '''
    def fit(self,train_data,train_label,test_data):
        '''
        需要你实现的部分
        '''

        m, n = train_data.shape
        K = np.zeros((m, m))  # 初始化
        for i in range(m):
            for j in range(m):
                K[i][j] = self.KERNEL(train_data[i], train_data[j])
        P = cvxopt.matrix(np.outer(train_label, train_label) * K)
        A = cvxopt.matrix(np.ones(m) * train_label, (1, m))
        q = cvxopt.matrix(np.ones(m) * -1)
        b = cvxopt.matrix(0.0)

        arg1 = np.diag(np.ones(m) * -1)
        arg2 = np.diag(np.ones(m))
        G = cvxopt.matrix(np.vstack((arg1, arg2)))
        arg1 = np.zeros(m)
        arg2 = np.ones(m) * self.C
        h = cvxopt.matrix(np.hstack((arg1, arg2)))

        solution = cvxopt.solvers.qp(P, q, G, h, A, b)
        a = np.ravel(solution['x'])

        sv = a > self.Epsilon
        index = np.arange(len(a))[sv]  # a>self.Epsilon 返回true or false的数组   取出对应为true的下标

        self.a = a[sv]  # 大于0对应的a的值index
        self.sv_X = train_data[sv]  # 支持向量的train_data index
        self.sv_y = train_label[sv]  # 支持向量的train_label  index

        print('%d 点中有 %d 个支持向量' % (m, len(self.a)))

        #算w以及b
        # 求w

        if self.kernel == 'Linear':
            self.w = np.zeros(n)
            for i in range(len(self.a)):
                self.w += self.a[i] * self.sv_y[i] * self.sv_X[i]
        else:
            self.w = None

        # 求b
        self.b = 0
        for i in range(len(self.a)):
            self.b += self.sv_y[i]
            self.b -= np.sum(self.a * self.sv_y * K[index[i]][index])
        self.b /= len(self.a)

        if self.kernel == 'Linear':
            aa = np.dot(test_data, self.w) + self.b
            aa = aa.reshape(-1, 1)
            return aa
        else:
            y_predict = np.zeros(len(test_data))
            for i in range(len(test_data)):
                s = 0
                for a, sv_y, sv_ in zip(self.a, self.sv_y, self.sv_X):
                    s += a * sv_y * self.KERNEL(test_data[i], sv_)
                y_predict[i] = s
            return np.array(y_predict + self.b).reshape(-1,1)


def main():
    # 加载训练集和测试集
    Train_data,Train_label,Test_data,Test_label=load_and_process_data()
    Train_label=[label[0] for label in Train_label]
    Test_label=[label[0] for label in Test_label]
    train_data=np.array(Train_data)
    test_data=np.array(Test_data)
    test_label=np.array(Test_label).reshape(-1,1)
    #类别个数
    num_class=len(set(Train_label))


    #kernel为核函数类型，可能的类型有'Linear'/'Poly'/'Gauss'
    #C为软间隔参数；
    #Epsilon为拉格朗日乘子阈值，低于此阈值时将该乘子设置为0
    kernel='Poly'
    C = 1
    Epsilon=10e-5
    #生成SVM分类器
    SVM=SupportVectorMachine(kernel,C,Epsilon)

    predictions = []
    #one-vs-all方法训练num_class个二分类器
    for k in range(1,num_class+1):
        #将第k类样本label置为1，其余类别置为-1
        train_label=svm_label(Train_label,k)
        # 训练模型，并得到测试集上的预测结果
        prediction=SVM.fit(train_data,train_label,test_data)
        predictions.append(prediction)
    predictions=np.array(predictions)
    #one-vs-all, 最终分类结果选择最大score对应的类别
    pred=np.argmax(predictions,axis=0)+1
    print(pred)
    # 计算准确率Acc及多分类的F1-score
    print("Acc: "+str(get_acc(test_label,pred)))
    print("macro-F1: "+str(get_macro_F1(test_label,pred)))
    print("micro-F1: "+str(get_micro_F1(test_label,pred)))


main()