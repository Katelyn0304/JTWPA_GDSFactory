from layout import layout

# Parameters
spacing = 2.0  # CPW gap
n = 150      # Number of JJ and Cap pairs

LAYER = {
    "Main": (1, 0),
    "Contact": (2, 0),
    "Bridge": (3, 0),
    "Mask": (4, 0),
    "Air": (1, 10),
    "Unmerged_M": (10, 0),
    "Unmerged_B": (30, 0),
}

taper_parameters = {
    "height": 270.0,
    "width": 190.0,
    "line_width": 18.0,
    "layer": LAYER["Main"],
    "layer_": LAYER["Unmerged_M"]
}

boun_cap_parameters = {
    "width": 6.0,
    "length": 100.0,
    "layer": LAYER["Main"],
    "layer_": LAYER["Unmerged_M"],
    "layer_c": LAYER["Contact"],
    "size_": 3,
    "spacing": spacing
}

cap_parameters = {
    "width": 6.0,
    "length": 200.0,
    "layer": LAYER["Main"],
    "layer_": LAYER["Unmerged_M"],
    "layer_c": LAYER["Contact"],
    "size_": 3,
    "spacing": spacing
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

bend_parameters = {
    "line_width": 18.0,
    "taper_parameters": taper_parameters,
    "JJ_parameters": JJ_parameters,
    "cap_parameters": cap_parameters,
    "n": n,
    "layer": LAYER["Main"],
    "layer_": LAYER["Unmerged_M"],
    "layer_c": LAYER["Contact"],
    "layer_b": LAYER["Bridge"],
    "size_": 10
}

cpw_parameters = {
    "n": n,
    "spacing": spacing,
    "taper_parameters": taper_parameters,
    "bend_parameters": bend_parameters,
    "boun_cap_parameters": boun_cap_parameters,
    "JJ_parameters": JJ_parameters,
    "cap_parameters": cap_parameters,
    "layer_": LAYER["Unmerged_M"],
    "layer_m": LAYER["Mask"],
}

bridge_parameters = {
    "JJ_params": JJ_parameters,
    "cap_params": cap_parameters,
    "n": n,
    "layer": LAYER["Bridge"],
    "layer_": LAYER["Unmerged_B"],
}

if __name__ == "__main__":
    layout(cpw_parameters=cpw_parameters, bridge_parameters=bridge_parameters, layer=LAYER["Main"], layer_m=LAYER["Mask"], layer_a=LAYER["Air"]).show()