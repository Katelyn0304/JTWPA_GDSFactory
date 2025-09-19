import gdsfactory as gf

@gf.cell
def rectangle(width: float, height: float, layer):
    c = gf.Component("rectangle")
    pts = [(0,0), (width,0), (width,height), (0,height)]
    c.add_polygon(pts, layer=layer)
    c.add_port("top", center=(width/2, height), orientation=90, width=1, layer=layer)
    c.add_port("bottom", center=(width/2, 0), orientation=270, width=1, layer=layer)
    c.add_port("left", center=(0, height/2), orientation=180, width=1, layer=layer)
    c.add_port("right", center=(width, height/2), orientation=0, width=1, layer=layer)
    return c

def circle(radius: float, layer):
    c = gf.Component("circle")
    circle = gf.components.circle(radius=radius, layer=layer)
    c.add_ref(circle)
    c.add_port("center", center=(0, 0), orientation=0, width=1, layer=layer)
    return c

if __name__ == "__main__":
    rectangle(width=100.0, height=200.0, layer=(1, 0)).show()
    circle(radius=50.0, layer=(2, 0)).show()