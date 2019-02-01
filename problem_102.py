
import math

def load_triangles():
    file = 'p102_triangles.txt'
    with open(file, 'r') as f:
        raw_triangles = f.readlines()

    triangles = []
    for t in raw_triangles:
        ps = t.split(',')
        triangle = []
        for i in range(0, 5, 2):
            triangle.append(
                (int(ps[i]), int(ps[i+1]))
            )
        triangles.append(triangle)
        
    return triangles

def intersection(line1, line2):
    x = (line2[1]-line1[1])/(line1[0]-line2[0])
    y = line1[0]*x+line1[1]
    _y = line2[0]*x+line2[1]
    #print(line1, line2, x, y, _y)
    #assert y == _y
    return (x, y)

def line(p1, p2):
    try:
        m = (p1[1]-p2[1])/(p1[0]-p2[0])
    except ZeroDivisionError:
        print(p1, p2)
        m = 1e6
    b = p1[1]-m*p1[0]
    _b = p2[1]-m*p2[0]
    #print(p1, p2, m, b, _b)
    return (m, b)

def point_intersects_side(p1, p2, p3):
    _line = line(p1, (0, 0))
    side = line(p2, p3)
    pI = intersection(_line, side)

    x_min, x_max = min(p2[0], p3[0]), max(p2[0], p3[0])
    y_min, y_max = min(p2[1], p3[1]), max(p2[1], p3[1])

    if x_min < pI[0] < x_max and y_min < pI[1] < y_max:
        return True
    else:
        return False

def check_points_2(points):

    if (
        point_intersects_side(*points) and
        point_intersects_side(points[1], points[2], points[0]) and
        point_intersects_side(points[2], points[0], points[1])
    ):
        return 1

    else:
        return 0

    

    

def angle(p1, p2):
    n_1 = (p1[0]**2+p1[1]**2)**0.5
    n_2 = (p2[0]**2+p2[1]**2)**0.5
    n = n_1*n_2
    dot = p1[0]*p2[0]+p1[1]*p2[1]
    theta = math.degrees(math.acos(dot/n))
    return theta

def radius(p1, p2):

    try:
        m = (p2[1] - p1[1])/(p2[0] - p1[0])
    except ZeroDivisionError:
        return p1[0], 0

    try:
        x = (m*p1[0]-p1[1])/(m+1/m)
    except ZeroDivisionError:
        return 0, p1[1]
    
    y = -x/m
    return x, y #(x**2+y**2)**0.5

def check_points(points):

    radii = [radius(points[i], points[(i+1)%3]) for i in range(3)]
    angles = [angle(radii[i], radii[(i+1)%3]) for i in range(3)]

    if points[0][1] > 0 and points[1][1] > 0 and points[2][1] > 0:
        return 0

    if points[0][1] < 0 and points[1][1] < 0 and points[2][1] < 0:
        return 0

    if points[0][0] > 0 and points[1][0] > 0 and points[2][0] > 0:
        return 0

    if points[0][0] < 0 and points[1][0] < 0 and points[2][0] < 0:
        return 0
        
    if int(sum(angles)) == 360:
        return 1
    else:
        print(points, angles, sum(angles))
        return 0


A = (-340, 495)
B = (-153, -910)
C = (835, -947)
##
X = (-175, 41)
Y = (-421, -714)
Z = (574, -645)
##
##print(radius(A, B))
##print(radius(B, C))
##print(radius(A, C))
print(point_intersects_side(C, A, B))
print(check_points_2([A, B, C]))
##
##print(radius(X, Y))
##print(radius(Y, Z))
##print(radius(X, Z))
#print(check_points_2([X, Y, Z]))

triangles = load_triangles()

print(sum([check_points_2(t) for t in triangles]))
