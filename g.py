import gdsfactory as gf
from basic_unit import rectangle

@gf.cell
def g(
    layer_m: tuple
):
    c = gf.Component("g")
    length = 5000.0
    c << rectangle(width=length, height=length, layer=layer_m)
    c.add_port("center", center=(length/2, length/2), orientation=180, width=1, layer=layer_m)
    return c

if __name__ == "__main__":
    comp = g(length=5000.0, layer_m=(3, 0))
    comp.show()
