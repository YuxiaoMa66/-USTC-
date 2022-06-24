import re

'''
# findall
lst = re.findall(r'\d+', '我的电话号码是：10010，他的电话是：10086')
print(lst)
'''

'''
# finditer 匹配字符串中所有内容，返回迭代器拿到内容需要.group
it = re.finditer(r'\d+', '我的电话号码是：10010，他的电话是：10086')
print(it)
for i in it:
    print(i)
    print(i.group())
'''
'''
# search,找到一个结果就返回
s = re.search(r'\d+', '我的电话号码是：10010，他的电话是：10086')
print(s.group())

# match,从头匹配,相当于在search前加^(^\d)
s = re.search(r'\d+', '我的电话号码是：10010，他的电话是：10086')
print(s.group())
'''

'''
# 预加载正则表达式
obj = re.compile(r'\d+')

ret = obj.finditer('我的电话号码是：10010，他的电话是：10086')
for it in ret:
    print(it.group())
'''

# 正则表达式的应用
s = """
<div class='jay'><span id='2'>周杰伦</span></div>
<div class='jj'><span id='2'>周杰</span></div>
<div class='njdnu'><span id='2'>不对吧</span></div>
<div class='nduvi'><span id='2'>女诗人</span></div>
"""
obj = re.compile(r"<div class='.*?'><span id='\d+'>(?P<suibian>.*?)</span></div>", re.S)  # 让.能匹配换行符

result = obj.finditer(s)
for it in result:
    print(it.group('suibian'))