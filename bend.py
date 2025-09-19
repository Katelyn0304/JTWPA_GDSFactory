import gdsfactory as gf
from basic_unit import rectangle

@gf.cell
def bend(
    line_width: float, 
    taper_parameters: dict,
    JJ_parameters: dict,
    cap_parameters: dict,
    n: int,
    layer: tuple,
    layer_: tuple,
    layer_c: tuple,
    layer_b: tuple,
    size_: int
):
    c = gf.Component("bend")
    
    taper_width = (taper_parameters["height"]-taper_parameters["line_width"])/2+taper_parameters["width"]
    line_length = (5000 - (2*taper_width + (n+2)*(cap_parameters["width"]+2*cap_parameters["spacing"]) + n*(JJ_parameters["L_J_length"]+2*JJ_parameters["width"])))/2
    c << rectangle(width=line_length, height=line_width, layer=layer)

    region = c.get_region(layer=layer)
    c.add_polygon(region.size(size_ * 1000), layer=layer_)

    c.add_port("left", center=(0, line_width/2), orientation=180, width=1, layer=layer)
    c.add_port("right", center=(line_length, line_width/2), orientation=0, width=1, layer=layer)
    
    radius = 5
    c_ = gf.Component()
    for i in range(1, 5):
        circ_d = c << gf.components.circle(radius=radius, layer=layer_c)
        circ_d.move((line_length * i/5, -size_ - radius - 2))
        circ_u = c << gf.components.circle(radius=radius, layer=layer_c)
        circ_u.move((line_length * i/5, line_width + size_ + radius + 2))

        circ_d_ = c_ << gf.components.circle(radius=radius, layer=(1,0))
        circ_d_.move((line_length * i/5, -size_ - radius - 2))
        circ_u_ = c_ << gf.components.circle(radius=radius, layer=(1,0))
        circ_u_.move((line_length * i/5, line_width + size_ + radius + 2))

        rect = c_ << rectangle(width=2*radius, height=line_width + 2*size_ + 4 + 2*radius, layer=(1,0))
        rect.move((line_length * i/5 - radius, -size_ - radius - 2))
    bridge_region = c_.get_region(layer=(1,0), merge=True)
    c.add_polygon(bridge_region, layer=layer_b)

    return c

if __name__ == "__main__":
    bend_parameters = {
        "line_width": 18.0,
        "line_length": 500.0,
        "layer": (1, 0),
        "layer_": (10, 0),
        "size_": 10
    }
    comp = bend(**bend_parameters)
    comp.show()
