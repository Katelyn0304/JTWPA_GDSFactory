import gdsfactory as gf
from basic_unit import rectangle

@gf.cell
def bridge(
    JJ_params: dict,
    cap_params: dict,
    n: int,
    layer: tuple,
    layer_: tuple
):
    c = gf.Component("bridge")

    radius = JJ_params["width"]-2
    circ_1 = c << gf.components.circle(radius=radius, layer=layer_)
    circ_2 = c << gf.components.circle(radius=radius, layer=layer_)
    circ_3 = c << gf.components.circle(radius=radius, layer=layer_)
    circ_4 = c << gf.components.circle(radius=radius, layer=layer_)

    height = JJ_params["height"]+2*JJ_params["sizey_"]+2*JJ_params["width"]+JJ_params["L_J_length"]
    unit_width = JJ_params["L_J_length"]+2*JJ_params["width"]+2*cap_params["spacing"]+cap_params["width"]
    width = n * unit_width

    circ_2.movex(width)
    circ_3.move((width, height))
    circ_4.movey(height)

    rect_d = c << rectangle(width=width, height=2*radius, layer=layer_)
    rect_d.movey(-radius)
    rect_u = c << rectangle(width=width, height=2*radius, layer=layer_)
    rect_u.movey(height - radius)

    rect_1 = c << rectangle(width=2*radius, height=height, layer=layer_)
    rect_1.movex(-radius)

    for i in range(1, n+1):
        if i % 5 == 0:
            rect = c << rectangle(width=2*radius, height=height, layer=layer_)
            rect.movex(i * unit_width - radius)
        else:
            continue

    region = c.get_region(layer=layer_, merge=True)
    c.add_polygon(region, layer=layer)

    c.add_port("center", center=(c.x, c.y), orientation=0, width=1, layer=layer)

    return c

if __name__ == "__main__":
    JJ_parameters = {
        "width": 6.0,
        "height": 1.0,
        "L_J_length": 1.0,
        "layer": (1, 0),
        "layer_": (10, 0),
        "layer_c": (2, 0),
        "sizex_": 3,
        "sizey_": 10
    }
    cap_parameters = {
        "width": 5.0,
        "length": 200.0,
        "layer": (1, 0),
        "layer_": (10, 0),
        "layer_c": (2, 0),
        "size_": 3,
        "spacing": 2.0
    }
    comp = bridge(JJ_params=JJ_parameters, cap_params=cap_parameters, n=100, layer=(3,0), layer_=(30,0))
    comp.show()