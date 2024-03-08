from vpython import *

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
planet = sphere(pos=sun.pos + vector(r1, 0, 0), radius=0.01, color=color.purple, make_trail=True)

# تکانه بر اساس سرعت اولیه و جرم آن
planet.p = m * vector(0, v1, 0)

t = 0
dt = 0.001

a1 = sphere(pos=planet.pos, radius=0.02, color=color.green)
a2 = sphere(pos=planet.pos, radius=0.02, color=color.green)
b1 = sphere(pos=planet.pos, radius=0.02, color=color.orange)
b2 = sphere(pos=planet.pos, radius=0.02, color=color.orange)

while t < 70:
    rate(1000)
    # محاسبه R بردار بین خورشید و زمین
    R = planet.pos - sun.pos
    # نیروی گرانش
    # norm = جهت بردار R , meg = قدر مطلق R
    F = -G * M * m * norm(R) / mag(R) ** 2
    planet.p = planet.p + F * dt
    planet.pos = planet.pos + planet.p * dt / m
    if planet.pos.y > 0 and abs(norm(planet.p).y) < 0.01:
        b1.pos = planet.pos
    if planet.pos.y < 0 and abs(norm(planet.p).y) < 0.01:
        b2.pos = planet.pos
    if planet.pos.x < 0 and abs(norm(planet.p).x) < 0.01:
        a2.pos = planet.pos