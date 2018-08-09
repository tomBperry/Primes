import math
# Number of digits in number
N = 4

primes = []

for n in range(N):
    primes.append([])

def isPrime(n, arr):
   for j in range(2, math.ceil(n / 2) + 1):
       if (n % j == 0):
           break
   else:
       arr.append(n)
       # print(str(n) + " is prime!")

for i in range(2, 10):
    isPrime(i, primes[0])

for i in range(1, 10):
    for j in range(len(primes[0])):
        isPrime(10*i + primes[0][j], primes[1])

for i in range(1, 10):
    for j in range(len(primes[1])):
        isPrime(10*i + primes[1][j], primes[2])

print(primes[2])
print("There are " + str(len(primes[2])) + " left-truncated primes that are 2 digits long.")

for i in range(1, 10):
    print(i)
