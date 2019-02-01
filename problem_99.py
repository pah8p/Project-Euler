
import math

def load_nums():
    file = 'C:/Users/Pete/AppData/Local/Programs/Python/Python36-32/Scripts/euler/p099_base_exp.txt'
    with open(file, 'r') as f:
        raw_matrix = f.readlines()

    matrix = []
    for i, row in enumerate(raw_matrix):
        #print(i)
        vals = row[:-1].split(',')
        base = int(vals[0])
        exp = int(vals[1])
        matrix.append((i, exp*math.log(base)))
            

    return max(matrix, key=lambda x: x[1])

print(518061*math.log(632382) > 525806*math.log(519432))
print(632382**518061 > 519432**525806)

print(load_nums())
