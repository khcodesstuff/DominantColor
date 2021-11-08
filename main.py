# So basically I take image colors
# Sort them by which color channel dominates in single color (getting 3 lists of colors)
# Getting the biggest list out of 3 (this color channel dominates in the picture)
# Calculating average color from all colors in this biggest list
#
# Which happens to be the dominant color in the picture
# Because I counted average from the biggest list (where only one channel is dominating)

from PIL import Image

img = Image.open('images/forest.jpg')
img_small = img.resize((150,150))
colors = img_small.getcolors(maxcolors=1000000)

# Sort colors by the fact that certain channel value dominates
# E.g. (100, 255, 100) goes into G_dominant
R_dominant, G_dominant, B_dominant = [],[],[]
for color in colors:
    if color[1].index(max(color[1])) == 0:
        R_dominant.append(color[1])
    elif color[1].index(max(color[1])) == 1:
        G_dominant.append(color[1])
    elif color[1].index(max(color[1])) == 2:
        B_dominant.append(color[1])

print("Number of colors where RED dominates:")
print(len(R_dominant))
print("Number of colors where GREEN dominates:")
print(len(G_dominant))
print("Number of colors where BLUE dominates:")
print(len(B_dominant))

def calculate_average(dominant_colors):
    # Separate the color channels
    r, g, b = [],[],[]
    for color in dominant_colors:
        r.append(color[0])
        g.append(color[1])
        b.append(color[2])

    average_r = sum(r) / len(r)
    average_g = sum(g) / len(g)
    average_b = sum(b) / len(b)

    return (average_r, average_g, average_b)

# Calculate average color of the biggest array
dominant_color = ()
if len(R_dominant) > len(G_dominant) and len(R_dominant) > len(B_dominant):
    dominant_color = calculate_average(R_dominant)
elif len(G_dominant) > len(R_dominant) and len(G_dominant) > len(B_dominant):
    dominant_color = calculate_average(G_dominant)
elif len(B_dominant) > len(R_dominant) and len(B_dominant) > len(G_dominant):
    dominant_color = calculate_average(B_dominant)

print("\nDominant color is:")
print(dominant_color)
