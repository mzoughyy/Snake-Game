import turtle

def go_up(head):
    if head.direction != "down":
        head.direction = "up"

def go_down(head):
    if head.direction != "up":
        head.direction = "down"

def go_left(head):
    if head.direction != "right":
        head.direction = "left"

def go_right(head):
    if head.direction != "left":
        head.direction = "right"

def move(head, wn):
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

    # Get the current position of the snake head
    x = head.xcor()
    y = head.ycor()

    # Define the image boundaries
    min_x, max_x = -290, 290
    min_y, max_y = -290, 290

    # Check if the snake head is outside the image boundaries
    if x <= min_x or x >= max_x or y <= min_y or y >= max_y:
        # Snake dies
        wn.bye()
