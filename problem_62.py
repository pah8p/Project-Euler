from collections import defaultdict

cubes = {}


def sort_num(num):
    str_num = str(num)
    lst_num = list(str_num)
    lst_num.sort()
    y = ''
    for x in lst_num:
        y = '%s%s' % (y, x)
    return y

i = 0
while True:

    cube = i**3
    hashed = sort_num(cube)
    
    if hashed in cubes:
        cubes[hashed]['count'] += 1
        cubes[hashed]['vals'].append(cube)

    else:
        cubes[hashed] = {
            'count': 1,
            'vals': [cube],
        }

    if cubes[hashed]['count'] == 5:
        print(cubes[hashed]['vals'])
        print(min(cubes[hashed]['vals']))
        break

    i += 1
