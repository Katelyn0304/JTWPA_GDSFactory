import gdsfactory as gf
from basic_unit import rectangle

@gf.cell
def cap(
    width: float, 
    length: float, 
    layer: tuple,
    layer_: tuple,
    layer_c: tuple,
    size_: int,
    spacing: float
):
    c = gf.Component("cap")

    c << rectangle(width=width, height=length, layer=layer)

    region = c.get_region(layer=layer)
    c.add_polygon(region.size(size_ * 1000), layer=layer_)

    c.add_port("left", center=(0, length/2), orientation=180, width=1, layer=layer)
    c.add_port("right", center=(width, length/2), orientation=0, width=1, layer=layer)

    contact_pts = [
        (-spacing-1.5, (length/2)-8), 
        (width+spacing+1.5, (length/2)-8),
        (width+spacing+1.5, (length/2)+8),
        (-spacing-1.5, (length/2)+8)
    ]
    c.add_polygon(contact_pts, layer=layer_c)

    return c


if __name__ == "__main__":
    cap_parameters = {
        "width": 5.0,
        "length": 200.0,
        "layer": (1, 0),
        "layer_": (10, 0),
        "layer_c": (2, 0),
        "size_": 3,
        "spacing": 2.0
    }
    comp = cap(**cap_parameters)
    comp.show()
