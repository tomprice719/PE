from arithmetic import *
from partition import *
from graphs import *

def fact_exp(n, p):
    e = 0
    pp = p
    while(pp <= n):
        e += n / pp
        pp *= p
    return e

print "A"

is_prime = [False] + [False] + [True] * (10000 - 1)
primes = []
for i in range(len(is_prime)):
    if is_prime[i]:
        primes.append(i)
        for j in range(0, len(is_prime), i):
            is_prime[j] = False

exponents = [fact_exp(10000, p) for p in primes]

print "B"

init_ngs_memo(30, 10000)

print "C"

ngs_memo.clear()

print "D"

partition_products = dict()

pts = partitions(30, 30)

i = 0

for p in pts:
    pp = 1
    for e in exponents:
        pp = pp * ngs_memo_2[p][e] % modulus
    partition_products[p] = pp
    i += 1
    if i % 100 == 0:
        print i, "of", len(pts)
        
print "E"

ngs_memo_2.clear()

print "F"

compute_graph_data(31, 440)

print "G"

num_products = 0

for i in range(436):
    for p in pts:
        num_products =  (num_products + partition_products[p] * num_graphs(p, i) * num_groupings(p) * (-1)**i) % modulus

num_products = num_products * fact_inverse[30] % modulus

print "final answer: ", num_products
