from arithmetic import *

def partitions(psum, max_summand, min_summand = 1):
    parts = [[] for i in range(psum + 1)]
    parts[0].append(())
    for i in range(min_summand, max_summand + 1): #summand
        for s in range(psum, -1, -1): #sums
            for j in range(1, (psum - s) / i + 1): #multipliers of i      
                for p in parts[s]: # partitions of sum s
                    new_p = p + (0,) * (i - len(p) - 1) + (j,)
                    parts[s + i * j].append(new_p)
    return parts[psum]

def part_sum(partition):
    return sum([partition[i] * (i + 1) for i in range(len(partition))])

def part_max_edges(partition):
    me = 0
    for i in range(len(partition)):
        me += partition[i] * i * (i+1) / 2
    return me

def max_summand(partition):
    return len(partition)

def part_dec(partition):
    partition2 = partition[:-1] + (partition[-1] - 1,)
    while len(partition2) > 0 and partition2[-1] == 0:
        partition2 = partition2[:-1]
    return partition2

def num_groupings(partition):
    ng = fact[part_sum(partition)]
    for i in range(len(partition)):
        ng = ng * fact_inverse[partition[i]] % modulus
        ng = ng * mod_exp(fact_inverse[i + 1], partition[i]) % modulus
    return ng

##def num_grouped_sums(partition, sum_):
##    if sum_ == 0:
##        return 1
##    if partition == ():
##        return 0
##    if (partition, sum_) in ngs_memo:
##        return ngs_memo[(partition, sum_)]
##    ngs = 0
##    partition2 = part_dec(partition)
##    ms = max_summand(partition)
##    for i in range(0, sum_ + 1, ms):
##        ngs = (ngs + num_grouped_sums(partition2, sum_ - i)) % modulus
##    ngs_memo[(partition, sum_)] = ngs
##    return ngs

#num grouped sums
ngs_memo = dict()
ngs_memo_2 = dict()
    
def set_ngs_memo(partition, sum_):
    partition2 = part_dec(partition)
    ms = max_summand(partition)
    ngs = ngs_memo[partition2][sum_]
    if ms <= sum_ :
        ngs = ngs + ngs_memo[partition][sum_ - ms] % modulus
    ngs_memo[partition][sum_] = ngs

def set_ngs_memo_2(partition, sum_):
    partition2 = part_dec(partition)
    ms = max_summand(partition)
    ngs = ngs_memo[partition2][sum_]
    if ms <= sum_ :
        ngs = ngs + ngs_memo_2[partition][sum_ - ms] % modulus
    ngs_memo_2[partition][sum_] = ngs

def init_ngs_memo(factors, max_exp):
    ngs_memo[()] = [1] + [0]*max_exp
    for i in range(1, factors):
        print len(partitions(i, factors - i)), "partitions"
        for p in partitions(i, factors - i):
            ngs_memo[p] = [0] * (max_exp + 1)
            for j in range(max_exp + 1):
                set_ngs_memo(p, j)
        print "done", i, "of", factors
    i = 0
    parts = partitions(factors, factors)
    for p in parts:
        ngs_memo_2[p] = [0] * (max_exp + 1)
        for j in range(max_exp + 1):
            set_ngs_memo_2(p, j)
        i += 1
        if i % 100 == 0:
            print i, "of", len(parts)
    

