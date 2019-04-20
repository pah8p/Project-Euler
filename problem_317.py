
from math import sin, cos, tan, pi
from matplotlib import pyplot
import euler_tools
from scipy import integrate

Y = 100
V = 20
G = -9.81
PI = pi

def r_x(phi, t):
    return V*t*cos(phi)

def r_y(phi, t):
    return Y + V*t*sin(phi) + 0.5*G*t**2

def quadratic(a, b, c):
    d = (b**2 - 4*a*c)**0.5
    return (-b+d)/(2*a), (-b-d)/(2*a)

def t_from_theta(theta, phi):
    a = G/2
    b = V*sin(phi)-V*cos(phi)*tan(theta)
    c = Y
    pos, neg = quadratic(a, b, c)
    if pos > 0:
        return pos
    elif neg > 0:
        return neg
    else:
        print(rad_to_degree(theta), rad_to_degree(phi), pos, neg, a, b, c)

def degree_to_rad(d):
    return d*PI/180

def rad_to_degree(r):
    return 180*r/PI

def max_radius(theta):
    rs = []
    step = 10
    for d_phi in range(0, 180*step + 1):
        phi = degree_to_rad(d_phi/step)
        t = t_from_theta(theta, phi)
        x = r_x(phi, t)
        y = r_y(phi, t)
        if y > 0:
            rs.append((x**2 + y**2, x, y, t, phi))
    
    try:
        max_r = max(rs, key=lambda x: x[0])
        return max_r
    except ValueError:
        return None, None, None, None, None
  
def curve():
    step = 10
    xs, ys, rs, ps, ts = [], [], [], [], []
    for _theta in range(0, 90*step + 1):
        theta = degree_to_rad(_theta/step)

        r, x, y, t, phi = max_radius(theta)

        if r:
            xs.append(x)
            ys.append(y)
            rs.append((x, y))
            ps.append(phi)
            ts.append(theta)

    print('y_max', max(ys))

    pyplot.plot(xs, ys)
    pyplot.show()

    return rs

def _curve(y, points):
    for p in range(1, len(points)):
        if points[p][1] > y:
            x = ((points[p][1] - y)*points[p-1][0] + (y-points[p-1][1])*points[p][0])/(points[p][1]-points[p-1][1])
            return PI*x**2
    return None


def parabola():
    xs, ys, rs = [], [] , []
    for _x in range(0, 10000000):
        x = _x/1000000
        
        xs.append(x)
        ys.append(100-x**2)
        rs.append((x, 100-x**2))

        #xs.append(-x)
        #ys.append(100-x**2)
        #rs.append((-x, 100-x**2))        

    #pyplot.plot(xs, ys, 'ro')
    #pyplot.show()

    return rs

def area():
    rs = curve()   
    rs.sort(key=lambda r: r[0], reverse=False)
    a = 0
    for n in range(1, len(rs)):
        y = rs[n][1]
        dx = rs[n][0] - rs[n-1][0]
        a += y*dx
    return a

def volume():
    rs = curve()
    rs.sort(key=lambda r: r[1], reverse=False)
    v = 0
    for n in range(1, len(rs)):
        x = (rs[n][0] + rs[n-1][0])/2
        dy = rs[n][1] - rs[n-1][1]
        v += PI*x**2*dy
    return v

#parabola()

#print(r(PI/4))
with euler_tools.Watch():

    points = curve()
    points.sort(key=lambda r: r[1], reverse=False)

    print(_curve(50, points))
    print(integrate.quad(_curve, 0, 10, args=(points,)))

    #print(volume())

#print(t_from_theta(PI/4, PI/3))

#_t = t(PI/4, PI/3)

#print(_t, r_x(PI/3, _t), r_y(PI/3, _t))


#print(quadratic(G/2, V, Y))

#pyplot.plot(
#    [r_x(PI/4, t/100) for t in range(0, 700)],
#    [r_y(PI/4, t/100) for t in range(0, 700)],
#)
#pyplot.show()




