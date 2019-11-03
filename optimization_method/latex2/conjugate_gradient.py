# -*- coding: utf-8 -*-
"""
@author: Starklee created on 2019-10-13
"""
import random
import sympy
import numpy as np
import math
import matplotlib.pyplot as pl
from scipy.linalg import orth
from mpl_toolkits.mplot3d import Axes3D as ax3

def random_int_list(start, stop, length):
  start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
  length = int(abs(length)) if length else 0
  random_list = []
  for i in range(length):
   random_list.append(random.randint(start, stop))
  return random_list


def random_SSDP(N):
    # 生成随机对称正定矩阵
    D = np.diag(random_int_list(1, 100, N))
    a = np.array(random_int_list(1, 100, N ** 2))
    u = a.reshape((N, N))
    U = orth(u)
    A = np.dot(U.T, D)
    A = np.dot(A, U)
    lam = np.linalg.eigvals(A)
    A = A - max(lam)*np.eye(N)
    print('是半正定矩阵')
    return A

def random_UD(N):
    # 生成随机对称正定矩阵
    D = np.diag(random_int_list(1, 100, N))
    a = np.array(random_int_list(1, 100, N ** 2))
    u = a.reshape((N, N))
    U = orth(u)
    A = np.dot(U.T, D)
    A = np.dot(A, U)
    lam = np.linalg.eigvals(A)
    A = A - ((max(lam)+min(lam))/2)*np.eye(N)
    B = np.linalg.eigvals(A)
    if np.all(B < 0):
        print('是负定 矩阵')
    elif np.all(B > 0):
        print('是正定 矩阵')
    elif np.all(B >= 0):
        print('是半正定 矩阵')
    else:
        print('是不定矩阵')
    return A

def random_SDP(N):
    # 生成随机对称正定矩阵
    D = np.diag(random_int_list(1, 100, N))
    a = np.array(random_int_list(1, 100, N ** 2))
    u = a.reshape((N, N))
    U = orth(u)
    A = np.dot(U.T, D)
    A = np.dot(A, U)
    B = np.linalg.eigvals(A)
    if np.all(B > 0):
        print('是正定 矩阵')
    return A





# 共轭梯度法
def CG(x0, N, E, f, f_d):
    X = [];
    Y = [];
    Y_d = [];
    #初始化
    n = 0
    r0 = -f_d(x0)
    rk0=r0
    rk=r0
    dk=0
    x=x0
    e=1
    while n < N and e > E:
        n = n + 1
        dk = rk + dk*np.linalg.norm(rk) ** 2/np.linalg.norm(rk0) ** 2
        ak = np.linalg.norm(rk) ** 2/np.dot(np.dot(dk.T, A), dk)
        x = x + dk * ak
        rk0=rk
        rk = -f_d(x)
        X.append(n)
        Y.append(f(x)[0, 0])
        e = np.linalg.norm(f_d(x))
        Y_d.append(e)
        print ('第%2s次迭代：f(x)=%f e=%f' % (n, f(x), e))
    return X, Y, Y_d

# 最速下降法
def SD(x0, N, E, f, f_d):
    X = [];
    Y = [];
    Y_d = [];
    #初始化
    n = 0
    x=x0
    e=1
    #f = lambda x: 0.5 * (np.dot(np.dot(x.T, A), x)) - np.dot(b.T, x)
    #f_d = lambda x: np.dot(A, x) - b
    while n < N and e > E:
        n = n + 1
        dk = f_d(x)
        ak = np.dot(dk.T, dk)/np.dot(np.dot(dk.T, A), dk)
        x = x - dk * ak
        X.append(n)
        Y.append(f(x)[0, 0])
        e = np.linalg.norm(f_d(x))
        Y_d.append(e)
        print ('第%2s次迭代：f(x)=%f e=%f' % (n, f(x), e))
    return X, Y, Y_d

# 牛顿法
def NT(x0, N, E, f, f_d):
    X = [];
    Y = [];
    Y_d = [];
    #初始化
    n = 0
    x=x0
    e=1
    #f = lambda x: 0.5 * (np.dot(np.dot(x.T, A), x)) - np.dot(b.T, x)
    #f_d = lambda x: np.dot(A, x) - b -> gx
    while n < N and e > E:
        n = n + 1
        dk = f_d(x)
        x = x - np.dot(np.linalg.inv(A),dk)
        X.append(n)
        Y.append(f(x)[0, 0])
        e = np.linalg.norm(f_d(x))
        Y_d.append(e)
        print ('第%2s次迭代：f(x)=%f e=%f' % (n, f(x), e))
    return X, Y, Y_d





if __name__ == '__main__':
    N=40
#    A=random_SSDP(N)
    A = random_SDP(N)
#    A=random_UD(N)
    x_goal = np.ones((N, 1))
    b = np.dot(A, x_goal)
    print(np.dot(b.T, x_goal))
    c = 0
    f = lambda x: 0.5 * (np.dot(np.dot(x.T, A), x)) - np.dot(b.T, x)
    f_d = lambda x: np.dot(A, x) - b
    x0 = x_goal + np.random.rand(N, 1) * 100000
    N = 10000#最大迭代次数
    E = 10 ** (-6)#计算精度要求
    print ('共轭梯度')
    X1, Y1, Y_d1 = CG(x0, N, E, f, f_d)
    print('最速下降')
    X2, Y2, Y_d2 = SD(x0, N, E, f, f_d)
    print('牛顿法')
    X3, Y3, Y_d3 = NT(x0, N, E, f, f_d)

    figure1 = pl.figure('SSDP')
    pl.subplot(1,3,1)
    pl.semilogx(X1, Y_d1, color='b',linestyle='dashed', marker='+', label='CG')#绘制收敛图像
    pl.legend()
    pl.xlabel('n')
    pl.ylabel('f(x)')

    pl.subplot(1, 3, 2)
    pl.semilogx(X2, Y_d2, color='b',linestyle='dashed', marker='+', label='SD')#绘制收敛图像
    pl.legend()
    pl.xlabel('n')
    pl.ylabel('f(x)')

    pl.subplot(1, 3, 3)
    pl.semilogx(X3, Y_d3, color='b',linestyle='dashed', marker='+', label='NT')#绘制收敛图像
    pl.legend()
    pl.xlabel('n')
    pl.ylabel('f(x)')

    pl.show()
