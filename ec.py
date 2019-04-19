import numpy as np
import math
p = 5
a = 4
b = 4

def bits(n):
    while n:
        yield n & 1
        n >>= 1

infinity = [-1,-1]
def inv(e,phi):
    def ext_GCD(e_KEY, mod_PHI):
        if (e_KEY == 0):
            return (mod_PHI, 0, 1)
        g, y, x = ext_GCD(mod_PHI%e_KEY,e_KEY)
        return (g, x - (mod_PHI//e_KEY) * y, y)

    def modinv(e_KEY, mod_PHI):
        g, x, y = ext_GCD(e_KEY, mod_PHI)
        return x%mod_PHI
    d_key = modinv(e,phi)
    return d_key

def addition(arg1,arg2):
    if(arg1==[-1,-1] and arg2==[-1,-1]): #This is the infinity added to infinity
        return arg1
    '''
    This next construct is for when a point is added to the point
    at infinity
    '''
    if(arg1==[-1,-1]):
        return arg2
    if(arg2==[-1,-1]):
        return arg1
    '''
    Same X coordinate
    '''
    if(arg1[0]==arg2[0]):
        return infinity

    if(arg1[0]!=arg2[0]):
        inverse = inv(arg2[0]-arg1[0],p)
        slope = int(arg2[1]-arg1[1])*inverse
        slope = int(slope)
        x_r = int((pow(slope,2) - arg1[0] - arg2[0])%p)
        y_r = (slope*(arg1[0]-x_r) - arg1[1])%p
        return [x_r,y_r]


def pointDoubling(arg1):
    inverse = inv(2*arg1[1],p)
    slope = (3*pow(arg1[0],2)+a)*inverse
    # slope=math.ceil(slope)
    x_r = (int(pow(slope,2)-2*arg1[0]))%p
    y_r = (int(slope*(arg1[0]-x_r)-arg1[1]))%p
    # arg1[0] = x_r
    # arg1[1] = y_r
    return [x_r,y_r]

# def multiplePoint(numbers,times):
#     newNumbers = pointDoubling(numbers)
#     for i in range(0,times-1):
#         newNumbers = addition(newNumbers,numbers)
#     return newNumbers
# print(pointDoubling([1,3]))
# print(multiplePoint([1,3],5))

def multiplePoint(N,times):
    Q = [-1,-1]
    d = []
    for bit in bits(times):
        d.append(bit)
    for i in range(0,len(d)):
        if(d[i]==1):
            Q = addition(Q,N)
        N = pointDoubling(N)
    return Q

print(multiplePoint([0,2],4))

# print(addition([1,3],[4,2]))


def functionOutput(x):
    y = (x**3+a*x+b)%p
    return int(math.sqrt(y))
# print(functionOutput(1))

