from turtle import *
from random import randint

image_width = int(input("Width: "))
image_height = int(input("Height: "))

X = image_width / -2
Y = image_height / 2

count = 0

hideturtle()
tracer(0, 0)
up()
goto(X, Y)
width(1)

print("\n")

for i in range(image_height):
    for j in range(image_width):
        random_color = f"#{randint(0, 255):02x}{randint(0, 255):02x}{randint(0, 255):02x}"
        
        color(random_color)
        down()
        forward(1)
        up()
        
        count += 1
        
        print(f"\rGenerating image... {round(count * 100 / (image_width * image_height), 2)}%", end="")
        
    goto(X, Y - (i + 1))

print("\n\nImage generation complete!")
done()        