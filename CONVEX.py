# Input : First Polygon  : {(2, 2), (3, 3), (5, 2), (4, 0), (3, 1)}
#         Second Polygon : {(-1, 0), (0, 1), (1, 0), (0, -2)}.
# Output : Upper Tangent - line joining (0,1) and (3,3)
#          Lower Tangent - line joining (0,-2) and (4,0)
import math

def takefirst(elem):
    return elem[0]

def find_upper_tangent(a,b):
    return(p1,p2)

def find_lower_tangent(a,b):
    return(p1,p2)

def find_convex(s0):
    return(s1)


lists = [[2, 2], [3, 3], [5, 2], [4, 0], [3, 1], [-1, 0], [0, 1], [1, 0], [0, -2]]
lists.sort(key=takefirst)
lists_temp=[[]]
num0= math.floor(len(lists)/5)
for i in range (num0):
    lists_temp[i]=lists[i:i+5]

if len(lists) - 5*num0 != 0:
    lists_temp.append(lists[5*num0:len(lists)-1])


print('finished')