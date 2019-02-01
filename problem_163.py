

class Vertex(object):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_children(self, vertices):
        for vertex in vertices:
            self.children.append(vertex)
        
class Triangle(object):
    def __init__(self, vertices):
        self.vertices = vertices

    def _sub_triangles(self):
        subs = []
        for vertex in self.vertices:
            for child in vertex.children:
                for grandchild in child.children:
                    for great_grandchild in grandchild.children:
                        if great_grandchild.name == vertex.name:
                            nodes = [vertex.name, child.name, grandchild.name]
                            nodes.sort()
                            subs.append(''.join(nodes))
        print(list(set(subs)))
        return len(set(subs))
            
a = Vertex('A')
b = Vertex('B')
c = Vertex('C')
d = Vertex('D')
e = Vertex('E')
f = Vertex('F')
g = Vertex('G')

a.add_children([d, e, g])
b.add_children([e, f, g])
c.add_children([d, f, g])
d.add_children([a, c, g])
e.add_children([a, b, g])
f.add_children([b, c, g])
g.add_children([a, b, c, d, e, f])

t = Triangle([a, b, c, d, e, f, g])

print(t._sub_triangles())
