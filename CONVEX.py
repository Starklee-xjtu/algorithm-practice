# Input : First Polygon  : {(2, 2), (3, 3), (5, 2), (4, 0), (3, 1)}
#         Second Polygon : {(-1, 0), (0, 1), (1, 0), (0, -2)}.
# Output : Upper Tangent - line joining (0,1) and (3,3)
#          Lower Tangent - line joining (0,-2) and (4,0)
import math
import matplotlib.pyplot as plt

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
def takesecond(elem):
    return elem[1]

def find_upper_tangent(a0,b0):
    a=[]
    b=[]
    for i in range(len(a0)):
        if takesecond(a0[i]) >= takesecond(a0[len(a0)-1]):
            a.append(a0[i])

    for i in range(len(b0)):
        if takesecond(b0[i]) >= takesecond(b0[0]):
            b.append(b0[i])

    inc_find=0;
    # a 是左边的凸集， b 是右边的凸集
    n1 = len(a)-1
    n2 = len(a)-2

    n3 = 0
    n4 = 1

    a_cross = 1
    b_cross = 1
    p1 = a[n1]
    p2 = a[n2]
    p3 = b[n3]
    p4 = b[n4]
    while inc_find==0:
        while a_cross==1:
            p2 = a[n2]
            p_temp = a[n2-1]
            if (p_temp[0]-p3[0])*(p2[1]-p3[1])/(p2[0]-p3[0]) >= p_temp[1]-p3[1]:
                n1 = n2
                n2 = n1 - 1
                p1 = a[n1]
                p2 = a[n2]
                a_cross=0
            else:
                n2 = n2-1
            print('across=0')

        while b_cross==1:
            p4 = b[n4]
            p_temp = b[n4+1]
            if (p_temp[0]-p1[0])*(p4[1]-p1[1])/(p4[0]-p1[0]) >= p_temp[1]-p1[1]:
                n3 = n4
                n4 = n3+1
                p3 = b[n3]
                p4 = b[n4]
                p_temp = a[n2]
                b_cross = 0
                if (p_temp[0] - p3[0]) * (p2[1] - p3[1]) / (p2[0] - p3[0]) >= p_temp[1] - p3[1]:
                    inc_find = 1
                else:
                    a_cross=0
            else:
                n4=n4+1
    return(p1,p3)

def find_lower_tangent(a0,b0):
    a=[]
    b=[]
    for i in range(len(a0)):
        if takesecond(a0[i]) <= takesecond(a0[len(a0)-1]):
            a.append(a0[i])

    for i in range(len(b0)):
        if takesecond(b0[i]) <= takesecond(b0[0]):
            b.append(b0[i])

    inc_find=0;
    # a 是左边的凸集， b 是右边的凸集
    n1 = len(a)-1
    n2 = len(a)-2

    n3 = 0
    n4 = 1

    a_cross = 1
    b_cross = 1
    p1 = a[n1]
    p2 = a[n2]
    p3 = b[n3]
    p4 = b[n4]
    while inc_find==0:
        while a_cross==1:

            p2 = a[n2]
            p_temp = a[n2-1]

            if (p_temp[0]-p3[0])*(p2[1]-p3[1])/(p2[0]-p3[0])<=p_temp[1]-p3[1]:
                n1 = n2
                n2 = n1 - 1
                p1 = a[n1]
                p2 = a[n2]
                a_cross=0
            else:
                n2=n2-1
            print('across=0')
        while b_cross==1:
            p4 = b[n4]
            p_temp = b[n4+1]
            if (p_temp[0]-p1[0])*(p4[1]-p1[1])/(p4[0]-p1[0])<=p_temp[1]-p1[1]:
                n3 = n4
                n4 = n3+1
                p3 = b[n3]
                p4 = b[n4]
                p_temp = a[n2]
                b_cross = 0
                if (p_temp[0] - p3[0]) * (p2[1] - p3[1]) / (p2[0] - p3[0]) <= p_temp[1] - p3[1]:
                    inc_find = 1
                else:
                    a_cross=0
            else:
                n4 = n4+1

    return(p1,p3)

def merge_convex(a0,b0):
    pu = find_upper_tangent(a0,b0)
    pl = find_lower_tangent(a0,b0)
    convex0 =[]
    for i in range(len(a0)):
        if (takefirst(a0[i]) <= takefirst(pu[0]) and takesecond(a0[i]) >= takesecond(a0[0]) ) or (takefirst(a0[i]) <= takefirst(pl[0]) and takesecond(a0[i]) <= takesecond(a0[0]) )  :
            convex0.append(a0[i])
    for i in range(len(b0)):
        if (takefirst(b0[i]) >= takefirst(pu[1]) and takesecond(b0[i]) >= takesecond(b0[0]) ) or (takefirst(b0[i]) >= takefirst(pl[1]) and takesecond(b0[i]) <= takesecond(b0[0]) )  :
            convex0.append(b0[i])
    return(convex0)

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



lists = [(2, 2), (3, 3), (5, 2), (4, 0), (3, 1),(-1, 0), (0, 1), (1, 0), (0, -2)]

split_li=split(lists)

hull1=brutehull(split_li[0])


testlist1=[(2, 2), (3, 3), (5, 2), (4, 0), (3, 1)]
testlist2=[(-1, 0), (0, 1), (1, 0), (0, -2)]
testlist1.sort(key=takefirst)
testlist2.sort(key=takefirst)
convex= merge_convex(testlist2,testlist1)

print(find_upper_tangent(testlist2,testlist1))
print(find_lower_tangent(testlist2,testlist1))

plt.figure(1)
x=[]
y=[]
for i in range(len(convex)):
    x.append(takefirst(convex[i]))
    y.append(takesecond(convex[i]))
plt.scatter(x,y,color='red',marker='s')
x=[]
y=[]
plt.figure(2)
for i in range(len(testlist1)):
    x.append(takefirst(testlist1[i]))
    y.append(takesecond(testlist1[i]))
plt.scatter(x,y,color='blue')
x=[]
y=[]
for i in range(len(testlist2)):
    x.append(takefirst(testlist2[i]))
    y.append(takesecond(testlist2[i]))
plt.scatter(x,y,color='blue')

plt.show()
print('finished')