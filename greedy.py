import numpy as np
import math



def takefirst(elem):
    return elem[0]
def takesecond(elem):
    return elem[1]



d = [(70,4), (60,2), (50,4), (40,3), (30,1), (20,4), (10,6)] #第一项为奖励，第二项为截止时间
fin =[] #最终选择
#d.sort(key=takefirst)
for i in range(len(d)):

    if d[i][1]>len(fin):
        fin.append(d[i])

fin.sort(key=takesecond)

for i in range(len(fin)):
    if fin[i][0]>len(fin):
        fin.append(d[i])


print (fin)




