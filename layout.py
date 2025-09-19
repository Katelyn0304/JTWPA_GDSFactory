import gdsfactory as gf
from cpw import cpw
from g import g
from bridge import bridge

@gf.cell
def layout(
    cpw_parameters: dict,
    bridge_parameters: dict,
    layer: tuple,
    layer_m: tuple,
    layer_a: tuple
):
    c = gf.Component("layout")

    cpw_ref = c << cpw(**cpw_parameters)
    bridge_ref = c << bridge(**bridge_parameters)
    g_ref = g(layer_m=layer_m)
    bridge_ref.connect("center", g_ref.ports["center"], allow_layer_mismatch=True)
    cpw_ref.connect("center", g_ref.ports["center"])
    ground_ref = gf.boolean(A=g_ref, B=cpw_ref, operation="not", layer1=layer_m, layer2=layer_m, layer=layer)
    air = gf.boolean(A=cpw_ref, B=cpw_ref, operation="not", layer1=layer_m, layer2=layer, layer=layer_a)
    c.add_ref(ground_ref)
    # c.add_ref(air)
    return c

if __name__ == "__main__":
    cpw_parameters = {
        "n": 100,
        "spacing": 5.0,
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
            "size_": 10000
        },
        "boun_cap_parameters": {
            "width": 5.0,
            "length": 100.0,
            "layer": (1, 0),
            "layer_": (10, 0),
            "size_": 3000
        },
        "JJ_parameters": {
            "width": 15.0,
            "height": 1.0,
            "L_J_length": 1.0,
            "layer": (1, 0),
            "layer_": (10, 0),
            "sizex_": 3,
            "sizey_": 10
        },
        "cap_parameters": {
            "width": 5.0,
            "length": 200.0,
            "layer": (1, 0),
            "layer_": (10, 0),
            "size_": 3000
        },
        "layer_": (10, 0),
        "layer_m": (3, 0),
    }
    comp = layout(cpw_parameters=cpw_parameters)
    comp.show()