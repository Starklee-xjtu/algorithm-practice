import numpy as np
import math
import copy
def takefirst(elem):
    return elem[0]
def takesecond(elem):
    return elem[1]
d = [(70,4), (60,2), (50,4), (40,3), (30,1), (20,4), (10,6)] #第一项为奖励，第二项为截止时间

fin=[]
d.sort(key=takefirst,reverse=True)
for i in range(len(d)):
    fin.append(d[i])
    temp=copy.deepcopy(fin)
    temp.sort(key=takesecond)
    if temp[len(temp)-1][1]<len(temp):
        print(fin.pop()) #pop 一定要带括号
fin.sort(key=takesecond)
print (fin)




