import sys
import time

N = int(sys.argv[1])
PrimeList = list(range(0, N+1))
PrimeList[1] = 0
Echtepriemgetallen = []
T1 = time.perf_counter()

primes = range(1, N+1)
for i in primes:
    factors = range(i, N+1, i)
    if PrimeList[i] != 0:
        Echtepriemgetallen.append(PrimeList[i])
        for j in factors[1:]:
            PrimeList[j] = 0

T2 = time.perf_counter()
lengte = len(Echtepriemgetallen)
print('Found', lengte, 'Prime numbers smaller than', int(sys.argv[1]), 'in', str(T2 - T1), 'sec.')

file = open(sys.argv[2], "w")

sep = ""
for x in Echtepriemgetallen:
    file.write(sep + str(x))
    sep = "\n"
    
file.close()