# Create a function that returns both the area and the circumference of a circle given its radius ; 

import math

def circle_stats(radius):
    area = math.pi*radius*radius
    circum = 2 * math.pi*radius
    return area , circum

a, b = circle_stats(5)
print(f"Area : {a:.3f}")
print(f"circum: {b:.3f}")