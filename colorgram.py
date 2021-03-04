import colorgram

# variable to store image filename
image = 'damien-hirst-lactulose.jpg'

# Empty list
rgb_colors = []


def extract_colors(nr_of_colors):
    """Extract number of colors from an image"""
    # colorgram.extract returns a color object, which gives access to RGB, HSL, and what proportion of the image was that color.
    # RGB and HSL  are named tuples, so values can be accessed as properties.
    colors = colorgram.extract(image, nr_of_colors)
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r, g, b)
        rgb_colors.append(new_color)
    print(rgb_colors)

extract_colors(43)