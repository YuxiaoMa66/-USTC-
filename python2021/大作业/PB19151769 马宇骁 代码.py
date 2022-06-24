import csv
import pandas as pd
import easygui as eg

class Book:
    def __init__(self, book_ID, book_name, ISBN, pub, date, author, number):
        self.book_name = book_name
        self.book_ID = book_ID
        self.ISBN = ISBN
        self.pub = pub
        self.date = date
        self.author = author
        self.number = number

    def __getitem__(self, item):
        if item in self.__dict__:
            return self.__dict__[item]

#status为1代表是会员
class Reader:
    def __init__(self, reader_ID, reader_name, tel, status):
        self.reader_name = reader_name
        self.reader_ID = reader_ID
        self.tel = tel
        self.status = status
        self.lend = {}
        self.lent = {}
    def __getitem__(self, item):
        if item in self.__dict__:
          return self.__dict__[item]
      
def insert_book():
    try:
        name = eg.enterbox(msg=' 请输入导入数据 ', title='图书管理系统管理员模式', default=' ', strip=True, image=None)
        c = pd.read_excel(name)
        for i in range(len(c)):
            m = []
            for k in c.loc[i]:
                m.append(k)
            books.append(Book(str(m[0]),str(m[1]),str(m[2]),str(m[3]),str(m[4]),str(m[5]),int(m[6])))
        eg.msgbox(msg="导入成功！",title="图书管理系统管理员模式",ok_button="确定")
    except:
        eg.msgbox(msg="导入失败！",title="图书管理系统管理员模式",ok_button="确定")
        
def add_book():
    m = eg.multenterbox(msg='增添图书', title='图书管理系统管理员模式', fields=['id','name','ISBN','pub','date','author','number'], values=())
    books.append(Book(str(m[0]),str(m[1]),str(m[2]),str(m[3]),str(m[4]),str(m[5]),int(m[6])))
# （3）删除书目
def delete_book():
    id = eg.enterbox(msg=' 请输入删除的书id ', title='图书管理系统管理员模式', default=' ', strip=True, image=None)
    
    for i in books:
        if i.book_ID == id:
            if i.number == 0:
                books.remove(i)
                break
    else:
        eg.msgbox(msg="操作拒绝",title="图书管理系统管理员模式",ok_button="确定")

def modify_book():
    id = eg.enterbox(msg=' 待修改的书id ', title='图书管理系统管理员模式', default=' ', strip=True, image=None)
    id = str(id)
    for i in books:
        if i.book_ID == id:
            new = eg.multenterbox(msg=id, title='图书管理系统管理员模式修改图书信息', fields=['name','ISBN','pub','date','author','number'], values=())
            i.book_name = new[0] if  new[0] is not None else i.book_name
            i.ISBN = new[1] if new[1] is not None else i.ISBN
            i.pub = new[2] if new[2] is not None else i.pub
            i.date = new[3] if new[3] is not None else i.date
            i.author = new[4] if new[4] is not None else i.author
            i.number = new[5] if new[5] is not None else i.number
            i.number = int(i.number)
            break
    if i.book_ID != id:
        eg.msgbox(msg="不存在这本书",title="图书管理系统管理员模式",ok_button="确定")
        
# 输入书名以及要修改的属性
def add_num():
    n = eg.multenterbox(msg='增添已有图书', title='图书管理系统管理员模式', fields=['name','number'], values=())
    num = int(n[1])
    name = n[0]
    for i in books:
        if i.book_name == name:
            i.number += num
            break
    if i.book_name != name:
        eg.msgbox(msg="不存在这本书",title="图书管理系统管理员模式",ok_button="确定")
def sub_num():
    n = eg.multenterbox(msg='减少已有图书', title='图书管理系统管理员模式', fields=['name','number'], values=())
    num = int(n[1])
    name = n[0]
    for i in books:
        if i.book_name == name:  
            if i.number == 0:
                eg.msgbox(msg="这本书没有了不能减少",title="图书管理系统管理员模式",ok_button="确定")
                break   
            else:  
                if i.number-num < 0: 
                    eg.msgbox(msg="这本书不能减少这么多",title="图书管理系统管理员模式",ok_button="确定")
                    break   
                else: 
                    i.number -= num
                    break
    if i.book_name != name:
        eg.msgbox(msg="不存在这本书",title="图书管理系统管理员模式",ok_button="确定")
# 即修改数量属性，且减少后数量不能小于0

# （6）分菜单
def manage_book():
    while True:
        choice = eg.buttonbox(msg='''
            图书管理系统：
            
         1.导入书目
         2.增加书目
         3.删除书目
         4.修改书目
         5.库存增加
         6.库存减少
         0.退出
            ''', title='管理员模式 ', choices=('1', '2', '3','4','5','6','0'), image=None)
        
        if choice == '1':
            insert_book()
        elif choice == '2':
            add_book()
        elif choice == '3':
            delete_book()
        elif choice == '4':
            modify_book()
        elif choice == '5':
            add_num()
        elif choice == '6':
            sub_num()
        elif choice == '0':
            break

def insert_reader():
    try:
        name = eg.enterbox(msg=' 请输入导入数据 ', title='图书管理系统管理员模式', default=' ', strip=True, image=None)
        c = pd.read_excel(name)
        c = c.fillna(0)
        for i in range(len(c)):
            m = []
            for k in c.loc[i]:
                m.append(k)
            readers.append(Reader(str(m[0]),str(m[1]),str(m[2]),int(m[3])))
            readers[i].lend = eval(c['lend'][i]) if c['lend'][i] != 0 else {}
            readers[i].lent = eval(c['lent'][i]) if c['lent'][i] != 0 else {}
        eg.msgbox(msg="导入成功！",title="图书管理系统管理员模式",ok_button="确定")
    except:
        eg.msgbox(msg="导入失败！",title="图书管理系统管理员模式",ok_button="确定")
        
def add_reader():
    m = eg.multenterbox(msg='增添读者', title='图书管理系统管理员模式', fields=['id','name','tel','status'], values=())
    readers.append(Reader(str(m[0]),str(m[1]),str(m[2]),int(m[3])))


def delete_reader():
    id = eg.enterbox(msg=' 请输入删除的读者id ', title='图书管理系统管理员模式', default=' ', strip=True, image=None)
    for i in readers:
        if i.reader_ID == id:
            readers.remove(i)
            break
    if i.reader_ID != id:
        eg.msgbox(msg="不存在这个人",title="图书管理系统管理员模式",ok_button="确定")


def modify_reader():
    id = eg.enterbox(msg=' 待修改的读者ID ', title='图书管理系统管理员模式', default=' ', strip=True, image=None)
    for i in readers:
        if i.reader_ID == id:
            new = eg.multenterbox(msg=id, title='图书管理系统管理员模式修改图书信息', fields=['name','tel','status'], values=())
            i.reader_name = new[0] if new[0] is not None else i.reader_name
            i.tel = new[1] if new[1] is not None else i.tel
            i.status = int(new[2]) if new[2] is not None else i.status
            break
    if i.reader_ID != id:
        eg.msgbox(msg="不存在这个人",title="图书管理系统管理员模式",ok_button="确定")
        

            
def manage_reader():
    while True:
        choice = eg.buttonbox(msg='''
            读者管理系统：
            
         1.导入读者
         2.增加读者
         3.删除读者
         4.修改读者信息      
         0.退出
            ''', title='管理员模式 ', choices=('1', '2', '3','4','0'), image=None)
        
        if choice == '1':
            insert_reader()
        elif choice == '2':
            add_reader()
        elif choice == '3':
            delete_reader()
        elif choice == '4':
            modify_reader()
        elif choice == '0':
            break


# 5.图书、读者信息查询
def search_book():
    while True:
        choice = eg.buttonbox(msg='''
            图书信息查询：
            
         1.书名
         2.作者
         3.出版社
         4.ISBN      
         0.退出
            ''', title='管理员模式 ', choices=('1', '2', '3','4','0'), image=None)
        
        if choice == '0':
            break
        key = eg.enterbox(msg=' 请输入查询的内容 ', title='图书管理系统管理员模式', default=' ', strip=True, image=None)
        temp = []
        tmp = []
        if choice == '1':
            for i in books:
                if i.book_name == key:
                    temp.append(i)
        elif choice == '2':
            for i in books:
                if i.author == key:
                    temp.append(i)
        elif choice == '3':
            for i in books:
                if i.pub == key:
                    temp.append(i)
        elif choice == '4':
            for i in books:
                if i.ISBN == key:
                    temp.append(i)
        
        for j in temp:
            for (k, v) in j.__dict__.items():
                t=[]
                t.append(k)
                t.append(v)
                tmp.append(t)
        eg.msgbox(msg=tmp,title="图书管理系统管理员模式",ok_button="确定")

def search_num():
    key = eg.enterbox(msg=' 请输入图书名字查询的库存 ', title='图书管理系统管理员模式', default=' ', strip=True, image=None)
    for i in books:
        if i.book_name == key:
            num = i.number
            break
    for i in readers:
        if i.lend[key]:
            num = num + i.lend[key] 
    eg.msgbox(msg=num,title="图书管理系统管理员模式",ok_button="确定")


def search_reader():
    while True:
        choice = eg.buttonbox(msg='''
            读者查询：
            
         1.读者名
         2.读者id
         3.联系方式
         0.退出
            ''', title='管理员模式 ', choices=('1', '2', '3','0'), image=None)
        
        if choice == '0':
            break
        key = eg.enterbox(msg=' 请输入查询的内容 ', title='图书管理系统管理员模式', default=' ', strip=True, image=None)
        temp = []
        tmp = []
        if choice == '1':
            for i in readers:
                if i.reader_name == key:
                    temp.append(i)
        elif choice == '2':
            for i in readers:
                if i.reader_ID == key:
                    temp.append(i)
        elif choice == '3':
            for i in readers:
                if i.tel == key:
                    temp.append(i)
        for i in temp:
            for (k, v) in i.__dict__.items():
                t=[]
                t.append(k)
                t.append(v)
                tmp.append(t)
        eg.msgbox(msg=tmp,title="图书管理系统管理员模式",ok_button="确定")



# 6、图书借还
#字典值相加
def returnSum(myDict):      
    sum = 0
    for i in myDict: 
        sum = sum + myDict[i]     
    return sum


def lend_book():
    av = []
    for i in books:
        if i.number > 0:
            av.append(i.book_name)
    eg.msgbox(msg=av,title="可借的书",ok_button="确定")
    name = eg.multenterbox(msg='借书信息', title='图书管理系统管理员模式', fields=['book_name','reader_name'], values=())
    name1 = name[0]
    name2 = name[1]
    for i in books:
        if i.book_name == name1:
            break
    if i.book_name != name1:
        eg.msgbox(msg='没这本书',title="图书管理系统管理员模式",ok_button="确定")
        return 0
    for j in readers:
        if j.reader_name == name2:
            break
    if j.reader_name != name2:
        eg.msgbox(msg='没这个人',title="图书管理系统管理员模式",ok_button="确定")
        return 0
    
    #jlend = 0
    if (j.lend):
        jlend = returnSum(j.lend)
    if (j.status == 1) and (jlend >= 8):
        eg.msgbox(msg='会员借书达到上限',title="图书管理系统管理员模式",ok_button="确定")
    elif (j.status == 0) and (jlend >= 4):
        eg.msgbox(msg='借书达到上限',title="图书管理系统管理员模式",ok_button="确定")
    elif i.number == 0:
        eg.msgbox(msg='剩余不够',title="图书管理系统管理员模式",ok_button="确定")
    else:
        if name1 in j.lend:
            j.lend[name1] += 1
        else:
            j.lend[name1] = 1
        if name1 in j.lent:
            j.lent[name1] += 1
        else:
            j.lent[name1] = 1
        i.number = i.number - 1
        eg.msgbox(msg='这本书借之后可借为:'+str(i.number),title="图书管理系统管理员模式",ok_button="确定")


def return_book():
    name = eg.multenterbox(msg='借书信息', title='图书管理系统管理员模式', fields=['book_name','reader_name'], values=())
    name1 = name[0]
    name2 = name[1]
    for i in books:
        if i.book_name == name1:
            break
    if i.book_name != name1:
        eg.msgbox(msg='没这本书',title="图书管理系统管理员模式",ok_button="确定")
        return 0
    for j in readers:
        if j.reader_name == name2:
            break
    if j.reader_name != name2:
        eg.msgbox(msg='没这个人',title="图书管理系统管理员模式",ok_button="确定")
        return 0
    if name1 not in j.lend:
        eg.msgbox(msg='ta没借这本书',title="图书管理系统管理员模式",ok_button="确定")
        return 0
    j.lend[name1] -= 1
    i.number += 1
    eg.msgbox(msg='这本书还之后可借为:'+str(i.number),title="图书管理系统管理员模式",ok_button="确定")
    
# 先判断读者是否能继续借书，若借书上限满、库存不够则不能继续借。

# 还书时判断读者是否持有这本书

# 其中为使类与字典转换，添加getitem

# 主函数以及菜单
books = []
readers = []
def main():
    B = pd.read_excel(r'C:\Users\Moriarty\Desktop\python\2021秋\大作业\origin.xls')
    R = pd.read_excel(r'C:\Users\Moriarty\Desktop\python\2021秋\大作业\origin2.xls')
    R = R.fillna(0)
    for i in range(len(B)):
        m = []
        for k in B.loc[i]:
            m.append(k)
        books.append(Book(str(m[0]),str(m[1]),str(m[2]),str(m[3]),str(m[4]),str(m[5]),m[6]))
    for i in range(len(R)):
        m = []
        for k in R.loc[i]:
            m.append(k)
        readers.append(Reader(str(m[0]),str(m[1]),str(m[2]),int(m[3])))
        readers[i].lend = eval(R['lend'][i]) if R['lend'][i] != 0 else {}
        readers[i].lent = eval(R['lent'][i]) if R['lent'][i] != 0 else {}
    while True:
        a = eg.buttonbox(msg='''
            欢迎使用图书管理系统:
            
            1.图书信息维护
            2.读者信息维护
            3.图书信息查询
            4.读者信息查询
            5.图书借出
            6.图书归还
            7.库存
            0.退出
            ''', title='图书管理系统 ', choices=('1', '2', '3','4','5','6','7','0'), image=None)
        if a == '1':
            manage_book()
        elif a == '2':
            manage_reader()
        elif a == '3':
            search_book()
        elif a == '4':
            search_reader()
        elif a == '5':
            lend_book()
        elif a == '6':
            return_book()
        elif a == '7':    
            search_num()
        elif a == '0':
            for i in range(len(B)):
                B = B.drop([i])
            idd,nm,isbn,pub,date,au,nu = [],[],[],[],[],[],[]
            for m in books:
                idd.append(m.book_ID)
                nm.append(m.book_name)
                isbn.append(m.ISBN)
                pub.append(m.pub)
                date.append(m.date)
                au.append(m.author)
                nu.append(m.number)
            B['book_ID'] = idd
            B['book_name'] = nm
            B['ISBN'] = isbn
            B['pub'] = pub
            B['date'] = date
            B['author'] = au
            B['number'] = nu
            B.to_excel(r'C:\Users\Moriarty\Desktop\python\2021秋\大作业\origin.xls',index=None)
            
            for i in range(len(R)):
                R = R.drop([i])
            idd,nm,tel,st,ld,lt = [],[],[],[],[],[]
            for m in readers:
                idd.append(m.reader_ID)
                nm.append(m.reader_name)
                tel.append(m.tel)
                st.append(m.status)
                ld.append(m.lend)
                lt.append(m.lent)
            R['reader_ID'] = idd
            R['reader_name'] = nm
            R['tel'] = tel
            R['status'] = st
            R['lend'] = ld
            R['lent'] = lt
            R.to_excel(r'C:\Users\Moriarty\Desktop\python\2021秋\大作业\origin2.xls',index=None)
                
            break
        

nm = '管理员登陆'
cd = '图书管理系统'
while True:
    id,mm = eg.multpasswordbox(nm,cd,(['用户名','密码']))
    if (id == 'tesla606') and (mm == '802366'):
        main()
        break
