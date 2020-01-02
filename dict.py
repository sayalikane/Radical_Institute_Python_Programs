import sys;

dict1={"Name":"sayali", "Age":20,"Salary":20000}
#dict2={"Name":"Nikhil", "Age":20,"Salary":25000}

#for i in dict1.keys():
#    if dict1[i]!=dict2[i] :
#        print(dict1[i],dict2[i])

dict3=[dict1[i] for i in dict1.keys()]
dict4=[i for i in dict1.values()]
print(dict3,dict4)

