import colorgram
# colorgram.extract(image, number_of_colors)   #Extract colors from an image.....1

# colorgram.Color......2

# A color extracted from an image. Its properties are:
# Color.rgb - The color represented as a namedtuple of RGB from 0 to 255, e.g. (r=255, g=151, b=210).
# Color.hsl - The color represented as a namedtuple of HSL from 0 to 255, e.g. (h=230, s=255, l=203).
# Color.proportion - The proportion of the image that is in the extracted color from 0 to 1, e.g. 0.34.






# Extract 6 colors from an image.
colors = colorgram.extract('image.png', 20) #20 colors extracted
print(colors)
# prints: [<colorgram.py Color: Rgb(r=245, g=247, b=251), 81.01821862348179%>,
# <colorgram.py Color: Rgb(r=252, g=247, b=241), 5.323886639676114%>,
# <colorgram.py Color: Rgb(r=237, g=241, b=240), 1.7854251012145748%>, .....ETC upto 20 OBJECTS of either RGB or HSL color TUPLES ***
print("\n")


rgb_colors = []
for each_color in colors: #for EXAMPLE: Color: Rgb(r=245, g=247, b=251)
    r = each_color.rgb.r #so r = 245
    g = each_color.rgb.g #so g = 247
    b = each_color.rgb.b #so b = 251
    my_color_tuple = (r, g, b) #reated a Tuple
    rgb_colors.append(my_color_tuple)

print(rgb_colors)