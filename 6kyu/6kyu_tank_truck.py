import math


class Celindr:
    def __init__(self, h, d, vt):
        self.circle = CircleSquare(h, d)
        self.segment = self.circle.square_segment()
        self.vt = vt

    # def return_del_segment(self):
    #     return self.segment
    def height_celindr(self):
        height = self.vt/math.pi*self.circle.radius
        return height


class CircleSquare:

    def __init__(self, h, d):
        self.h = h
        self.d = d
        self.radius = d/2

    def alfa(self):
        alfa = 2*math.acos(1-self.h/self.radius)
        return math.degrees(alfa), alfa

    def square_segment(self):
        alfa_deg, alfa_rad = self.alfa()
        square = 0.5 * self.radius**2 * (alfa_rad - math.sin(alfa_rad))
        return square



        pass

def tankvol(h, d, vt):

    pass

# Pi * r**2 * h
# This form volume
# all screnshots in folder
circle = CircleSquare(40, 120)
alfa_deg, alfa_rad = circle.alfa()
square = circle.square_segment()
print(alfa_deg, square)

celindr = Celindr(40, 120, 3500)
ans = celindr.height_celindr()
print(ans)
