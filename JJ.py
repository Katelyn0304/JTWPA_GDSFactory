import gdsfactory as gf
from basic_unit import rectangle

@gf.cell()
def JJ(
    width: float, 
    height: float, 
    L_J_length: float, 
    layer: tuple,
    layer_: tuple,
    layer_c: tuple,
    sizex_: int,
    sizey_: int
):
    c = gf.Component("JJ")

    left_ref = c << rectangle(width=width, height=height, layer=layer)
    right_ref = c << rectangle(width=width, height=height, layer=layer)
    L_J_ref = c << rectangle(width=L_J_length, height=L_J_length, layer=layer)

    L_J_ref.connect("left", left_ref.ports["right"])
    right_ref.connect("left", L_J_ref.ports["right"])

    region_pts = [
        (c.xmin - sizex_, c.ymin - sizey_), 
        (c.xmax + sizex_, c.ymin - sizey_), 
        (c.xmax + sizex_, c.ymax + sizey_), 
        (c.xmin - sizex_, c.ymax + sizey_)
    ]

    c.add_polygon(region_pts, layer=layer_)

    c.add_port("left", port=left_ref.ports["left"])
    c.add_port("right", port=right_ref.ports["right"])

    radius = width-2
    cir_ref_1 = c << gf.components.circle(radius=radius, layer=layer_c)
    cir_ref_1.move((width + L_J_length/2, -sizey_ - (width + L_J_length/2)))

    cir_ref_2 = c << gf.components.circle(radius=radius, layer=layer_c)
    cir_ref_2.move((width + L_J_length/2, height + sizey_ + (width + L_J_length/2)))

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
    comp = JJ(**JJ_parameters)
    comp.show()