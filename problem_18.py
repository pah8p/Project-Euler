
EASY_TRIANGLE = [
[3,],
[7,4,],
[2,4,6,],
[8,5,9,3,]
]

TRIANGLE = [
[75],
[95, 64],
[17, 47, 82],
[18, 35, 87, 10],
[20, 4, 82, 47, 65],
[19, 1, 23, 75, 3, 34],
[88, 2, 77, 73, 7, 63, 67],
[99, 65, 4, 28, 6, 16, 70, 92],
[41, 41, 26, 56, 83, 40, 80, 70, 33],
[41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
[63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
[4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23],
]

##00
##10 11
##20 21 22
##30 31 32 33
##
##10 = 10 + 00
##11 = 10 + 00
##
##10 11
##20 21 22
##30 31 32 33
##
##20 = 20 + 10
##21 = 21 + max(10, 11)
##22 = 22 + 11
##
##  20  21  22
##30  31  32  33
##
##30 = 30 + 20
##31 = 31 + max(20, 21)
##32 = 32 + max(21, 22)
##33 = 33 + 22

def sum_triangle(t):

    i = 0
    
    for row_num, row_value in enumerate(t):
        for col_num, col_value in enumerate(row_value):

            if row_num == 0:
                pass

            elif col_num == 0:
                t[row_num][col_num] += t[row_num-1][col_num]

            elif col_num+1 == len(row_value):
                t[row_num][col_num] += t[row_num-1][col_num-1]

            else:
                t[row_num][col_num] += max(t[row_num-1][col_num-1], t[row_num-1][col_num])

            i += 1
                
    print(t)
    print(i)
    return max(t[-1])

##print(sum_triangle(EASY_TRIANGLE))
##
##print(sum_triangle(TRIANGLE))








            
