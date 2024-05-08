from vpython import *

# مربوط به انیمیشن
g1 = graph(xtitle="x", ytitle="y", width=500, height=300)
f1 = gcurve(color=color.blue)
f2 = gcurve(color=color.red)
f3 = gcurve(color=color.red)


G = 1
M = 1
m = 1
r1 = 1
v1 = 0.7

"""
اعداد واقعی انیمیشن را خراب میکنند
G = 6.7e-11
M = 2e30
m = 6e24
r1 = 1.5e11
v1 = 3e4
"""

# خورشید و کره زمین
sun = sphere(pos=vector(0, 0, 0), radius=0.03, color=color.yellow)
planet = sphere(pos=sun.pos + vector(r1, 0, 0), radius=0.01, color=color.cyan, make_trail=True)

planet.p = m * vector(0, v1, 0)

t = 0
dt = 0.001

a1 = sphere(pos=planet.pos, radius=0.02, color=color.red)
a2 = sphere(pos=planet.pos, radius=0.02, color=color.red)
b1 = sphere(pos=planet.pos, radius=0.02, color=color.blue)
b2 = sphere(pos=planet.pos, radius=0.02, color=color.blue)

while t < 70:
    # چرخش 1000 بار
    rate(1000)
    # محاسبه R بردار بین خورشید و زمین
    R = planet.pos - sun.pos
    # نیروی گرانش
    # norm = جهت بردار R , meg = قدر مطلق R
    F = -G * M * m * norm(R) / mag() ** 2
    planet.p = planet.p + F * dt
    planet.pos = planet.pos + planet.p * dt / m
    if planet.pos.y > 0 and abs(norm(planet.p).y) < 0.01:
        b1.pos = planet.pos
    if planet.pos.y < 0 and abs(norm(planet.p).y) < 0.01:
        b2.pos = planet.pos
    if planet.pos.x < 0 and abs(norm(planet.p).x) < 0.01:
        a2.pos = planet.pos
    f1.plot(planet.pos.x, planet.pos.y)
    t = t + dt

a = mag(a2.pos - a1.pos) / 2
b = mag(b2.pos - b1.pos) / 2
c = a1.pos.x - a
sun2 = sphere(pos=vector(2 * c, 0, 0), radius=0.03)

x = r1
dx = 0.01
while x > a2.pos.x:
    yp = b * sqrt(1 - x ** 2 / a ** 2)
    ym = -b * sqrt(1 - x ** 2 / a ** 2)
    f2.plot(x, yp)
    f3.plot(x, ym)
    x = x - dx