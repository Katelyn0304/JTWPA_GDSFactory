import gdsfactory as gf

@gf.cell
def taper(
    height: float, 
    width: float, 
    line_width: float, 
    layer: tuple,
    layer_: tuple
):
    c = gf.Component("taper")
    dx = (height - line_width)/2
    pts = [
        (0,0), 
        (width, 0), 
        (width + dx, dx), 
        (width + dx, dx + line_width),
        (width, height),
        (0, height)
    ]
    c.add_polygon(pts, layer=layer)

    region_pts = [
        (0, -67.5), 
        (width, -67.5), 
        (width + dx, dx - 10), 
        (width + dx, dx + line_width + 10),
        (width, height + 67.5),
        (0, height + 67.5)
    ]
    c.add_polygon(region_pts, layer=layer_)

    # 左中
    c.add_port(
        name="left",
        center=(0, height/2),
        orientation=180,  # 朝左
        width=1,
        layer=layer,
    )

    # 右中
    c.add_port(
        name="right",
        center=(width+dx, height/2),
        orientation=0,  # 朝右
        width=1,
        layer=layer,
    )

    return c

if __name__ == "__main__":
    taper_parameters = {
        "height": 270.0,
        "width": 190.0,
        "line_width": 18.0,
        "layer": (1, 0),
        "layer_": (10, 0)
    }
    comp = taper(**taper_parameters)
    comp.show()
