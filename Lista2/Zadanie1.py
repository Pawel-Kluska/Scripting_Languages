import math

degrees = 360


def from_degrees_to_radians(d):
    return (math.pi / 180) * d


def form_radians_to_degrees(r):
    return (180/math.pi)*r


print(from_degrees_to_radians(degrees))
print(from_degrees_to_radians(degrees/4))
print(from_degrees_to_radians(degrees/8))

print(math.radians(degrees))
print(math.radians(degrees/4))
print(math.radians(degrees/8))
