from turtle import *
from random import randint
from PIL import Image
from datetime import datetime

print("\nWelcome to the Random Image Generator!\n\n")

image_width = int(input("Width: "))
image_height = int(input("Height: "))

X = image_width / -2
Y = image_height / 2

count = 0

setup(width=image_width, height=image_height)
title("Random Image Generator")  

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

print("\n\nImage generation complete!\n\n")

save_image = input("Do you want to save the image? (y/n): ").lower()

if save_image == "y":
    print("\nSaving image...\n")

    getscreen().getcanvas().postscript(file="image.eps")
    img = Image.open("image.eps")
    img.save(f"saved/RIG-{datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}.png", "png")
    
    print(f"\nImage saved successfully!\n")
elif save_image == "n":
    print("\nImage not saved.\n")
    exit()
else:
    print("\nInvalid input. Image not saved.\n")

done()        