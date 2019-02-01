
import copy
import collections

M = [
[0,16,12,21,0,0,0,],
[16,0,0,17,20,0,0,],
[12,0,0,28,0,31,0,],
[21,17,28,0,18,19,23,],
[0,20,0,18,0,0,11,],
[0,0,31,19,0,0,27,],
[0,0,0,23,11,27,0,],
]

OPT_M = [
[0,16,12,0,0,0,0],
[16,0,0,17,0,0,0],
[12,0,0,0,0,0,0],
[0,17,0,0,18,19,0],
[0,0,0,18,0,0,11],
[0,0,0,19,0,0,0],
[0,0,0,0,11,0,0],
]


def load_graph():
    file = 'p107_network.txt'
    with open(file, 'r') as f:
        raw_graph = f.readlines()

    graph = []
    for raw_row in raw_graph:
        row = []
        raw_cols = raw_row.split(',')
        for raw_col in raw_cols:
            if raw_col[0] == '-':
                row.append(0)
            else:
                row.append(int(raw_col))
        graph.append(row)

    return graph

def siblings(node, matrix, seen = []):
    _sibs = []
    node_row = matrix[node]
    for col_num, col_val in enumerate(node_row):
        if col_val and col_num not in seen:
            #print(col_val, col_num, seen, _sibs)
            seen.append(col_num)
            _sibs.append(col_num)
            sib_sibs = siblings(col_num, matrix, seen)
            for sib_sib in sib_sibs:
                _sibs.append(sib_sib)
    return list(set(_sibs))

def check_graph(matrix):
    good_node = list(range(len(matrix)))
    for i in range(len(matrix)):
        if siblings(i, matrix, []) != good_node:
            return False
    return True

def optimize_graph(matrix):
    matrix = copy.deepcopy(matrix)
    key_nodes = []

    i = 1

    while True:

        print(i)
        _matrix = copy.deepcopy(matrix)

        edges = []
        for row_num, row in enumerate(matrix):
            for col_num, col in enumerate(row):
                if (row_num, col_num) not in key_nodes and col > 0:
                    edges.append((col, row_num, col_num))

        if len(edges) == 0:
            break

        max_edge = max(edges, key=lambda x: x[0])

        matrix[max_edge[1]][max_edge[2]] = 0
        matrix[max_edge[2]][max_edge[1]] = 0

        if not check_graph(matrix):
            key_nodes.append((max_edge[1], max_edge[2]))
            matrix = copy.deepcopy(_matrix)
        i += 1
    return matrix

def sum_graph(matrix):
    s = 0
    for row in matrix:
        #print(sum(row))
        s += sum(row)
    return s/2

#opt_m = optimize_graph(M)

#print(sum_graph(M)-sum_graph(opt_m))
#print(sum_graph(M))

#for r in opt_m: print(r)

#for r in OPT_M: print(r)

graph = load_graph()

graph_score = sum_graph(graph)

opt_graph = optimize_graph(graph)

opt_score = sum_graph(opt_graph)

print(graph_score - opt_score)


