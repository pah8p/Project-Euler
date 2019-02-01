

N = 50

points = []
for x in range(N+1):
    for y in range(N+1):
        if x == 0 and y == 0:
            pass
        else:
            points.append((x, y))

rights = 0
for p in range(len(points)):
    for q in range(p+1, len(points)):

        s1 = points[p][0]**2 + points[p][1]**2
        s2 = points[q][0]**2 + points[q][1]**2
        s3 = (points[q][0]-points[p][0])**2 + (points[q][1]-points[p][1])**2

        if (s1+s2==s3) or (s2+s3==s1) or (s1+s3==s2):
            rights += 1
            ##print('%s ; %s' % (points[p], points[q]))

print(rights)



##(1, 0) ; (0, 1)
##(1, 0) ; (1, 1)
##(1, 0) ; (0, 2)
##(1, 0) ; (1, 2)
##
##(2, 0) ; (0, 1)
##(2, 0) ; (1, 1)
##(2, 0) ; (2, 1)
##(2, 0) ; (0, 2)
##(2, 0) ; (2, 2)
##
##(1, 1) ; (0, 1)
##
##(2, 1) ; (0, 1)
##
##(1, 1) ; (0, 2)
##
##(1, 2) ; (0, 2)
##
##(2, 2) ; (2, 2)
