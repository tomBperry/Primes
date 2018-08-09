import math

primes = []
N = 1000000

def isPrime(n):
   for j in range(2, math.ceil(n / 2) + 1):
       if (n % j == 0):
           break
   else:
       primes.append(n)
       print(str(n) + " is prime!")

for i in range(2, N + 1):
    isPrime(i)

print("There are " + str(len(primes)) + " primes up to " + str(N) + ".")



