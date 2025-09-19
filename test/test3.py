import gdsfactory as gf

c = gf.Component()
c1 = c << gf.components.circle(radius=10)
c2 = c << gf.components.circle(radius=9)
c2.movex(5)

c.show()