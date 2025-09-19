import gdsfactory as gf
from taper import taper
from bend import bend
from boun_cap import boun_cap
from cap import cap
from JJ import JJ

@gf.cell
def cpw(
    n: int, 
    spacing: float,
    taper_parameters: dict,
    bend_parameters: dict,
    boun_cap_parameters: dict,
    JJ_parameters: dict,
    cap_parameters: dict,
    layer_: tuple,
    layer_m: tuple,
):
    c = gf.Component("cpw")

    left_taper = c << taper(**taper_parameters)
    left_bend = c << bend(**bend_parameters)
    left_bend.connect("left", left_taper.ports["right"])
    left_boun_cap = c << boun_cap(**boun_cap_parameters)
    left_boun_cap.connect("left", left_bend.ports["right"])
    left_boun_cap.movex(spacing)
    prev = left_boun_cap

    for _ in range(n):
        JJ_ref = c << JJ(**JJ_parameters)
        JJ_ref.connect("left", prev.ports["right"])
        JJ_ref.movex(spacing)
        prev = JJ_ref
        cap_ref = c << cap(**cap_parameters)
        cap_ref.connect("left", prev.ports["right"])
        cap_ref.movex(spacing)
        prev = cap_ref

    JJ_ref_last = c << JJ(**JJ_parameters)
    JJ_ref_last.connect("left", prev.ports["right"])
    JJ_ref_last.movex(spacing)
    prev = JJ_ref_last
    right_boun_cap = c << boun_cap(**boun_cap_parameters)
    right_boun_cap.connect("left", prev.ports["right"])
    right_boun_cap.movex(spacing)

    right_bend = c << bend(**bend_parameters)
    right_bend.connect("left", right_boun_cap.ports["right"])
    right_bend.movex(spacing)
    right_taper = c << taper(**taper_parameters)
    right_taper.rotate(180)
    right_taper.connect("right", right_bend.ports["right"])

    region = c.get_region(layer=layer_, merge=True)
    c.add_polygon(region, layer=layer_m)

    c.add_port("center", center=(c.x, c.y), orientation=0, width=1, layer=layer_m)

    return c

if __name__ == "__main__":
    cpw_parameters = {
        "n": 100,
        "spacing": 2.0,
        "taper_parameters": {
            "height": 270.0,
            "width": 190.0,
            "line_width": 18.0,
            "layer": (1, 0),
            "layer_": (10, 0)
        },
        "bend_parameters": {
            "line_width": 18.0,
            "line_length": 500.0,
            "layer": (1, 0),
            "layer_": (10, 0),
            "size_": 10
        },
        "boun_cap_parameters": {
            "width": 6.0,
            "length": 100.0,
            "layer": (1, 0),
            "layer_": (10, 0),
            "layer_c": (2, 0),
            "size_": 3,
            "spacing": 2.0
        },
        "JJ_parameters": {
            "width": 6.0,
            "height": 1.0,
            "L_J_length": 1.0,
            "layer": (1, 0),
            "layer_": (10, 0),
            "layer_c": (2, 0),
            "sizex_": 3,
            "sizey_": 10
        },
        "cap_parameters": {
            "width": 5.0,
            "length": 200.0,
            "layer": (1, 0),
            "layer_": (10, 0),
            "layer_c": (2, 0),
            "size_": 3,
            "spacing": 2.0
        },
        "layer_": (10, 0),
        "layer_m": (3, 0),
    }
    comp = cpw(**cpw_parameters)
    comp.show()
