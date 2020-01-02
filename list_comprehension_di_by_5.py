import sys;

#list=[1,2,5,20,40,100,7]

#list1=[i for i in list if i%5==0]
#print(list1)

str1="The boy was eating fish and the girl was sleeping"

#l=[i for ch in str1.split() for i in len(ch) if ch!='the' or ch!='THE']

l=[len(i) for i in str1.split() if i.lower()!='the']
print(l)

#s=str1.split()
#print(s)
#t="the"
#the1=t.casefold()

#for i in s:
    #if i!=t :
        #print(len(i))



