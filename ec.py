import numpy as np
import math

file = open("variables.txt", 'r')
contents = file.read().split(" ")
file.close()
p = int(contents[0])
a = int(contents[1])
b = int(contents[2])

infinity = [-1,-1]

def bits(n):
    while n:
        yield n & 1
        n >>= 1

# def inv(e,phi):
#     def ext_GCD(e_KEY, mod_PHI):
#         if (e_KEY == 0):
#             return (mod_PHI, 0, 1)
#         g, y, x = ext_GCD(mod_PHI%e_KEY,e_KEY)
#         return (g, x - (mod_PHI//e_KEY) * y, y)

#     def modinv(e_KEY, mod_PHI):
#         g, x, y = ext_GCD(e_KEY, mod_PHI)
#         return x%mod_PHI
#     d_key = modinv(e,phi)
#     return d_key

def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)
 
def inv(a, m):
    g, x, y = extended_gcd(a, m)
    if (g != 1):
	    raise ValueError
    return x % m


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
        inverse = inv((arg2[0]-arg1[0]),p)
        slope = ((arg2[1]-arg1[1])*inverse)%p   
        x_r = (pow(slope,2) - arg1[0] - arg2[0])%p
        y_r = (slope*(arg1[0]-x_r) - arg1[1])%p
        return [x_r,y_r]

def pointDoubling(arg1):
    inverse = inv(2*arg1[1],p)
    slope = (3*pow(arg1[0],2)+a)*inverse
    x_r = (pow(slope,2)-(2*arg1[0]))%p
    y_r = (slope*(arg1[0]-x_r)-arg1[1])%p
    return [x_r,y_r]

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

def negationPoint(point):
    return [point[0],(-point[1])%p]

def subtractionPoint(point1,point2):
    return addition(point1,negationPoint(point2))

def functionCheck(xcord):
    y2 = (xcord**3 + a*xcord + b)%p
    y = math.sqrt(y2)
    return int(y)
# print(multiplePoint([4,14],3))
print(addition([8,2],[4,14]))
print(addition([4,14],[8,2]))
# print(functionCheck(56))
# print(negationPoint([1,2]))

def check_EC(x,y): #function to check if given co-ordinates are part of EC or not
    
    return ((y**2 - (x**3 + a*x + b)) % p == 0 and 0 <= x < p and 0 <= y < p)
