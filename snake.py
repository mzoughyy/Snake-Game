import turtle
import time
from snakeHead import create_snake_head
from food import move_food
from snake_function import go_up, go_down, go_left, go_right, move
import random

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.register_shape("background.png", (1000, 800))
wn.bgpic("background.png")
wn.setup(width=800, height=600)
wn.tracer(0)  # Turns off screen updates

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Segments
segments = []

# Function to move the snake head
def move_snake():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Function to check if snake collides with wall
def snake_collides_with_wall():
    x = head.xcor()
    y = head.ycor()
    if x > 290 or x < -290 or y > 290 or y < -290:
        return True
    return False

segments.clear()

# Score
score = 0

# Score display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("black")
score_display.penup()
score_display.hideturtle()
score_display.goto(-380, 230)
score_display.write("Score: {}".format(score), align="left", font=("Arial", 24, "normal"))
    
# Function to check for collision with the food
def check_collision():
    global score
    if head.distance(food) < 20:
        # Move food to a random location
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
        # Increase the score
        score += 1
        # Update the score display
        score_display.clear()
        score_display.write("Score: {}".format(score), align="left", font=("Arial", 24, "normal"))

# Keyboard bindings
wn.listen()
wn.onkeypress(lambda: go_up(head), "Up")
wn.onkeypress(lambda: go_down(head), "Down")
wn.onkeypress(lambda: go_left(head), "Left")
wn.onkeypress(lambda: go_right(head), "Right")

# Function to display game over screen
def game_over():
    # Clear the screen
    wn.clear()

    # Display the "You died" image
    wn.bgpic("gameover.png")

    # Create the restart button
    restart_btn = turtle.Turtle()
    restart_btn.speed(0)
    restart_btn.shape("square")
    restart_btn.color("white")
    restart_btn.penup()
    restart_btn.goto(0, -200)

    # Function to restart the game
    def restart_game():
        # Clear the screen
        wn.clear()

        # Reinitialize the game
        head.goto(0, 0)
        head.direction = "stop"
        food.goto(0, 100)
        segments.clear()
        score = 0
        score_display.clear()
        score_display.write("Score: {}".format(score), align="left", font=("Arial", 16, "normal"))

        # Start the game loop again
        game_loop()

    # Bind the restart_game() function to the restart button
    restart_btn.onclick(restart_game)

# Main game loop
def game_loop():
    while True:
        wn.update()

        # Check for collision with the food
        if head.distance(food) < 20:
            # Move food to a random location
            x = random.randint(-290, 290)
            y = random.randint(-290, 290)
            food.goto(x, y)

        move_snake()

        # Check if the snake dies
        if snake_collides_with_wall():
            game_over()

        check_collision()

        time.sleep(0.1)

# Start the game loop
game_loop()
wn.mainloop()
