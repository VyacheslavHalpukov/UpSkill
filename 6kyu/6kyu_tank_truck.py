import math


class Celindr:
    def __init__(self, h, d, vt):
        self.circle = CircleSquare(h, d)
        self.segment = self.circle.square_segment()
        self.circle_square = self.circle.square_circle()
        self.vt = vt

    def height_celindr(self):
        height = self.vt/self.circle_square
        return height

    def volume_segment(self):
        volume_segment = self.segment * self.height_celindr()
        return volume_segment


class CircleSquare:

    def __init__(self, h, d):
        self.h = h
        self.d = d
        self.radius = d/2

    def alfa(self):
        alfa = 2*math.acos(1-self.h/self.radius)
        return math.degrees(alfa), alfa

    def square_circle(self):
        square = math.pi * self.radius**2
        return square

    def square_segment(self):
        alfa_deg, alfa_rad = self.alfa()
        square = 0.5 * self.radius**2 * (alfa_rad - math.sin(alfa_rad))
        return square




def tankvol(h, d, vt):
    volume_segment = Celindr(h, d, vt).volume_segment()
    return math.floor(volume_segment)




# Pi * r**2 * h
# This form volume
# all screnshots in folder
circle = CircleSquare(5, 7)
alfa_deg, alfa_rad = circle.alfa()
square_seg = circle.square_segment()
square_full = circle.square_circle()
print(alfa_deg, square_seg, square_full)

celindr = Celindr(5, 7, 3848)
ans = celindr.height_celindr()
print(ans * square_seg)

result_finish = tankvol(2, 7, 3848)
print(result_finish)
