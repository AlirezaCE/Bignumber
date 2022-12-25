from numpy.random import randint
import numpy as np
import random

def sum(): 
    i = 0
    carry = 0

    #generate bignumber
    a = randint(0, 10, randint(5, 10))
    b = randint(0, 10, randint(5, 10))

    print(np.flip(a))
    print(np.flip(b))

    # print(a)
    # print(b)

    n1 = len(a)
    n2 = len(b)

    n = min(n1, n2)

    #result
    c = []

    while(n>0):
        m = a[i] + b[i] + carry
        c.append(m%10)
        # c = m%10 
        carry = int(m/10)
        i += 1
        n -= 1

    while carry > 0:
        if n1 == max(n1,n2) and n1 > i:
            carry = int((carry + a[i])/10)
            c.append(carry + a[i])
        elif n2 > i: # elif  = else if 
            carry = int((carry + b[i])/10)
            c.append(carry + b[i])
        else:
            c.append(carry)
            carry = 0
        i += 1

    if n1 == max(n1, n2) and n1 > i :
        c.extend(a[i:]) # a[2:5] a[:5] a[2:]
    elif n2 > i :
        c.extend(b[i:])

    print(np.flip(c))


def sub(): 
    i = 0
    carry = 0

    #generate bignumber
    a = randint(0, 10, randint(5,10))
    b = randint(0, 10, randint(5,10))

    print(np.flip(a)) 
    print(np.flip(b))

    n1 = len(a)
    n2 = len(b)

    n = min(n1, n2)

    c = []

    if n2 > n1: 
        a , b = b , a
        # temp = a    
        # a = b
        # b = temp

    while(n>0):
        m = a[i] - b[i] + carry

        if m < 0 : 
            m += 10
            carry = -1
        else:
            carry = 0

        c.append(m) 

        i += 1
        n -= 1

    while carry == -1:
        a[i] = a[i] + carry
        carry = a[i]
        if a[i] == -1 :
            a[i] += 10
        i += 1

    c.extend(a[i:])

    print(np.flip(c))


def multi():
    res = []
    i = 0
    carry = 0

    #generate bignumber
    a = randint(0, 10, randint(5,10))
    b = randint(0, 10)

    n = len(a)

    print(np.flip(a))
    print(np.flip(b))
    
    while(n>i):
        m = a[i] * b + carry
        res.append(m%10) # res = m%10
        carry = int(m/10) #carry = m/10
        i += 1

    if carry > 0:
        res.append(carry)
        i += 1

    print(np.flip(res))

if __name__ == "__main__":
    # sum() 
    # sub()
    multi()