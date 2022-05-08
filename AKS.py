import math
from sympy.ntheory.factor_ import totient
import numpy as np

def stepuno(n):
    for b in range(2,int(math.log(n,2))+1):
        for a in range(2, int(n**0.5)+1):
            print('a = '+str(a)+', b = '+str(b))
            if (n==a**b):
                print('a^b = '+str(a)+'^'+str(b)+' equals '+str(n))
                return 'composite'
            print('a^b = '+str(a)+'^'+str(b)+' does not equal '+str(n))
    return



def stepdos(n):
    count = 0
    for r in range(2,max(3,int(math.log(n,2)**5)+1)):
        if count == int(math.log(n,2)**2)-1:
            print("r = ",r-1, " satisfies the conditions for multplicative order.")
            return r-1
        count = 0
        for k in range(1,int(math.log(n,2)**2)):
            count += 1
            print("Testing r = ", r, "with k = ", k)
            if (n**k) % r == 1 or (n**k) % r == 0:
                print("The given r and k fail the given conditions. Moving on to a new value for r.")
                break

def steptres(r,n):
    for a in range(2,r):
        print("Checking if GCD(a,n) is within the bounds, where a = ", a)
        if math.gcd(a,n) > 1 and math.gcd(a,n) < n :
            print("The GCD(a,n) is between 1 and n. Therefore ", n, " is composite.")
            return 'composite'
    return

def stepcuatro(n,r):
    if n <= r:
        print('n is less than or equal to r. Therefore n must be prime')
        return 'prime'


def stepcinco(n,r):
    for a in range(1,int(totient(n)**0.5 * math.log(n,2))):
        left_hand_side = np.poly1d([1,a])**n
        right_hand_side = np.poly1d([1]+[0 for i in range(n-2)]+[a])
        divisor = np.poly1d([1]+[0 for i in range(r-2)]+[-1])
        quotientLHS, remainderLHS = np.polydiv(left_hand_side, divisor)
        quotientRHS, remainderRHS = np.polydiv(right_hand_side, divisor)
        print("Checking if a = ", a, " satisfies the stated property.")
        if(np.all(np.polysub(np.array(remainderLHS)%n,np.array(remainderRHS)%n) != 0)):
            print("The given value of a fails. Therefore n is composite.")
            return 'composite'


  

n = 69 #composite

outputs = []
outputs.append(stepuno(n))
r = stepdos(n)
outputs.append('lol')
outputs.append(steptres(r,n))
outputs.append(stepcuatro(n,r))
outputs.append(stepcinco(n,r))
count = 0
for i in range(len(outputs)):
    if outputs[i] == 'composite':
        print('the number is composite, it failed step', i+1)
        break
    count += 1
if count == len(outputs):
    print('the number is prime')
    



