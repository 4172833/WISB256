import sys
import random
import math

if len(sys.argv) > 3:
    seed = float(sys.argv[3])
    random.seed(seed)

if len(sys.argv) < 3:
    print("Use: estimate_pi.py N L")
    exit(1)

N = int(sys.argv[1])
L = float(sys.argv[2])

def drop_needle(L):
    x0 = random.random()
    theta = random.vonmisesvariate(0,0)
    x1 = x0 + L*math.cos(theta)
    if x1 >= 1 or x1 <= 0:
        return True
    else:
        return False

i = 0
hits = 0
while i < N:
    if drop_needle(L) == True:
        hits = hits + 1
    i = i + 1

if L > 1:
    a = math.sqrt(L*L-1) + math.asin(1/L)
    PI = (2*L - 2*a)/((hits/N) - 1)
    print(hits, "hits in", N, "tries")
    print("Pi =", PI)
else:
    approx = 2*L/(hits/N)
    print(hits, "hits in", N, "tries")
    print("Pi =", approx)