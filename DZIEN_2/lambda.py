print((lambda g:g*8)(7))

x = lambda a,c=4: a*c**2

print(x(4,2))

def px(a,c):
    return a*c**2

print(px(4,2))

print(x(5))

def multip(h):
    return lambda b:b*h/2

print(multip(6)(3))

nbs = [5,1,3,7,9,12,4,45,66,78,79,101,99,40,-45,-22,0]
