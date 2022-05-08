import math
from sympy.ntheory.factor_ import totient
import numpy as np

def stepuno(n):
    for b in range(2,int(math.log(n,2))+1):
        for a in range(2, int(n**0.5)+1):
            if (n==a**b):
                return 'composite'
    return

##upper bounds fixed is faster than updating them each time (?)

def stepdos(n):
    count = 0
    for r in range(2,max(3,int(math.log(n,2)**5)+1)):
        if count == int(math.log(n,2)**2)-1:
            return r-1
        count = 0
        for k in range(1,int(math.log(n,2)**2)):
            count += 1
            if (n**k) % r == 1 or (n**k) % r == 0:
                break

def steptres(r,n):
    for a in range(2,r):
        if math.gcd(a,n) > 1 and math.gcd(a,n) < n :
            return 'composite'
    return

def stepcuatro(n,r):
    if n <= r:
        return 'prime'

##runs in nlog(n) since n numbers to check and gcd alg. is log(n)
def stepcinco(n,r):
    for a in range(1,int(totient(n)**0.5 * math.log(n,2))):
        left_hand_side = np.poly1d([1,a])**n
        right_hand_side = np.poly1d([1]+[0 for i in range(n-2)]+[a])
        divisor = np.poly1d([1]+[0 for i in range(r-2)]+[-1])
        quotientLHS, remainderLHS = np.polydiv(left_hand_side, divisor)
        quotientRHS, remainderRHS = np.polydiv(right_hand_side, divisor)
        if(np.all(np.polysub(np.array(remainderLHS)%n,np.array(remainderRHS)%n) != 0)):
            return 'composite'


  
#first upper bound is lemma 3.1 in primes paper
# second upper bound still need to understand
# this is the r that we want since Ord_r(n) is n^k = 1 mod(r)
# if we don't find it then the multiplcative order is great than log_2(n)^2

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
    



