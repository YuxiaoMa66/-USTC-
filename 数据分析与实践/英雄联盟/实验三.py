#导入需要的包
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import warnings

'''
warnings.filterwarnings('ignore')
%matplotlib inline
plt.style.use('ggplot')
'''
#加载数据集
lol_rowdata = pd.read_csv(r'C:\Users\Moriarty\Desktop\python\lol\exp3.csv')

'''
#检查缺失数据
n = sum(lol_rowdata.isnull().sum())
print(n)
'''
'''
#查看数据类型
print(lol_rowdata.dtypes.value_counts())

print(lol_rowdata.shape)
'''

#提取数据出来分析
cols = lol_rowdata.columns #标题
lol_result = lol_rowdata.team1_win

'''
#先看看数据集中胜利和失败的游戏各占多少
num = 0
num1 = 0
for i in lol_result:
    if i == 1:
        num += 1
    else:
        num1 += 1
win_ratio = num/(num+num1)
#绘制饼图可视化一下
plt.figure(figsize=(6,6))
sizes=[win_ratio,1-win_ratio]
labels=('Victory','Defeat')
plt.pie(sizes,labels=labels,autopct='%1.0f%%')

for i in lol_rowdata.mapId:
    if i == 12:
        lol_rowdata.mapId.remove(i)
    else:
        continue

lol_rowdata['index'].groupby(lol_rowdata['queueId']).count()
'''
'''
df_remove = df[df['team_role'] == '1-MID'].groupby('matchid').agg({'team_role':'count'})
df_remove[df_remove['team_role'] != 1].index.values
'''
'''
map = lol_rowdata.mapId
queue = lol_rowdata.queueId
c = 0
c1 = 0
for i in map:
    if i == 12 and queue[c1] == 450:
        c += 1
    else:
        continue
    c1 += 1
print(c)
'''

lol = lol_rowdata.drop(lol_rowdata[lol_rowdata['queueId'] == (450 or 700 or 900 or 1020)].index)
i = 1
def position(row,i):
    if row['player'+str(i)+'_role'] in ('DUO_SUPPORT', 'DUO_CARRY'):
        return row['player'+str(i)+'_role']
    else:
        return row['player'+str(i)+'_lane']
while i <= 10: 
    lol['player'+str(i)+'_position'] = lol.apply(position ,args=(i,),axis = 1)
    i += 1

i = 1
while i<= 10:
    lol = lol.drop(lol[lol['player'+str(i)+'_position'] == 'NONE'].index)
    i += 1
print(lol['player10_position'])


'''
print(lol['team1_firstBlood'][1]==0)

first_blood_win = lol[(lol['team1_win']==1) & (lol['team1_firstBlood']== 1)]['index'].count()/lol[lol['team1_firstBlood']==1]['index'].count()
first_tower_win = lol[(lol['team1_win']==1) & (lol['team1_firstTower']== 1)]['index'].count()/lol[lol['team1_firstTower']==1]['index'].count()
first_inhibitor_win = lol[(lol['team1_win']==1) & (lol['team1_firstInhibitor']== 1)]['index'].count()/lol[lol['team1_firstInhibitor']==1]['index'].count()
first_baron_win = lol[(lol['team1_win']==1) & (lol['team1_firstBaron']== 1)]['index'].count()/lol[lol['team1_firstBaron']==1]['index'].count()
first_gragon_win = lol[(lol['team1_win']==1) & (lol['team1_firstDragon']== 1)]['index'].count()/lol[lol['team1_firstDragon']==1]['index'].count()
first_riftherald_win = lol[(lol['team1_win']==1) & (lol['team1_firstRiftHerald']== 1)]['index'].count()/lol[lol['team1_firstRiftHerald']==1]['index'].count()

first_blood_lose = lol[(lol['team1_win']==1) & (lol['team1_firstBlood']== 0)]['index'].count()/lol[lol['team1_firstBlood']==0]['index'].count()
first_tower_lose = lol[(lol['team1_win']==1) & (lol['team1_firstTower']== 0)]['index'].count()/lol[lol['team1_firstTower']==0]['index'].count()
first_inhibitor_lose = lol[(lol['team1_win']==1) & (lol['team1_firstInhibitor']== 1)]['index'].count()/lol[lol['team1_firstInhibitor']==1]['index'].count()
first_baron_lose = lol[(lol['team1_win']==1) & (lol['team1_firstBaron']== 0)]['index'].count()/lol[lol['team1_firstBaron']==0]['index'].count()
first_gragon_lose = lol[(lol['team1_win']==1) & (lol['team1_firstDragon']== 0)]['index'].count()/lol[lol['team1_firstDragon']==0]['index'].count()
first_riftherald_lose = lol[(lol['team1_win']==1) & (lol['team1_firstRiftHerald']== 0)]['index'].count()/lol[lol['team1_firstRiftHerald']==0]['index'].count()


plt.figure(figsize=(10,10))

axe1=plt.subplot(1,2,1)
axe1.pie([first_blood_win,1-first_blood_win],
          labels=('Win','Lose'),
         autopct='%1.1f%%')
axe1.set_title('Win firstBlood')
axe2=plt.subplot(1,2,2)
axe2.pie([first_blood_lose,1-first_blood_lose],
          labels=('Win','Lose'),
         autopct='%1.1f%%')
axe2.set_title('Lost firstBlood')

axe1=plt.subplot(1,2,1)
axe1.pie([first_tower_win,1-first_tower_win],
          labels=('Win','Lose'),
         autopct='%1.1f%%')
axe1.set_title('Win firstTower')
axe2=plt.subplot(1,2,2)
axe2.pie([first_tower_lose,1-first_tower_lose],
          labels=('Win','Lose'),
         autopct='%1.1f%%')
axe2.set_title('Lost firstTower')

axe3=plt.subplot(1,2,1)
axe3.pie([first_inhibitor_win,1-first_inhibitor_win],
          labels=('Win','Lose'),
         autopct='%1.1f%%')
axe3.set_title('Win Frist inhibitor')
axe4=plt.subplot(1,2,2)
axe4.pie([first_inhibitor_lose,1-first_inhibitor_lose],
          labels=('Win','Lose'),
         autopct='%1.1f%%')
axe4.set_title('Lost Frist inhibitor')

axe5=plt.subplot(1,2,1)
axe5.pie([first_baron_win,1-first_baron_win],
          labels=('Win','Lose'),
         autopct='%1.1f%%')
axe5.set_title('Win firstBaron')
axe6=plt.subplot(1,2,2)
axe6.pie([first_baron_lose,1-first_baron_lose],
          labels=('Win','Lose'),
         autopct='%1.1f%%')
axe6.set_title('Lost firstBaron')

axe7=plt.subplot(1,2,1)
axe7.pie([first_gragon_win,1-first_gragon_win],
          labels=('Win','Lose'),
         autopct='%1.1f%%')
axe7.set_title('Win firstGragon')
axe8=plt.subplot(1,2,2)
axe8.pie([first_gragon_lose,1-first_gragon_lose],
          labels=('Win','Lose'),
         autopct='%1.1f%%')
axe8.set_title('Lost firstGragon')

axe9=plt.subplot(1,2,1)
axe9.pie([first_riftherald_win,1-first_riftherald_win],
          labels=('Win','Lose'),
         autopct='%1.1f%%')
axe9.set_title('Win firstriftherald')
axe10=plt.subplot(1,2,2)
axe10.pie([first_riftherald_lose,1-first_riftherald_lose],
          labels=('Win','Lose'),
         autopct='%1.1f%%')
axe10.set_title('Lost firstriftherald')
'''
'''
lol_position = lol[lol['team_role'] == '1-MID'].groupby('matchid').agg({'team_role':'count'})
df_remove[df_remove['team_role'] != 1].index.values

'''

lolplay = pd.merge(lol[])
kills = df['kills'].value_counts().sort_index() / len(df)
kills.cumsum()



lolplay =  pd.DataFrame(columns = ['win','id','kills','deaths','assists','position','gold']) #创建一个空的dataframe


i = 1
while i<=10:
    if i <= 5:
        lolplay = lolplay.append(lol[['team1_win','player'+str(i)+'_championId','player'+str(i)+'_kills','player'+str(i)+'_deaths','player'+str(i)+'_assists','player'+str(i)+'_position','player'+str(i)+'_goldEarned']])
    else:
        if lol['team1_win']==1:
            lol['team1_win']=0
        else:
            lol['team1_win']=1
        lolplay = lolplay.append(lol[['team1_win','player'+str(i)+'_championId','player'+str(i)+'_kills','player'+str(i)+'_deaths','player'+str(i)+'_assists','player'+str(i)+'_position','player'+str(i)+'_goldEarned']])       
    i += 1
i = 2
lolplay = lolplay[1]
while i<=10:
    lolplay = lolplay.append(lolplay[i])
    i += 1

plt.figure(figsize = (15, 10))
sns.violinplot(x="position", y="kills", hue="_win", data=lolplay, palette='Set3', split=True, inner='quartile')
plt.title('Kills by position: win vs loss')
    i += 1
i = 2
lolplay = lolplay[1]
while i<=10:
    lolplay = lolplay.append(lolplay[i])
    i += 1

plt.figure(figsize = (15, 10))
sns.violinplot(x="position", y="kills", hue="_win", data=lolplay, palette='Set3', split=True, inner='quartile')
plt.title('Kills by position: win vs loss')




KDA=[]
for k,d,a in zip(lolplay['kills'],lolplay['deaths'],lolplay['assists']):
    if d == 0:
        kda=(k+a)/(d+1)*3
    else:
        kda=(k+a)/d*3
    KDA.append(kda)
#把KDA整合到数据集中
lol_result['KDA']=KDA
#先来看看KDA的分布怎么样
lol_result['KDA'].describe()
win_kda=lol_result[lol_result['hasWon']==1]['KDA']
lose_kda=lol_result[lol_result['hasWon']==0]['KDA']
kda_list=[win_kda,lose_kda]
 
plt.figure(figsize=(6,6))
plt.boxplot(kda_list,patch_artist=True,showfliers=False,widths=0.8)
plt.xticks(np.arange(3),('','Win','Lose'))
plt.ylabel('KDA')
plt.title('KDA distribution for win and lose teams')























'''
first_blood_win = (lol[(lol['team1_win']==1) and (lol['team1_firstBlood']=='TRUE')]['index'].count()/lol[lol['team1_firstBlood']=='TRUE']['index'].count())


'''
'''
'''

'''

'''



'''
#将role和lane合并为一个属性
if lol_rowdata['player1_role'] in ('DUO_SUPPORT', 'DUO_CARRY'):
    lol_rowdata['position'] = lol_rowdata['player1_role']
else:
    lol_rowdata['position'] = lol_rowdata['player1_lane']

print(lol_rowdata)
'''
'''
def adj_position(row):
    if row['player1_role'] in ('DUO_SUPPORT', 'DUO_CARRY'):
        continue
    else :
        row['player1_role'] = row['player1_lane']
    i += 1
'''





































'''
print(lol_rowdata)
'''




'''
#分队
df['team'] = df['player'].apply(lambda x: '1' if x <= 5 else '2')
df['team_role'] = df['team'] + '-' + df['adjposition']
'''

'''
list = lol_rowdata.values.tolist()

print(list)
'''