from functools import reduce
def find_common(*s):
    s0 = set(reduce(lambda x,y: x.intersection(y),s))
    return s0

class my_list:
    def __init__(self, *data):  self.content = data
    def __len__(self):  return len(self.content)  # 重写了len函数
    def __add__(self, b):  # 重写了加法
        if len(b)<len(self):
            for m in range(len(b), len(self)):
                b.content[m] = 0
        elif len(b)>len(self):
            for m in range(len(self), len(b)):
                b.content[m] = 0
        k = len(b) if len(b) > len(self) else len(self)
        content = [self.content[i] + b.content[i] for i in range(k)]
        return my_list(*content)  # note *content means multiple variables instead of one
 
class my_dict:
    def __init__(self, **data):
        self.data = data
    def __add__(self, b):
        c = {}
        keys = set(self.data.keys()) | set(b.data.keys())
        for i in keys:
            c[i] = self.data.get(i, 0) + b.data.get(i, 0)
        return c
    
def sum_of_all( *p, block = 1, inverse = False):
    s = 0 
    if (block == 1) and (inverse == False):
        for k in p:
            s += k
        return s
    elif (block == 2) and (inverse == False):
        p = list(p)
        import math
        for i in range(int(math.floor(len(p)/2))):
            s = s+p[2*i]*p[2*i+1]
        if (len(p)/2)%1 == 0:
            s = s
        else:
            s = s+p[-1]
        return s
    elif (block == 1) and (inverse == True):
        for k in p:
            s += 1/k
        return s
    elif (block == 2) and (inverse == True):
        p = list(p)
        import math
        for i in range(int(math.floor(len(p)/2))):
            s = s+1/(p[2*i]*p[2*i+1])
        if (len(p)/2)%1 == 0:
            s = s
        else:
            s = s+1/p[-1]
        return s

class Shape:
    cnt = 0
    def __init__(self, name):
        self.name = name
        self.area = 1
    def get_area(self):
        return self.area
    def set_area(self,area):
        self.area = area
        
class Circle(Shape):
    def __init__(self, d = 2):
        import math
        Shape.__init__(self, name = 'circle')
        self.diameter = d
        self.area = math.pi / 4 * d ** 2
class Square(Shape):
    def __init__(self, s = 2):
        Shape.__init__(self, name = 'square')
        self.side = s
        self.area = s ** 2
        