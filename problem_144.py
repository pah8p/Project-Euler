from decimal import Decimal

class Vector(object):

    def __init__(self, x, y):
        self.x = Decimal(x)
        self.y = Decimal(y)
        self.magnitude = Decimal(x**2+y**2).sqrt()

    def unit(self):
        return Vector(self.x/self.magnitude, self.y/self.magnitude)

    def dot(self, w):
        return self.x*w.x + self.y*w.y

    def __sub__(self, w):
        return Vector(self.x-w.x, self.y-w.y)

    def __mul__(self, w):
        if isinstance(w, Vector):
            return self.dot(w)
        else:
            return Vector(self.x*w, self.y*w)

    def __repr__(self):
        return 'x=%s y=%s' % (self.x, self.y)

def quadratic(a, b, c):
    #a, b, c = Decimal(a), Decimal(b), Decimal(c)
    d = Decimal(b**2-4*a*c).sqrt()
    return (-b+d)/(2*a), (-b-d)/(2*a)
    
def reflected_ray(intersection_point, ray):
    slope_of_tangent = -4*intersection_point.x/intersection_point.y
    slope_of_normal = -1/slope_of_tangent
    normal_unit = Vector(1, slope_of_normal).unit()
    ray_unit = ray.unit()
    reflected = normal_unit*(normal_unit*ray_unit*2) - ray_unit
    return reflected

def intersection_point(reflection_point, ray):
    m = ray.y/ray.x
    b = reflection_point.y-m*reflection_point.x
    x = quadratic(4+m**2, 2*m*b, b**2-100)


    z = abs(x[0]-reflection_point.x)
    
    #print(x, reflection_point.x, z, z<0.001)
    
    if z < 0.0000001:
        y = m*x[1]+b
        return Vector(x[1], y)
    
    else:# abs(x[1] - reflection_point.x) < 1e3:
        y = m*x[0]+b
        return Vector(x[0], y)

def bounce_light(entry_point, first_intersection):
    ray = first_intersection-entry_point
    point = first_intersection
    i = 1

    x_bot = -0.01
    x_top = 0.01
    y_bot = (100-4*x_bot**2)**0.5
    
    while True:
        ray = reflected_ray(point, ray)
        point = intersection_point(point, ray)

        #if i < 10: print(i, point)
        
        if -0.01 < point.x < 0.01:
            #print(i, point, y_bot)
            if y_bot < point.y:
                print(i, point)
                #pass
                #return i, point

        else:
            i += 1
            #print(i, point, ray)

        if i > 1000: break

        #if i % 1000 == 0:
            #print(i, point, ray)

p0 = Vector(0.0, 10.1)
p1 = Vector(1.4, -9.6)

print(bounce_light(p0, p1))


##ray = p1-p0
##
##
##print(p0)
##print(p1)
##print(ray)
##r_ray = reflected_ray(p1, ray)
##i_point = intersection_point(p1, r_ray)
##print(i_point)
