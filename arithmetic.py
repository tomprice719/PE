modulus = 1000000007
fact_range = 2000
fact = [1]
fact_inverse = [1]

def bezout(a, b):
    assert((a, b) != (0, 0))
    if a == 0:
        return (0, 1)
    if b == 0:
        return (1, 0)
    if a <= b:
        c = b % a
        x, y = bezout(a, c)
        return (x -(b/a) * y, y)
    y, x = bezout(b, a)
    return (x, y)

def inverse(x):
    y, _ = bezout(x, modulus)
    return y % modulus

for i in range(fact_range):
    fact.append(fact[i] * (i + 1) % modulus)
    fact_inverse.append(fact_inverse[i] * inverse(i + 1) % modulus)

def mod_exp(b, e):
    p = 1
    for i in range(e):
        p = p * b % modulus
    return p

def choose(a, b):
    if b > a:
        return 0
    return fact[a] * fact_inverse[b] * fact_inverse[a - b] % modulus

