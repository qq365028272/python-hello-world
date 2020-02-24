import  math
from fractions import Fraction

def readius_area (r):
    return math.pi * r ** 2

def cylinder_volume (r,h):
    return r**2 * math.pi * h

def cone_volume (r,h):
    return r**2 * math.pi * h * Fraction(1,3)