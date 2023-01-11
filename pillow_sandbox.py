from PIL import Image

# instantiate an 800 * 1280 white image
img1 = Image.new("RGB", (1000, 1000), (255, 255, 255))
img2 = Image.new("RGB", (1000, 1000), (255, 255, 255))

# set variables for width and height
# width, height= img.size
# print(width)
# print(height)

# show image
# img.show()

black= (0, 0, 0)
yummy_orange= (235, 94, 52)

"""
args:
img - Image instance
color - RGB tuple (R, G, B)
"""
def draw_line_down_middle(img, color):
    width, height= img.size
    x= int(width / 2)
    for y in range(height):
        img.putpixel((x, y), color)
    return

# TEST FUNCTION

#draw_line_down_middle(img, black)
#img.show()

def draw_line_across_middle(img, color):
    width, height= img.size
    y= int(height / 2)
    for x in range(width):
        img.putpixel((x, y), color)
    return

#draw_line_across_middle(img, black)
#img.show()

def draw_line_down(img, color, x):
    width, height= img.size
    for y in range(height):
        img.putpixel((x, y), color)
    return

"""
some_x_values= [100, 200, 400, 800]

for x in some_x_values:
    draw_line_down(img, black, x)
img.show()
"""

def draw_line_down_inverted(img, color, x):
    width, height= img.size
    for y in range(height):
        img.putpixel((-x, y), color)
    return

def draw_line_across(img, color, y):
    width, height= img.size
    for x in range(width):
        img.putpixel((x, y), color)
    return

def draw_line_across_inverted(img, color, y):
    width, height= img.size
    for x in range(width):
        img.putpixel((x, -y), color)
    return

"""
returns a list of ints starting at 1, in multiples up to x
e.g. multiple of 2:  1, 2, 4, 8, 16, etc.
"""
def multiply_me_up_to(x, multiple):
    lst= []
    value= 1
    while value < x:
        lst.append(value)
        value= int((value * multiple) + 1)
    return lst


my_values= multiply_me_up_to(500, 1.075)
for x in my_values:
    draw_line_down(img1, black, x)
    draw_line_down_inverted(img1, black, x)
    
for y in my_values:
    draw_line_across(img1, black, y)
    draw_line_across_inverted(img1, black, y)
img1.show()
# img1.save("geometry.png", "PNG")


def fill(img, color):
    width, height= img.size
    for x in range(width):
        for y in range(height):
            img.putpixel((x, y), color)
    return

# TEST fill() FUNCTION

# fill(img, color=black)
# img.show()

def fill_2x2(img, color):
    width, height= img.size
    for x in range(int(width/2)):
        for y in range(int(height/2)):
            img.putpixel((x, y ), color)
            
    for x in range(int(width/2), width):
        for y in range(int(height/2), height):
            img.putpixel((x, y), color)
    return

# TEST fill_2x2 FUNCTION
fill_2x2(img2, yummy_orange)
img2.show()
img2.save("two_by_two.png", "PNG")

def checker_fill(img, color, dimension):
    width, height= img.size
    pass







