from problem_18 import sum_triangle

with open('C:/Users/Pete/AppData/Local/Programs/Python/Python36-32/Scripts/euler/p067_triangle.txt', 'r') as f:
    t = f.readlines()

tt = []
for _t in t:
    tt.append([int(__t) for __t in _t.split(' ')])



print(sum_triangle(tt))
