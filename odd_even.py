import sys;

list1=[1,2,3,4,5,6,7]
e=0
o=0

for i in list1:
    if i%2==0 :
        print("Even nos are: ",i)
        e=e+1
    else:
        print("Odd nos are:",i)
        o=o+1

print("Even nos count=",e)
print("Odd nos count=",o)

