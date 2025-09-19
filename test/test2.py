import gdsfactory as gf
from bridge import bridge

@gf.cell
def test(bridge_parameters):
    c = gf.Component()
    bridge_ref = c << bridge(**bridge_parameters)
    c.add_port("center", center=(bridge_ref.x, bridge_ref.y), orientation=0, width=1, layer=bridge_parameters["layer"])
    return c

if __name__ == "__main__":
    LAYER = {
        "Main": (1, 0),
        "Contact": (2, 0),
        "Bridge": (3, 0),
        "Mask": (4, 0),
        "Air": (1, 10),
        "Unmerged_M": (10, 0),
        "Unmerged_B": (30, 0),
    }
    cap_parameters = {
        "width": 6.0,
        "length": 200.0,
        "layer": LAYER["Main"],
        "layer_": LAYER["Unmerged_M"],
        "layer_c": LAYER["Contact"],
        "size_": 3,
        "spacing": 2.0
    }
    JJ_parameters = {
        "width": 6.0,
        "height": 1.0,
        "L_J_length": 1.0,
        "layer": LAYER["Main"],
        "layer_": LAYER["Unmerged_M"],
        "layer_c": LAYER["Contact"],
        "sizex_": 3,
        "sizey_": 10
    }
    bridge_parameters = {
        "JJ_params": JJ_parameters,
        "cap_params": cap_parameters,
        "n": 100,
        "layer": LAYER["Bridge"],
        "layer_": LAYER["Unmerged_B"],
    }
    comp = test(bridge_parameters=bridge_parameters)
    comp.show()
