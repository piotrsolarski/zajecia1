from math import sqrt

class Line:
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2
        self.x1 = coor1[0]
        self.y1 = coor1[1]
        self.x2 = coor2[0]
        self.y2 = coor2[1]

    def distance(self):
        return (self.y2 - self.y1) / (self.x2 - self.x1)

    def slope(self):
        slope = (self.y2 - self.y1)**2 + (self.x2 - self.x1)**2
        return sqrt(slope)

coor1 = (1, 1)
coor2 = (12, 7)

line = Line(coor1, coor2)

print(line.distance())
