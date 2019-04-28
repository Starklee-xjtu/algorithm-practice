# Input : First Polygon  : {(2, 2), (3, 3), (5, 2), (4, 0), (3, 1)}
#         Second Polygon : {(-1, 0), (0, 1), (1, 0), (0, -2)}.
# Output : Upper Tangent - line joining (0,1) and (3,3)
#          Lower Tangent - line joining (0,-2) and (4,0)
import math

def sign_ret(num):
    if(num==0):
        return 0
    if(num > 0):
        return 1
    else:
        return -1

def takefirst(elem):
    return elem[0]

def find_upper_tangent(a,b):
    return(p1,p2)

def find_lower_tangent(a,b):
    return(p1,p2)

def find_convex(s0):
    return(s1)

def brutehull(li):
    hull=[]
    pos=0
    neg=0
    for i in range(len(li)):
        for j in range(i+1,len(li)):
            p1=li[i]
            p2=li[j]

            for k in range(len(li)):
                p3=li[k]
                if (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p3[0] - p1[0]) * (p2[1] - p1[1])>=0:
                    pos = pos+1
                if (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p3[0] - p1[0]) * (p2[1] - p1[1])<=0:
                    neg = neg+1
            if pos == len(li) or neg == len(li):
                hull.append(p1)

    return hull

lists = [[2, 2], [3, 3], [5, 2], [4, 0], [3, 1], [-1, 0], [0, 1], [1, 0], [0, -2]]
lists.sort(key=takefirst)
lists_temp=[[]]
num0= math.floor(len(lists)/5)
for i in range (num0):
    lists_temp[i]=lists[i:i+5]

if len(lists) - 5*num0 != 0:
    lists_temp.append(lists[5*num0:len(lists)])

hull1=brutehull(lists)


print('finished')