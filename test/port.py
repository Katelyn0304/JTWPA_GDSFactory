import gdsfactory as gf
from basic_unit import rectangle
from taper import pad

@gf.cell
def port(
    height: float = 270.0, 
    width: float = 190.0, 
    line_width: float = 18.0, 
    line_length: float = 500.0, 
    layer=(1, 0)
):
    c = gf.Component("port")
    line_ref = c << rectangle(width=line_length, height=line_width, layer=layer)
    c.add_polygon(c.get_region(layer=layer).size(3000), layer=(2, 0))
    pad_ref = c << pad(height=height, width=width, line_width=line_width, layer=layer)
    line_ref.connect("left", pad_ref.ports["right"])
    region_pts = [
        (pad_ref.xmin, pad_ref.ymin - 67.5), 
        (pad_ref.xmin + width, pad_ref.ymin - 67.5), 
        (pad_ref.xmax, line_ref.ymin - 10), 
        (pad_ref.xmax, line_ref.ymax + 10),
        (pad_ref.xmin + width, pad_ref.ymax + 67.5),
        (pad_ref.xmin, pad_ref.ymax + 67.5)
    ]
    c.add_polygon(region_pts, layer=(2, 0))

    c.add_port("left",  port=pad_ref.ports["left"])
    c.add_port("right", port=line_ref.ports["right"])
    return c

if __name__ == "__main__":
    port(height=270.0, width=190.0, line_width=18.0, line_length=500.0, layer=(1, 0)).show()
