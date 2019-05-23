import copy
import sys

sys.setrecursionlimit(1000000)
def find1(list1):
     for k in range(len(list1)):
          templist3 = list1[k]
          if templist3 != []:
               return k
          else:
               return 0

def find2(list1):
     for k in range(len(list1)):
          templist3 = list1[k]
          if templist3 != []:
               return k
          else:
               return 0


def Branch(list1,delitem):
     templist=copy.deepcopyc(list1)
     P=delitem
     for k in range(len(P)):
          n=P[k]-1
          templist[n]=[]
     return templist




X=[1,2,3,4,5,6]
F=[[1,3],[1,2,3],[4,5,6],[4,5],[4],[5,6]]
flag=[[],[],[],[],[],[]]
list1=[]
for i in range(len(X)):
     list1.append([])


for i in range(len(F)):
     temp = F[i]
     temp.sort
     for k in range(len(X)):
          if temp[0]==X[k]:
               list1[k].append(temp)
               break

while flag!=0

Branch(list1,0,[])