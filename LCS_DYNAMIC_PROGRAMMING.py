
import numpy as np
def string_reverse(string):
    return string[::-1]

def LCS_str(s1):
    num1=len(s1)
    arr = [[0 for i in range(num1 + 1)] for j in range(num1 + 1)]
    temp = [i for i in range(num1 + 1)]
    max1 = 0
    p = 0
    s2 = string_reverse(s1)
    cnt =[0 for i in range(num1)];
    for i in range(len(s2)):
        for j in range(len(s1)):
            if s1[i] == s2[j] and i != num1 - j -1:
                arr[i][j] = 1
            else:
                arr[i][j] = 0

    for i in range(num1+1):
        for j in range(i):

            print (arr[7-temp[i]+j+1][j])

            # if arr[i][num1-j-1] == arr[i+1][num1-j]:
            #     cnt[i] = cnt[i]+1





print(LCS_str('REDIVIDE'))
