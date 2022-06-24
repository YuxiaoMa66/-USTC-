
#coding=utf-8

import os
import random

def Rnd(r):
    return int(random.random()*r)
    pass

bai=0xFFFFFF		#白色
hei=0x000000		#黑色
shui=0x555555		#深灰色
qhui=0xAAAAAA		#浅灰色

def color(R,G,B):
    pass


color(hei,bai,bai)
key_0=48
key_1=49
key_2=50
key_3=51
key_4=52
key_5=53
key_6=54
key_7=55
key_8=56
key_9=57
key_a=65
key_b=66
key_c=67
key_d=68
key_e=69
key_f=70
key_g=71
key_h=72
key_i=73
key_j=74


def Cls():
    os.system("cls")


def tk():
    Cls()
    print("本游戏由冰封飞飞制作")
    print("谢谢使用")
    print("初学乍练,有不好的地方")
    print("希望大家提出建议")
    p()    
    exit() ##End 
    ##End Function 


def js():
    Cls()
    print( "经过一番恶战")
    print( "邪恶的斯巴达克终于")
    print( "倒下了,你逃离暗黑学校")
    print( "回到地球")
    p()
    tk()
    ##End Function    

font_24hei=""
font_16song=""
def font(a):
    pass

def p():
    input("")
    pass

def getkey():
    return ord((input()+" ")[0])

lv=0
Exp=0
expmax=100
gj=100
fy=50
hp=300
hpmax=300
mpmax=100
mp=100
y1=5
y2=0
y3=0
y4=5
y5=0
y6=0
y7=5
y8=0
y9=0
y10=0
y11=0
y12=0
y13=0
y14=0
y15=0
fp=5
mg1=0
mg2=0
mg3=0
mg4=0
money=1000
Cls()
print( "校园历险记")
p()
font("font_24hei")
print( "    Ⅱ      " )
print( "----------ver1.0")
p()
Cls()
font("font_16song")
print( "你在宇宙中飞行--")
print( "轰--轰--轰" )
print( "飞机失事你坠入了暗黑学校")
p()
print( "这里充满凶险又不乏")
print( "和谐与安乐")
p()
Cls()

print( "但-那终究不是你的家园")
print( "逃离吧----")
print( "努力吧----")
p()
Cls()

font("font_24song")
print( "出")
print( "发")
print( "喽")
print( "！")
p()
GoTo=1
#
'----------------主程序------------'
while True:
    if GoTo==1: 
        Cls()
        font("font_12song")
        print( "1  2  3  4  5  6 ")
        print( "状 对 买 打 修 升")
        print( "态 话 卖 工 炼 级")
        print( "7  8  9  0  E ")
        print( "打 赌 猜 储 退")
        print( "怪 博 数 存 出")
        key=getkey()
        if key==key_1 :
            GoTo=101
            continue
        elif key==key_2 : 
            GoTo=102 
            continue
        elif key==key_3 : 
            GoTo=103 
            continue
        elif key==key_4 : 
            GoTo=104 
            continue
        elif key==key_5 : 
            GoTo=105 
            continue
        elif key==key_6 : 
            GoTo=106 
            continue
        elif key==key_7 : 
            GoTo=107 
            continue
        elif key==key_8 : 
            GoTo=108 
            continue
        elif key==key_9 : 
            GoTo=109 
            continue
        elif key==key_0 : 
            GoTo=110 
            continue
        elif key==key_e :
            tk()
        else: 
            GoTo=1 
            continue
        #End If
    '----------状态---------'
    if GoTo==101:
        Cls()
        print( "等级",lv )
        print( "经验",Exp,"/",expmax)
        print( "体力",hp,"/",hpmax)
        print( "魔法",mp,"/",mpmax)
        print( "攻击力",gj)
        print( "防御力",fy)
        print( "金钱",money)
        print( "-----0返回---------")
        key=getkey()
        if key==key_0 : 
            GoTo=1 
            continue
        else: 
            GoTo=101 
            continue 
        #End If
    '---------------对话----------'
    if GoTo==102:
        Cls()
        print( "1游戏介绍人")
        print( "2挑战人")
        print( "0--返回---")
        key=getkey()
        if key==key_1 :
            GoTo=1021
            continue
        elif key==key_2 :
            GoTo=1022
            continue
        elif key==key_0 :
            GoTo=1
            continue
        else: 
            GoTo=102 
            continue
        #End If 
    if GoTo==1021:
        Cls()
        print( "你想做什么？0--返回")
        print( "1买卖     2打工")
        print( "3修炼     4升级")
        print( "5打怪     6游戏")
        key=getkey()
        if key==key_1 : 
            GoTo=10211 
            continue
        elif key==key_2 : 
            GoTo=10212 
            continue
        elif key==key_3 :
            GoTo=10213
            continue
        elif key==key_4 :
            GoTo=10214
            continue
        elif key==key_5 :
            GoTo=10215
            continue
        elif key==key_6 :  
            GoTo=10216  
            continue
        elif key==key_0 :
            GoTo=102
            continue
        else: 
            GoTo=1021 
            continue
        #End If 
    if GoTo==10211:
        Cls()
        print( "你可以在商店买卖")
        print( "血药（大,中,小）")
        print( "法药（大,中,小）")
        print( "暗器（飞镖,飞刀,飞剑）")
        print( "等----")
        print( "并且可以买到修炼中使用的属性点")
        p()
        GoTo=1021
        continue
    if GoTo==10212:
        Cls()
        print( "打工是利用你的经验值")
        print( "来换取金钱的交易")
        print( "随着等级的提升换取量越来越大")
        p()
        GoTo=1021
        continue
    if GoTo==10213:
        Cls()
        print( "修炼可以提升你的功击")
        print( "防御或魔法攻击")
        print( "修炼攻击防御一次消耗一个")
        print( "属性点,修炼魔法根据魔法等级")
        print( "递增")
        p()
        GoTo=1021
        continue
    if GoTo==10214:
        Cls()
        print( "这个游戏由于修炼打工")
        print( "等,会用到大量的经验值")
        print( "所以当经验值超过上限")
        print( "不会自动升级,需要手")
        print( "动升级")
        p()
        GoTo=1021
        continue
    if GoTo==10215:
        Cls()
        print( "练级场地有能力大小不同的")
        print( "各种怪物,可根据你的能力")
        print( "进行练级")
        print( "战斗胜利后会获得经验值")
        print( "金钱以及随即获得属性点")
        print( "战斗失败,游戏结束")
        print( "战斗中可以使用血药法药")
        print( "以及暗器")
        p()
        GoTo=1021
        continue
    if GoTo==10216:
        Cls()
        print( "赌博为压大小")
        print( "2个骰子点数和大于7为大,小于")
        print( "7为小,你可压大或小。但点数等于")
        print( "7庄家通吃")
        print( "胜利3倍赢钱")
        print( "输了押金全部没收")
        p()
        Cls()
        print( "猜数字为无本金游戏")
        print( "从0--9选一个数")
        print( "如果大了或小了都会提示")
        print( "有3次机会")
        print( "猜中会得到相应金钱")
        print( "随着级别增加而增加")
        p()
        GoTo=1021
        continue
    if GoTo==1022:
        Cls()
        print( "你确定要挑战boss吗")
        print( "1是       2否   ")
        key=getkey()
        if key==key_1 :
            GoTo=10222
            continue
        elif key==key_2 :
            GoTo=102
            continue 
        else: 
            GoTo=1022 
            continue 
        #End If
    
    '-----------买卖-------------'
    if GoTo==103:

        Cls()
        print( "你要买还是卖？")
        print( "1 买")
        print( "2 卖")
        print( "0---返回")
        key=getkey()
        if key==key_1 :
            GoTo=1031
            continue
        elif key==key_2 :
            GoTo=1032
            continue
        elif key==key_0 :
            GoTo=1
            continue
        else: 
            GoTo=103 
            continue
        #End If
    if GoTo==1031:
        Cls()
        print( "B--下页 C--返回")
        print( "1小血药--100",y1)
        print( "2中血药--250",y2)
        print( "3大血药--500",y3)
        print( "4小法药--150",y4)
        print( "5中法药--300",y5)
        print( "6大法药--700",y6)
        print( "7飞镖----500",y7)
        print( "8飞刀----800",y8)
        print( "9飞剑---1200",y9)
        key=getkey()
        if key==key_1 and money>99 :
            y1=y1+1
            money=money-100
        elif key==key_2 and money>249 :
            y2=y2+1
            money=money-250
        elif key==key_3 and money>499 :
            y3=y3+1
            money=money-500
        elif key==key_4 and money>149 :
            y4=y4+1
            money=money-150
        elif key==key_5 and money>299 :
            y5=y5+1 
            money=money-300
        elif key==key_6 and money>699 :
            y6=y6+1 
            money=money-700
        elif key==key_7 and money>499 :
            y7=y7+1
            money=money-500
        elif key==key_8 and money>799 :
            y8=y8+1 
            money=money-800
        elif key==key_9 and money>1199 :
            y9=y9+1
            money=money-1200
        elif key==key_b : 
            GoTo=10312 
            continue
        elif key==key_c : 
            GoTo=103 
            continue
        else: 
            GoTo=1031 
            continue
        #End If 
        GoTo=1031 
        continue
    if GoTo==10312:

        Cls()
        print( "A---上页  C---返回")
        print( "1毒箭------5000",y10)
        print( "2勾魂箭---10000",y11)
        print( "3万箭穿心-25000",y12)
        print( "4属性点---20000")
        key=getkey()
        if key==key_1 and money>4999 :
            y10=y10+1 
            money=money-5000
        elif key==key_2 and money>9999 :
            y11=y11+1 
            money=money-10000
        elif key==key_3 and money>24999 :
            y12=y12+1 
            money=money-25000
        elif key==key_4 and money>19999 :
            fp=fp+1 
            money=money-20000
        elif key==key_a :
            GoTo=1021
            continue
        elif key==key_c :
            GoTo=103
            continue
        else: 
            GoTo=10312 
            continue
        #End If 
        GoTo=10312 
        continue
    if GoTo==1032:

        Cls()
        print( "B---下页  C---返回")
        print( "1小血药---50",y1)
        print( "2中血药--125",y2)
        print( "3大血药--250",y3)
        print( "4小法药---75",y4)
        print( "5中法药--150",y5)
        print( "6大法药--350",y6)
        print( "7飞镖----250",y7)
        print( "8飞刀----400",y8)
        print( "9飞剑----600",y9)
        key=getkey()
        if key==key_1 and y1>0 :
            money=money+50 
            y1=y1-1
        elif key==key_2 and y2>0 :
            money=money+125 
            y2=y2-1
        elif key==key_3 and y3>0 :
            money=money+250 
            y3=y3-1
        elif key==key_4 and y4>0 :
            money=money+75 
            y4=y4-1
        elif key==key_5 and y5>0 :
            money=money+150 
            y5=y5-1
        elif key==key_6 and y6>0 :
            money=money+350 
            y6=y6-1
        elif key==key_7 and y7>0 :
            money=money+250
            y7=y7-1
        elif key==key_8 and y8>0 :
            money=money+400 
            y8=y8-1
        elif key==key_9 and y9>0 :
            money=money+600 
            y9=y9-1
        elif key==key_b :
            GoTo=10322
            continue
        elif key==key_c :
            GoTo=103
            continue
        else: 
            GoTo=1032 
            continue
        #End If
        GoTo=1032
        continue
    if GoTo==10322:
        Cls()
        print( "A---上页  C---返回")
        print( "1毒箭------2500",y10)
        print( "2勾魂箭----5000",y11)
        print( "3万箭穿心-12500",y12)

        key=getkey()
        if key==key_1 and y10>0 :
            money=money+2500 
            y10=y10-1
        elif key==key_2 and y11>0 :
            money=money+5000
            y11=y11-1	
        elif key==key_3 and y12>0 :
            money=money+12500
            y12=y12-1
        elif key==key_a  :
            GoTo=1032
            continue
        elif key==key_c :
            GoTo=103
            continue
        else: 
            GoTo=10322 
            continue
        #End If
        GoTo=10322
        continue
    '---------------打工------------'
    if GoTo==104:
        Cls()
        print( "你要做什么？ A--退出"	)
        print( "1做包子 0级以上")
        print( "2栽树   5级以上")
        print( "3运石块 10级以上")
        print( "4做家具 20级以上")
        print( "5盖房   30级以上")
        key=getkey()
        if key==key_1 and Exp>249 :
            money=money+300
            Exp=Exp-250
            print( "你得到了300块钱")
            p()
        elif key==key_2 and lv>4 and Exp>499 :
            money=money+900
            Exp=Exp-500
            print( "你得到了900元钱")
            p()
        elif key==key_3 and lv>9 and Exp>1499 :
            money=money+5000
            Exp=Exp-1500
            print( "你得到了5000元钱")
            p()
        elif key==key_4 and lv>19 and Exp>4999 :
            money=money+30000
            Exp=Exp-5000
            print( "你得到了30000元钱")
            p()
        elif key==key_5 and lv>29 and Exp>6999 :
            money=money+75000
            Exp=Exp-7000
            print( "你得到了75000元钱")
            p()
        elif key==key_a :
            GoTo=1
            continue

        #End If
        GoTo=104
        continue
        '------------修炼-----------'
    if GoTo==105: 
        Cls()
        print( "你要修炼什么？A--退出")
        print( "1攻击")
        print( "2防御")
        print( "------魔法-------")
        print( "3飞沙走石 5级以上---魔法等级",mg1)
        print( "4水漫金山 10级以上--魔法等级",mg2)
        print( "5天诛地灭 15级以上--魔法等级",mg3)
        print( "6乾坤烈焰 30级以上--魔法等级",mg4)
        print( "属性点",fp,"个")
        key=getkey()
        if key==key_1 and fp>0 :
            gj=gj+10
            fp=fp-1
        elif key==key_2 and fp>0 :
            fy=fy+8
            fp=fp-1
        elif key==key_3 and fp>0 and lv>4 :
            mg1=mg1+1
            fp=fp-1
        elif key==key_4 and fp>1 and lv>9 :
            mg2=mg2+1
            fp=fp-2
        elif key==key_5 and fp>2 and lv>14 :
            mg3=mg3+1
            fp=fp-3
        elif key==key_6 and fp>mg4 and lv>29 :
            mg4=mg4+1
            fp=fp-(mg4+1)
        elif key==key_a :
            GoTo=1
            continue
        else: 
            GoTo=105 
            continue
        #End If 
        GoTo=105 
        continue
        '-----------------升级-----------------'
    if GoTo==106:
        Cls()
        print( "你确定你要升级吗？")
        print( "你的等级",lv)
        print( "经验值",Exp,"/",expmax)
        print( "1我确定要升级")
        print( "2我再考虑一下")
        key=getkey()
        if key==key_1 and Exp>expmax-1 :
            lv=lv+1 
            Exp=Exp-expmax
            expmax=expmax+lv*lv*20
            hpmax=hpmax+lv*20
            hp=hpmax
            mpmax=mpmax+lv*10
            mp=mpmax
            gj=gj+lv*5
            fy=fy+lv*5
            print( "你升级了！")
            p()
        elif key==key_2 :
            GoTo=1
            continue
        else: 
            GoTo=106 
            continue
        #End If 
        GoTo=106 
        continue
        '----------------打怪---------------'
    if GoTo==107:
        Cls()
        print( "---升级场---0退出")
        print( "1 0---- 5练级区")
        print( "2 5----10练级区")
        print( "3 10---20练级区")
        print( "4 20---30练级区")
        print( "5 头目级怪练级区")
        key=getkey()
        if key==key_1 : 
            GoTo=1071 
            continue
        elif key==key_2 :
            GoTo=1072
            continue
        elif key==key_3 :
            GoTo=1073
            continue
        elif key==key_4 : 
            GoTo=1074 
            continue
        elif key==key_5 :
            GoTo=1075
            continue
        elif key==key_0 :
            GoTo=1
            continue
        else: 
            GoTo=107 
            continue
        #End If 
    if GoTo==1071:
        Cls()
        print( "0---5级练级区")
        print( "1 妖魔")
        print( "2 妖魔斗士")
        print( "3 狼人")
        print( "4 巨蚁")
        print( "0---返回---")
        key=getkey()
        if key==key_1 : 
            GoTo=10711 
            continue
        elif key==key_2 :
            GoTo=10712
            continue 
        elif key==key_3 :
            GoTo=10713
            continue
        elif key==key_4 :
            GoTo=10714
            continue
        elif key==key_0 :
            GoTo=107
            continue
        else: 
            GoTo=1071 
            continue
        #End If 
    if GoTo==1072:
        Cls()
        print( "5---10级练级场")
        print( "1 骷髅")
        print( "2 骷髅斗士")
        print( "3 侏儒")
        print( "4 侏儒斗士")
        print( "0--返回")
        key=getkey()
        if key==key_1 :
            GoTo=10730
            continue
        elif key==key_2 :
            GoTo=10715
            continue
        elif key==key_3 :
            GoTo=10716
            continue
        elif key==key_4 :
            GoTo=10717
            continue
        elif key==key_0 :
            GoTo=107
            continue
        else: 
            GoTo=1072 
            continue
    if GoTo==1073:
        Cls()
        print( "10---20练级区")
        print( "1 夏洛克")
        print( "2 变形虫")
        print( "3 魅影")
        print( "4 雪怪")
        print( "0-返回")
        key=getkey()
        if key==key_1  :
            GoTo=10718
            continue
        elif key==key_2 :
            GoTo=10719
            continue
        elif key==key_3 : 
            GoTo=10720 
            continue
        elif key==key_4 :
            GoTo=10721
            continue
        elif key==key_0 : 
            GoTo=107 
            continue
        else: 
            GoTo=1073 
            continue
        #End If 
    if GoTo==1074:
        Cls()
        print( "20---30级练级场")
        print( "1 毒蝎")
        print( "2 亚利安")
        print( "3 邪恶蜥蜴")
        print( "4 死神")
        print( "0---返回")
        key=getkey()
        if key==key_1 :
            GoTo=10722
            continue
        elif key==key_2 : 
            GoTo=10723 
            continue
        elif key==key_3 :
            GoTo=10724
            continue
        elif key==key_4 :
            GoTo=10725
            continue
        elif key==key_0 : 
            GoTo=107 
            continue 
        else: 
            GoTo=1074 
            continue
        #End If 
    if GoTo==1075:
        print( "头目级怪物练级区")
        print( "1 死亡骑士")
        print( "2 巨蚁女皇")
        print( "3 冰之女皇")
        print( "4 不死鸟")
        print( "0---返回")
        key=getkey()
        if key==key_1 :
            GoTo=10726
            continue
        elif key==key_2 :
            GoTo=10727
            continue
        elif key==key_3 :
            GoTo=10728
            continue
        elif key==key_4 :
            GoTo=10729
            continue
        elif key==key_0 :
            GoTo=107
            continue
        else: 
            GoTo=1075 
            continue
        #End If 
    if GoTo==10711:
        ds_="妖魔"
        hpd=50
        gjd=20
        fyd=20
        mond=100
        expd=50
        sj=10
        Kill=0
        GoTo=1076
        continue
    if GoTo==10712:
        ds_="妖魔斗士"
        hpd=80
        gjd=30
        fyd=25
        mond=125
        expd=80
        Kill=0
        sj=10
        GoTo=1076
        continue
    if GoTo==10713:
        ds_="狼人"
        hpd=100
        gjd=50
        Kill=0
        fyd=40
        mond=200+Rnd(10)
        expd=100
        sj=10
        GoTo=1076
        continue
    if GoTo==10714:
        ds_="巨蚁"
        hpd=120
        Kill=0
        gjd=60
        fyd=50
        mond=200+Rnd(20)
        expd=120
        sj=10
        GoTo=1076
        continue
    if GoTo==10730:
        ds_="骷髅"
        hpd=200
        gjd=80
        Kill=0
        fyd=50
        mond=200+Rnd(50)
        expd=150
        sj=5
        GoTo=1076
        continue
    if GoTo==10715:
        ds_="骷髅斗士"
        hpd=220
        gjd=100
        fyd=100
        Kill=0
        mond=250+Rnd(10)
        expd=180
        sj=5
        GoTo=1076
        continue
    if GoTo==10716:
        ds_="侏儒"
        hpd=250
        gjd=120
        fyd=100
        Kill=0
        mond=300
        expd=200
        sj=5
        GoTo=1076
        continue
    if GoTo==10717:
        ds_="侏儒斗士"
        hpd=280
        gjd=130
        fyd=110
        Kill=0
        mond=300+Rnd(10)
        expd=220
        sj=5
        GoTo=1076
        continue
    if GoTo==10718:
        ds_="夏洛克"
        hpd=300
        Kill=0
        gjd=150
        fyd=120
        mond=350+Rnd(50)
        expd=300
        sj=4
        GoTo=1076
        continue
    if GoTo==10719:
        ds_="变形虫"
        hpd=320
        gjd=160
        Kill=0
        fyd=140
        mond=350+Rnd(100)
        expd=350
        sj=5
        GoTo=1076
        continue
    if GoTo==10720:
        ds_="魅影"
        hpd=500
        gjd=200
        Kill=0
        fyd=160
        mond=500+Rnd(100)
        expd=400
        sj=5
        GoTo=1076
        continue
    if GoTo==10721:
        ds_="雪怪"
        hpd=600
        gjd=250
        Kill=0
        fyd=140
        mond=500+Rnd(10)
        expd=450
        sj=5
        GoTo=1076
        continue
    if GoTo==10722:
        ds_="毒蝎"
        hpd=800
        gjd=300
        Kill=0
        fyd=200
        mond=600+Rnd(100)
        expd=500
        sj=3
        GoTo=1076
        continue
    if GoTo==10723:
        ds_="亚利安"
        hpd=1000
        Kill=0
        gjd=350
        fyd=250
        mond=800+Rnd(100)
        expd=800
        sj=3
        GoTo=1076
        continue
    if GoTo==10724:
        ds_="邪恶蜥蜴"
        hpd=1500
        gjd=500
        Kill=0
        fyd=200
        mond=1000+Rnd(200)
        expd=1000
        sj=3
        GoTo=1076
        continue
    if GoTo==10725:
        ds_="死神"
        hpd=2000
        gjd=600
        Kill=0
        fyd=300
        mond=2000-Rnd(500)
        expd=1500
        sj=3
        GoTo=1076
        continue
    if GoTo==10726:
        ds_="死亡骑士"
        hpd=5000
        Kill=0
        gjd=1200
        fyd=500
        mond=10000-Rnd(5000)
        expd=2000
        sj=1
        GoTo=1076
        continue
    if GoTo==10727:
        ds_="巨蚁女皇"
        hpd=6000
        gjd=800
        Kill=0
        fyd=800
        mond=10000-Rnd(3000)
        expd=2500
        sj=1
        GoTo=1076
        continue
    if GoTo==10728:
        ds_="冰之女皇"
        hpd=100000
        gjd=400
        Kill=0
        fyd=100
        mond=10000-Rnd(3000)
        expd=3000
        sj=1
        GoTo=1076
        continue
    if GoTo==10729:
        ds_="不死鸟"
        hpd=8000
        gjd=1000
        Kill=0
        fyd=500
        mond=10000+Rnd(1000)
        expd=4000
        sj=1
        GoTo=1076
        continue
    if GoTo==10222:
        ds_="斯巴达克"
        hpd=50000
        gjd=2000
        fyd=1200
        mond=100000+Rnd(1000)
        expd=10000
        sj=1
        Kill=1
        
        GoTo=1076
        
        continue
        p()
    if GoTo==1076:
        Cls()
        print( ds_,"体力:",hpd)
        print( "你的体力",hp,"/",hpmax)
        print( "你的魔法",mp,"/",mpmax)
        print( " 1  2  3  4 ")
        print( "物 魔 使  逃")
        print( "理 法 用  跑")
        print( "攻 攻 物    ")
        print( "击 击 品    ")
        key=getkey()
        if key==key_1 :
            GoTo=10761
            continue
        elif key==key_2 :
            GoTo=107620
            continue 
        elif key==key_3 :
            GoTo=107630
            continue
        elif key==key_4 :
            GoTo=107640
            continue
        else: 
            GoTo=1076 
            continue
        #End If 
    if GoTo==10761:
        s1=gj-fyd/2-Rnd(fyd/2)
        d1=gjd-fy/2-Rnd(fy/2)
        a=Rnd(10)+1
        Cls()
        if s1<2 :
            hpd=hpd-a
            print( "你的攻击使",ds_,"损失",a,"点体力")
            p()
            GoTo=10762
            continue
        else:
            hpd=hpd-s1
            print( "你的攻击使",ds_,"损失",s1,"点体力")
            p()
            GoTo=10762
            continue
        #End If 
    if GoTo==10762:
        if hpd<1 :
            GoTo=10763
            continue
                
        #End If 
        if d1<2 :
            hp=hp-a
            print( ds_,"的攻击使你损失",a,"点体力"
)
            p()
        else: 
            hp=hp-d1
            print( ds_,"的攻击使你损失",d1,"点体力"
)
            p()
        #End If 
        GoTo=10764 
        continue
    if GoTo==10763:
        if Rnd(sj)==0 :
            fp=fp+1
            qn=1
        else: 
            qn=0
        #End If 
        if Kill==1 :
            GoTo=10223
            continue
        #End If 
        Cls()
        Exp=Exp+expd
        money=money+mond
        print( "战斗胜利")
        print( "你获得经验",expd)
        print( "你获得金钱",mond)
        print( "你获得潜能点",qn,"点")
        p()
        GoTo=107
        continue
    if GoTo==10764:
        if hp<1 :
            e1=(Rnd(Exp+1))/20
            Exp=Exp-e1
            m1=(Rnd(money+1))/50
            money=money-m1
            hp=hpmax
            mp=mpmax
            Cls()
            print( "战斗失败")
            print( "经验损失",e1)
            print( "金钱损失",m1)
            p()
            GoTo=1
            continue
        else: 
            GoTo=1076 
            continue
        #End If
    if GoTo==10223:
        js()
    if GoTo==107620:
        Cls()
        print( "你使用什么魔法")
        print( "1飞沙走石 20点mp")
        print( "2水漫金山 50点mp")
        print( "3天诛地灭 150点mp")
        print( "4乾坤烈焰 300点mp")
        print( "0-----返回----")
        key=getkey()
        if key==key_1 and mg1>0 and mp>19 :
            mf1=mg1*5+Rnd(200)+Rnd(gj/10)
            mp=mp-20
            hpd=hpd-mf1
            Cls()
            print( "你念咒使用飞沙走石")
            print( "满天黄沙,风起云涌")
            print( "使",ds_,"损伤",mf1,"点体力")
            p()
        elif key==key_2 and mg2>0 and mp>49 :
            mf2=mg2*7+Rnd(300)+Rnd(gj/9)
            mp=mp-50
            hpd=hpd-mf2
            Cls()
            print( "你召唤水龙冲塌房屋")
            print( "使",ds_,"损伤",mf2,"点体力")
            p()
        elif key==key_3 and mg3>0 and mp>149 :
            mf3=mg3*15+Rnd(400)+Rnd(gj/8)
            mp=mp-150
            hpd=hpd-mf3
            print( "轰--轰--轰")
            print( "3记响雷划破天空直")
            print( "劈",ds_,"的天灵盖")
            print( "使",ds_,"损失",mf3,"点体力")
            p()
        elif key==key_4 and mg4>0 and mp>299 :
            mf41=mg4*5+Rnd(100)+Rnd(gj/10)
            mf42=mg4*10+Rnd(200)+Rnd(gj/8)
            mf43=mg4*20+Rnd(300)+Rnd(gj/5)
                
            mp=mp-300
            hpd=hpd-mf41-mf42-mf43
            Cls()
            print( "你一挥袖子点起一阵三味真火")
            print( "使",ds_,"损伤",mf41,"点体力")
            p()
            Cls()
            print( "你再一挥袖子,摆起火龙阵")
            print( "使",ds_,"损伤",mf42,"点体力")
            p()
            Cls()
            print( "你用尽全力,一挥袖子")
            print( "天崩地裂,火焰四起")
            print( "使",ds_,"损伤",mf43,"点体力")
            p()
        elif key==key_0 :
            GoTo=1076
            continue 
        else: 
            GoTo=107620 
            continue
        #End If 
        GoTo=10762 
        continue
    if GoTo==107630:
        Cls()
        print( "B---下页  C---返回")
        print( "1小血药",y1)
        print( "2中血药",y2)
        print( "3大血药",y3)
        print( "4小法药",y4)
        print( "5中法药",y5)
        print( "6大法药",y6)
        print( "7飞镖  ",y7)
        print( "8飞刀  ",y8)
        print( "9飞剑  ",y9)
        key=getkey()
        if key==key_1 and y1>0 :
            hp=hp+100
            y1=y1-1
        elif key==key_2 and y2>0 :
            hp=hp+500
            y2=y2-1
        elif key==key_3 and y3>0 :
            hp=hp+1200
            y3=y3-1
        elif key==key_4 and y4>0 :
            mp=mp+100
            y4=y4-1
        elif key==key_5 and y5>0 :
            mp=mp+400
            y4=y4-1
        elif key==key_6 and y6>0 :
            mp=mp+800
            y6=y6-1
        elif key==key_7 and y7>0 :
            hpd=hpd-200
            y7=y7-1
            print( "你使用飞镖使",ds_,"损失200点体力")
            p()
        elif key==key_8 and y8>0 :
            hpd=hpd-300
            y8=y8-1
            
            print( "你使用飞刀使",ds_,"损失300点体力")
            p()
        elif key==key_9 and y9>0 :
            hpd=hpd-400
            y9=y9-1
            print( "你使用飞剑使",ds_,"损失400点体力")
            p()
        elif key==key_b  :
            GoTo=107631
            continue
        elif key==key_c :
            GoTo=1076
            continue
        else: 
            GoTo=107630 
            continue
        #End If 
        if hp>hpmax-1 :
            hp=hpmax
        #End If 
        if mp>mpmax-1 :
            mp=mpmax
        #End If 
        GoTo=10762 
        continue
    if GoTo==107631:
        Cls()
        print( "A---上页  C---返回")
        print( "1毒箭     ",y10)
        print( "2勾魂箭   ",y11)
        print( "3万箭穿心 ",y12)
        key=getkey()
        if key==key_1 and y10>0 :
            Cls()
            hpd=hpd-500
            y10=y10-1
            print( "你使用毒箭使",ds_,"损失500点体力")
            p()
        elif key==key_2 and y11>0 :
            Cls()
            aq1=Rnd(gj)+500
            hpd=hpd-aq1
            y11=y11-1
            print( "你使用勾魂箭使",ds_,"损失",aq1,"点体力")
            p()
        elif key==key_2 and y12>0 :
            Cls()
            aq2=800+Rnd(gj*2)
            hpd=hpd-aq2
            y12=y12-1
            print( "你使用万箭穿心使",ds_,"损失",aq2,"点体力")
            p()
        elif key==key_a :
            GoTo=107630
            continue
        elif key==key_c :
            GoTo=1076
            continue
        else: 
            GoTo=107631 
            continue
        #End If 
        GoTo=10762 
        continue
    if GoTo==107640: 
        Cls()
        tp=Rnd(2)
        if tp==1 :
            print( "逃跑成功")
            p()
            GoTo=1
            continue
        else: 
            print( "逃跑失败")
            p()
            GoTo=1076
            continue
        #End If 
    '-----------------赌博--------------'
    if GoTo==108:
        Cls()
        tz1=Rnd(6)+1
        tz2=Rnd(6)+1
        he=tz1+tz2
        print( "押大小来！黄大小坐庄来！")
        print( "1  大")
        print( "2  小")
        print( "3 不赌了")
        key=getkey()
        if key==key_1 :
            dx=1
            GoTo=1081
            continue
        elif key==key_2 :
            dx=2
            GoTo=1082
            continue
        elif key==key_3 :
            GoTo=1
            continue
        else: 
            GoTo=108 
            continue
        #End If 
    if GoTo==1081: 
        Cls() 
        print( "客官您压的大")
        print( "请输入您压的金额")
        je=input()
        je = int(je) if je.isnumeric() else 0
        if je >money  or je< 1 :
            print( "超出范围")
            p()
            p()
            GoTo=1081
            continue
        #End If 
        GoTo=1083 
        continue
    if GoTo==1082:
        Cls()
        print( "客官您压的小")
        print( "请输入您压的金额")
        je=input()
        if je >money  or je< 1 :
            print( "超出范围")
            p()
            p()
            GoTo=1082
            continue
        #End If 
        GoTo=1083 
        continue
    if GoTo==1083:
        if he>7 :
            dxd=1
        elif he<7 : 
            dxd=2
        else: 
            dxd=3
        #End If 
        if dx==dxd :
            money=money+2*je
            print( "恭喜你,你赢了")
            print( "你获得了",2*je,"块钱（不包含押金）")
            p()
            p()
            GoTo=108
            continue
        else: 
            money=money-je
            print( "哈哈,你输了")
            print( "你输了",je,"块钱")
            p()
            p()
            GoTo=108
            continue
        #End If
    '------------------猜数字-----------------'
    if GoTo==109:
        d=0
        szd=Rnd(10)
    if GoTo==1091:
        Cls()
        if d>=3 : 
            print( "你猜得次数到了")
            p()()
            GoTo=1
            continue
        #End If
        print( "请从0--9中选取1个数字")
        sz=input("请输入你猜得数字")
        if sz<0 or sz>9 :
            print( "超出范围")
            p()
            GoTo=1091
            continue
        #End If 
        if sz>szd :
            print( "大了")
            p()
            p()
        elif sz<szd :
            print( "小了")
            p()
            p()
        else:
            hd=lv*lv*20 
            money=money+hd
            print( "恭喜,你猜中了")
            print( "你获得了",hd,"元钱")
            p()
            p()
            GoTo=1
            continue
        #End If 
        d=d+1
        GoTo=1091
        continue
    '-------------------'
    if GoTo==110:
        Cls()
        print( "你是读取还是储存")
        print( "1储存")
        print( "2读取")
        print( "0---返回---")
        key=getkey()
        if key==key_1 :
            GoTo=1101
            continue
        elif key==key_2 :
            GoTo=1102
            continue
        elif key==key_0 :
            GoTo=1
            continue
        else: 
            GoTo=110 
            continue
        #End If 
    if GoTo==1101:
        Cls()
        print( "储存中")
        print( "1 进度1")
        print( "2 进度2")
        print( "3 进度3")
        print( "0--返回---")
        key=getkey()
        if key==key_1 :
            #OPEN "JL1.sav" FOR BINARY AS #1        
            #Put #1,lv
            #Put #1,hp
            #Put #1,hpmax
            #Put #1,mp
            #Put #1,mpmax
            #Put #1,Exp
            #Put #1,expmax
            #Put #1,gj
            #Put #1,fy
            #Put #1,money
            #Put #1,mg1
            #Put #1,mg2
            #Put #1,mg3
            #Put #1,mg4
            #Put #1,fp
            #Put #1,y1
            #Put #1,y2
            #Put #1,y3
            #Put #1,y4    
            #Put #1,y5
            #Put #1,y6
            #Put #1,y7
            #Put #1,y8
            #Put #1,y9
            #Put #1,y10
            #Put #1,y11
            #Put #1,y12
            #Put #1,y13
            #Put #1,y14
            #Put #1,y15
            #CLOSE #1    
            print( "储存成功" )
            p()         
        elif key==key_2 :
            #OPEN "JL2.sav" FOR BINARY AS #2
            #Put #2,lv
            #Put #2,hp
            #Put #2,hpmax
            #Put #2,mp
            #Put #2,mpmax
            #Put #2,Exp
            #Put #2,expmax
            #Put #2,gj
            #Put #2,fy
            #Put #2,money
            #Put #2,mg1
            #Put #2,mg2
            #Put #2,mg3
            #Put #2,mg4
            #Put #2,fp
            #Put #2,y1
            #Put #2,y2
            #Put #2,y3
            #Put #2,y4    
            #Put #2,y5
            #Put #2,y6
            #Put #2,y7
            #Put #2,y8
            #Put #2,y9
            #Put #2,y10
            #Put #2,y11
            #Put #2,y12
            #Put #2,y13
            #Put #2,y14
            #Put #2,y15
            #CLOSE #2
            print( "储存成功")
            p()
        elif key==key_3 :
            #OPEN "JL3.sav" FOR BINARY AS #3
            #Put #3,lv
            #Put #3,hp
            #Put #3,hpmax
            #Put #3,mp
            #Put #3,mpmax
            #Put #3,Exp
            #Put #3,expmax
            #Put #3,gj
            #Put #3,fy
            #Put #3,money
            #Put #3,mg1
            #Put #3,mg2
            #Put #3,mg3
            #Put #3,mg4
            #Put #3,fp
            #Put #3,y1
            #Put #3,y2
            #Put #3,y3
            #Put #3,y4    
            #Put #3,y5
            #Put #3,y6
            #Put #3,y7
            #Put #3,y8
            #Put #3,y9
            #Put #3,y10
            #Put #3,y11
            #Put #3,y12
            #Put #3,y13
            #Put #3,y14
            #Put #3,y15
            #CLOSE #3
            print( "储存成功")
            p()
        elif key==key_0 :
            GoTo=110
            continue
        else:
            GoTo=1101
            continue            
        #End If   
    if GoTo==1102:
        Cls()
        print( "读取中")
        print( "1 进度1")
        print( "2 进度2")
        print( "3 进度3")
        print( "0 返回")
        key=getkey()
        if key==key_1 :
            #OPEN "JL1.sav" FOR BINARY AS #1
            #Get#1,lv
            #Get#1,hp
            #Get#1,hpmax
            #Get#1,mp
            #Get#1,mpmax
            #Get#1,Exp
            #Get#1,expmax
            #Get#1,gj
            #Get#1,fy
            #Get#1,money
            #Get#1,mg1
            #Get#1,mg2
            #Get#1,mg3
            #Get#1,mg4
            #Get#1,fp
            #Get#1,y1
            #Get#1,y2
            #Get#1,y3
            #Get#1,y4    
            #Get#1,y5
            #Get#1,y6
            #Get#1,y7
            #Get#1,y8
            #Get#1,y9
            #Get#1,y10
            #Get#1,y11
            #Get#1,y12
            #Get#1,y13
            #Get#1,y14
            #Get#1,y15
            #CLOSE #1
            print( "读取成功")
            p()
        elif key==key_2 :
            #OPEN "JL1.sav" FOR BINARY AS #2
            #Get#2,lv
            #Get#2,hp
            #Get#2,hpmax
            #Get#2,mp
            #Get#2,mpmax
            #Get#2,Exp
            #Get#2,expmax
            #Get#2,gj
            #Get#2,fy
            #Get#2,money
            #Get#2,mg1
            #Get#2,mg2
            #Get#2,mg3
            #Get#2,mg4
            #Get#2,fp
            #Get#2,y1
            #Get#2,y2
            #Get#2,y3
            #Get#2,y4    
            #Get#2,y5
            #Get#2,y6
            #Get#2,y7
            #Get#2,y8
            #Get#2,y9
            #Get#2,y10
            #Get#2,y11
            #Get#2,y12
            #Get#2,y13
            #Get#2,y14
            #Get#2,y15
            #CLOSE #2
            print( "读取成功")
            p()

        elif key==key_3 :
            #OPEN "JL1.sav" FOR BINARY AS #3
            #Get#3,lv
            #Get#3,hp
            #Get#3,hpmax
            #Get#3,mp
            #Get#3,mpmax
            #Get#3,Exp
            #Get#3,expmax
            #Get#3,gj
            #Get#3,fy
            #Get#3,money
            #Get#3,mg1
            #Get#3,mg2
            #Get#3,mg3
            #Get#3,mg4
            #Get#3,fp
            #Get#3,y1
            #Get#3,y2
            #Get#3,y3
            #Get#3,y4    
            #Get#3,y5
            #Get#3,y6
            #Get#3,y7
            #Get#3,y8
            #Get#3,y9
            #Get#3,y10
            #Get#3,y11
            #Get#3,y12
            #Get#3,y13
            #Get#3,y14
            #Get#3,y15
            #CLOSE #3

            print( "读取成功")
            p()
            p()
        elif key==key_0 :
            GoTo=110
            continue
        else: 
            GoTo=1102 
            continue
        #End If
        GoTo=1102
        continue
                   
    GoTo=1
