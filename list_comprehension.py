list=[1,3,4,5,7,8,9,4,3,1,10,11]
#sum=0
#list2=[i+2 for i in list]

#list2=[i*i for i in list if i%2!=0 else i*2]

#list2=[i*i if i%2!=0 else i*2 for i in list]

#list2=[i*i if i%2!=0 and i>9 else i*2 for i in list]
list2=[i*2 if i>=2 and i<5 else i*3 if i>=5 and i<9 else i*4 for i in list]
print(list2)


