def duplicated(L):
    cnt = {}
    for v in L:
        if v in cnt:
            cnt[v] += 1
        else:
            cnt[v] = 1
    n = []
    for m in cnt:
        if cnt[m]>1:
            n.append(m)
    return n

def counting(s):
    s1=[]
    for i in s:
        if i.isupper():
            s1.append(i)
    cnt = {}
    for v in s1:
        if v in cnt:
            cnt[v] += 1
        else:
            cnt[v] = 1
    return cnt

def continued_fraction(*x):
    lgt = len(x)-2
    cf = x[-1]
    while lgt >= 0:
        if lgt%2 == 0:
            cf = x[lgt]/cf
        else:
            cf = x[lgt]+cf
        lgt -= 1
    return cf
    

    
def bi_gram(s):
    l1 = list(s)
    l3 = []
    for i in range(len(l1)-1):
        l3.append(l1[i]+l1[i+1])
    places = {}
    for i,v in enumerate(l3):
        if v in places:
            places[v].append(i)
        else:
            places[v] = [i]
    return places
    
def sort_by_age(s):
    L = list(s.items())
    L.sort(key=lambda x:x[1],reverse=True)
    lis = []
    for m in L:
        lis.append(m[0])
    return lis
