import math

class CircleSquare:

    def __init__(self, h, d):
        self.h = h
        self.d = d

    def alfa(self):
        radius = self.d/2
        alfa = 2*math.acos(1-self.h/radius)
        return math.degrees(alfa), alfa


    def square_segment(self):


        pass

def tankvol(h, d, vt):

    pass

# Pi * r**2 * h
# This form volume
# all screnshots in folder
circle = CircleSquare(12, 1500)
alfa_deg, alfa_rad = circle.alfa()
print(alfa_deg)