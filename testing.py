
def double_and_add(n, x):
    """
    Returns the result of n * x, computed using
    the double and add algorithm.
    """
    result = 0
    addend = x

    for bit in bits(n):
        if bit == 1:
            result += addend
        addend *= 2

    return result
print(double_and_add(10,2))

N = [1,3]
Q = [0,0]

for i in range(0,m):
    if(d_i==1):
        Q = addition(Q,N)
    N = pointDoubling(N)
return Q

