import sys;

d={1:10, 2:13, 3 :7, 4: 5, 5:15, 6:14}
#print(d[1])
max1=0
max2=0
for i in d.keys():
    if d[i]>max1 :
        max1=d[i]
        #print(max1)
    if d[i]>max2 and d[i]<max1:
        max2=d[i]
print(max2)


