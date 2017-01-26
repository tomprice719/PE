#TODO: put everything where you need to think about the internal structure of a partition into one "partition.py" file
#TODO: memoize partitions and num_groupings


#define fact, fact_inverse
from arithmetic import *
from partition import *


#memoize
num_connected_memo = dict()
manual_nc = 0
def num_connected(vertices, edges):
    global manual_nc
    if (vertices, edges) in num_connected_memo:
        return num_connected_memo[(vertices, edges)]
    if edges < vertices - 1:
        return 0
    num_possible_edges = vertices * (vertices - 1) / 2
    total_graphs = choose(num_possible_edges, edges)
    if edges > (vertices - 1)*(vertices - 2) / 2:
        return total_graphs
    num_disconnected = 0
    for partition in partitions(vertices, vertices - 1):
        num_disconnected += num_graphs(partition, edges) * num_groupings(partition) % modulus
    nc = (total_graphs - num_disconnected) % modulus
    num_connected_memo[(vertices, edges)] = nc
    manual_nc += 1
    return nc

#TODO: memoize better:
#make keys partitions and have lists for different numbers of edges
num_graphs_memo = dict()
manual_ng = 0
all_ng = 0
def num_graphs(partition, edges):
    global manual_ng
    global all_ng
    all_ng += 1
    if edges == 0 and len(partition) <= 1:
        return 1
    if edges == 0 or len(partition) <= 1:
        return 0
    if partition in num_graphs_memo:
        if num_graphs_memo[partition][edges] != -1:            
            return num_graphs_memo[partition][edges]
    else:
        num_graphs_memo[partition] = [-1] * 450
    if edges > part_max_edges(partition):
        return 0
    ms = max_summand(partition) #2
    partition1 = part_dec(partition) #(0, 1)
    ng = 0
    #range(1, 2)
    for i in range(edges - part_max_edges(partition1), ms * (ms - 1) / 2 + 1):
      ng = (ng + num_connected(ms, i) * num_graphs(partition1, edges - i)) % modulus
    num_graphs_memo[partition][edges] = ng
    manual_ng += 1
    return ng

def compute_graph_data(num_factors, max_edges):
    global manual_nc, manual_ng, all_ng
    for i in range(num_factors):
        for j in range(max_edges):
            x = num_connected(i, j)
        print "done", i, "of", num_factors
