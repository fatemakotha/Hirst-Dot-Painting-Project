import colorgram

# Extract 6 colors from an image.
colors = colorgram.extract('image.png', 20) #20 colors extracted
print(colors)
# prints: [<colorgram.py Color: Rgb(r=245, g=247, b=251), 81.01821862348179%>,
# <colorgram.py Color: Rgb(r=252, g=247, b=241), 5.323886639676114%>,
# <colorgram.py Color: Rgb(r=237, g=241, b=240), 1.7854251012145748%>, .....ETC upto 20 OBJECTS of either RGB or HSL color TUPLES ***