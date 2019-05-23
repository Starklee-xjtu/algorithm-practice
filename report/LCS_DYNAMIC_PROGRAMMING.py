
import numpy as np
import math


def string_reverse(string):
    return string[::-1]

def LCS_str(s1):
    num1=len(s1)
    lists = [[] for i in range(num1*2-1)]
    arr = [[0 for i in range(num1)] for j in range(num1)]
    arnp= np.asarray(arr)
    temp = [i for i in range(num1)]
    temp0 = np.asarray(temp)
    s2 = string_reverse(s1)
    cnt =[0 for i in range(num1*2-1)];
    ntemp=num1;

    for i in range(len(s2)):
        for j in range(len(s1)):
            if s1[i] == s2[j] and i != num1 - j -1:
                arr[i][j] = 1
            else:
                arr[i][j] = 0

    for i in range(num1*2-1):
        if i < num1 :
            for j in range(i+1):
                #print ([num1-1-temp0[i]+j],[j])
                lists[i].append (arr[num1-1-temp0[i]+j][j])
        else:
            ntemp=ntemp-1;
            for j in range(ntemp):
                lists[i].append (arr[j][j+1+i-num1])

    for i in range(num1 * 2 - 1):
        cnt[i]=lists[i].count(1)

    num4 = max (cnt)
    i=cnt.index(num4)
    cnt2 =[0 for i in range(num4)]; #存储重复字段

    ntemp = num1;
    num3=0;
    if i < num1 :
        for j in range(i+1):
            if arr[num1-1-temp0[i]+j][j] == 1:
                cnt2[num3] = (s1[num1-1-temp0[i]+j])
                num3=num3+1
    else:
        ntemp=ntemp-i+num1-1;
        for j in range(ntemp):
            if arr[j][j+1+i-num1] == 1:
                cnt2 [num3] = (s1[j])
                num3 = num3+1

    print (cnt2[0:math.floor(num4/2)])


            # if arr[i][num1-j-1] == arr[i+1][num1-j]:
            #     cnt[i] = cnt[i]+1
LCS_str('ALGORITHM')
LCS_str('RECURSION')
LCS_str('REDIVIDE')
