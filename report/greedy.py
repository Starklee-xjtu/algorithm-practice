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
    for j in range(len(temp)):
        if temp[j][1]<j+1:
            fin.pop() #pop 一定要带括号
            break

fin.sort(key=takesecond)
print (fin)




