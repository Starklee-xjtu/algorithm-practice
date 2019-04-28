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

def split(li):
    li.sort(key=takefirst)
    li_temp = [[]]
    num0 = math.floor(len(li) / 5)
    for i in range(num0):
        li_temp[i] = li[i:i + 5]

    if len(li) - 5 * num0 != 0:
        li_temp.append(li[5 * num0:len(lists)])
    return li_temp

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
    hull0=[]

    for i in range(len(li)):
        for j in range(i+1,len(li)):
            p1=li[i]
            p2=li[j]
            pos = 0
            neg = 0
            for k in range(len(li)):
                p3=li[k]
                if (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p3[0] - p1[0]) * (p2[1] - p1[1])>=0:
                    pos = pos+1
                if (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p3[0] - p1[0]) * (p2[1] - p1[1])<=0:
                    neg = neg+1
            if pos == len(li) or neg == len(li):
                hull0.append(p1)
                hull0.append(p2)

    for i in hull0:
        if i not in hull:
            hull.append(i)

    li.sort(key=takefirst)
    return hull



lists = [(2, 2), (3, 3), (5, 2), (4, 0), (3, 1),(-1, 0), (0, 1), (1, 0), (0, -2)];

split_li=split(lists)

hull1=brutehull(split_li[0])


print('finished')