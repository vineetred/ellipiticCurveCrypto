def check_EC(point): #function to check if given co-ordinates are part of EC or not
    x,y = point
    if(x>p or x<0 or y>p or y<0):
        return False
    flag = ((y**2 - (x**3 + a*x + b)))%p==0
    return flag
