from functools import reduce
import matplotlib.pyplot as plt

#Cele doua poligoane
d1 = [(5, 0), (7, 0), (7, 3), (5, 3)]
d2 = [(-1, -2), (1, -2), (1, 1), (-1, 1)]

#Functia de acoperire convexa
def convex_hull_graham(points): 
    TURN_LEFT, TURN_RIGHT, TURN_NONE = (1, -1, 0)

    def cmp(a, b):
        return (a > b) - (a < b)

    def turn(p, q, r):
        return cmp((q[0] - p[0])*(r[1] - p[1]) - (r[0] - p[0])*(q[1] - p[1]), 0)

    def _keep_left(hull, r):
        while len(hull) > 1 and turn(hull[-2], hull[-1], r) != TURN_LEFT:
            hull.pop()
        if not len(hull) or hull[-1] != r:
            hull.append(r)
        return hull

    points = sorted(points)
    l = reduce(_keep_left, points, [])
    u = reduce(_keep_left, reversed(points), [])
    return l.extend(u[i] for i in range(1, len(u) - 1)) or l

#Acoperirea convexa a reuniunii de puncte
d1.extend(d2)
coord = convex_hull_graham(d1)

#Afisam rezultatul
def arata(pct):
    coord.append(coord[0])
    xs, ys = zip(*coord)
    plt.figure()
    plt.plot(xs, ys)

plt.show()
arata(coord)