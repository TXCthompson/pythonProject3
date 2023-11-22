import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.coords = [vertice1, vertice2, vertice3]

    def distance(self, point1, point2):
        return math.sqrt((point2._Point__x - point1._Point__x)**2 + (point2._Point__y - point1._Point__y)**2)

    def perimeter(self):
        side1 = self.distance(self.coords[0], self.coords[1])
        side2 = self.distance(self.coords[1], self.coords[2])
        side3 = self.distance(self.coords[2], self.coords[0])

        return side1 + side2 + side3


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())