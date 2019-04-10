
from math import sin, cos, tan, pi

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

'''
def t_from_theta(theta, phi):
    t = 0.00001
    while True:
        x = r_x(phi, t)
        y = r_y(phi, t)

        #print(t, x, y, tan(theta), y/x)

        if y < 0:
            break

        if abs(tan(theta) - y/x) < 1e-3:
            return t, x, y
        
        t += 0.00001
'''

def degree_to_rad(d):
    return d*PI/180
           
def r(theta):
    rs = []
    for d_phi in range(0, 91):
        phi = degree_to_rad(d_phi)
        if phi > theta:
            t = t_from_theta(theta, phi)
            x = r_x(phi, t)
            y = r_y(phi, t)
            rs.append((x**2 + y**2, x, y, t))
    
    return max(rs, key=lambda x: x[0])

def area():
    a = 0
    step = 1
    lo = -90*step
    hi = 90*step
    for _theta in range(lo, hi):
        theta = degree_to_rad(_theta/step)
        a += r(theta)[0]*degree_to_rad(1/step)
    return a

def volume():
    return 2*PI*area()

print(r(PI/4))
print(area())
print(volume())

#print(t_from_theta(PI/4, PI/3))

#_t = t(PI/4, PI/3)

#print(_t, r_x(PI/3, _t), r_y(PI/3, _t))








