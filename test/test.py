import gdsfactory as gf
from port import port
from boun_cap import boun_cap
from cap import cap
from JJ import JJ

@gf.cell
def chain(n: int = 100, spacing: float = 5.0):
    c = gf.Component("chain")

    left_port = c << port()
    left_boun_cap = c << boun_cap()

    left_boun_cap.connect("left", left_port.ports["right"])
    left_boun_cap.movex(spacing)
    prev = left_boun_cap

    for i in range(1, n):
        JJ_ref = c << JJ()
        JJ_ref.connect("left", prev.ports["right"])
        JJ_ref.movex(spacing)
        prev = JJ_ref
        cap_ref = c << cap()
        cap_ref.connect("left", prev.ports["right"])
        cap_ref.movex(spacing)
        prev = cap_ref

    JJ_ref_last = c << JJ()
    JJ_ref_last.connect("left", prev.ports["right"])
    JJ_ref_last.movex(spacing)
    prev = JJ_ref_last
    right_boun_cap = c << boun_cap()
    right_boun_cap.connect("left", prev.ports["right"])
    right_boun_cap.movex(spacing)
    right_port = c << port()
    right_port.rotate(180)
    right_port.connect("right", right_boun_cap.ports["right"])
    right_port.movex(spacing)

    # region = c.get_region(layer=(1, 0))
    # c2 = gf.Component()
    # c2.add_polygon(region.size(3000), layer=(2, 0))
    # region = c2.get_region(layer=(2, 0), merge=True)
    # c.add_polygon(region, layer=(2, 0))

    return c

if __name__ == "__main__":
    chain().show()
