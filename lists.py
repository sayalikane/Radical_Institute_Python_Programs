import sys;
import random;

s='abcdefg@#$%^123456'
list=[1,2,3,4,5]
list1=[2,3,2,3,40]
list2=[]
#print(list)
#print(list2)
#for i in list:
#    for j in list1:
#        list2.append(i-j)
list2=[i+j for i,j in zip(list,list1)]
print(list2)

#print(random.sample(s,5))
x="".join(random.sample(s,8))
print(x)



