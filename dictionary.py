import sys;
from collections import Counter

l=[1,2,3,4,4,5,5,7,7,8,8,8]
d={}
#for i in l:
#    l1=l.count(i)
#print(l1)

#a=Counter(l)
#print(dict(a))

for lst in l:
    if lst in d.keys():
        cnt=d[lst]
        cnt=cnt+1
        d[lst]=cnt
    else:
        d[lst]=1

print(d)