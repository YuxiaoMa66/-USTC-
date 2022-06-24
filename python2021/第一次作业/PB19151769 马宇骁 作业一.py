def febo(n):
    if ((n==1) | (n==2)):
        return (int(1))
    else:
        return (febo(n-1)+febo(n-2))

l = []
for i in range(1,30):
    m = int(febo(int(i)))
    l.append(m)
    print(i)
print(l)

 
def root(x, level = 2):
    x1 = x
    x2 = x/2
    n = level
    while (abs(x2-x1)>1e-15):
        x1 = x2
        x2 = x1 - (x1**n - x)/(n*x1**(n-1))
    return (x1)
#n = int(input()) 
#x = float((input())) 

def prime(n):
    tn = []
    tn.append(2)
    i = 3
    while(1):
        k = 1
        for m in tn:
            if i%m==0:
                k=0
                break
        if k==1:
            tn.append(i)
        i = i+1
        if len(tn) == int(n):
            return tn[-1]
            break


        
def seek_unique(t):
    one = []
    for i in t:
        if t.count(i)==1:
            one.append(i)
    return one
                 
def find_names(s, n):
    f = n[0]
    l = n[-1]
    out = []
    for m in s:
        if ((m.startswith(f)) & m.endswith(l)):
            out.append(m)
    return out

'''
s=['awe','eucb','fra','llll']
n='evdfsgb'
print(find_names(s, n))
'''