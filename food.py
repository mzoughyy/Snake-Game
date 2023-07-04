import turtle
import random

def move_food(food):
    x = random.randint(-290, 290)
    y = random.randint(-290, 290)

    # Check if the food position is within the image bounds
    while not (-290 < x < 290 and -290 < y < 290):
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)

    food.goto(x, y)
