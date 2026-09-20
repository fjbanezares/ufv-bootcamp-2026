# Import the colorgram library, which allows us to extract colors from images.
# Import the os library to get access to functionality like getting the current working directory.

import colorgram
import os

# Print the current working directory, useful for debugging paths.
print(os.getcwd())

# Extract 30 colors from an image located at the given path.
# Here, we specify the path to an image called 'paz.jpg'.
# The extract method returns a list of Color objects, each one containing RGB, HSL, and the proportion of that color in the image.

colors = colorgram.extract(
    "/Users/fjbanezares/ufv-bootcamp-python-2023/training/turtle/colorgram/paz.jpg", 30
)

# Print the extracted colors for debugging purposes.
print(colors)

# Accessing the first color from the list of extracted colors.
# This first color is represented as a Color object, which includes its RGB, HSL, and proportion attributes.
first_color = colors[0]
rgb = (
    first_color.rgb
)  # RGB (Red, Green, Blue) - a way to represent colors in a range from 0-255 for each component.
print(rgb)
hsl = (
    first_color.hsl
)  # HSL (Hue, Saturation, Lightness) - another way to represent color.
print(hsl)
proportion = first_color.proportion  # The proportion of the image that is this color.
print(proportion)

# Since RGB and HSL are named tuples, their values can be accessed as properties or via indexing.
red = rgb[0]  # Access the 'Red' value via index.
red = rgb.r  # Access the 'Red' value via property.
print(red)

# Accessing the 'Saturation' value from the HSL named tuple.
saturation = hsl[1]  # Via index.
saturation = hsl.s  # Via property.

# Initialize an empty list to hold the RGB tuples.
rgb_colors = []

# Loop through each Color object to extract its RGB values and append them as a tuple to the rgb_colors list.
# This transformation is essential for using these colors in Python libraries like Turtle, which often expect colors in simple tuple formats.
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))

# Print the final list of RGB tuples.
print(rgb_colors)
