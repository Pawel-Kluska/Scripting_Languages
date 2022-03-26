import math

value = 360


def from_degrees_to_radians(d):
    return (math.pi / 180) * d


def form_radians_to_degrees(r):
    return (180 / math.pi) * r


def print_radians_to_degrees(degrees):
    print(from_degrees_to_radians(degrees))
    print(from_degrees_to_radians(degrees / 4))
    print(from_degrees_to_radians(degrees / 8))


def print_radians_from_degrees_module(degrees):
    print(math.radians(degrees))
    print(math.radians(degrees / 4))
    print(math.radians(degrees / 8))


print_radians_to_degrees(value)
print_radians_from_degrees_module(value)
