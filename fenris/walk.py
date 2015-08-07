import numpy as np
import math

angle = np.arange(0, 2 * math.pi, 0.1)


def animate(i):
    x = 200*np.cos(i)
    y = 100*np.sin(i)
    y = y if y > 0 else 0
    _dist = np.sqrt(x**2+(200-y)**2)
    angle_leg = np.arcsin(x/_dist)
    angle_edge = np.arccos((_dist/2)/150)
    return "{%s, %s} ," % (np.degrees(angle_leg), np.degrees(angle_edge))

points = []
for ang in angle:
    points.append(animate(ang))

print len(angle)
print '{'
for p in points:
    print p
print '}'
