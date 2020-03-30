#!/usr/bin/env python3

# Simple Snake game

# Imports
import turtle
import time
import random
 

# Score
score = 0.0
high_score = 0

# Speed of Gameloop
delay = 0.1
#delay = 0.1 - score/100.0


# Set up the Screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0) # Turn off Screen-Updates


###########################################################################
# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"


# Snake segments
segments = []


# Snakefood
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))


###########################################################################
# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
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


###########################################################################
# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")


###########################################################################
# Main Game-Loop
while True:
    wn.update()

    # No border collision, spawn at oponent side
    if head.xcor() > 290:
        x = head.xcor()
        y = head.ycor()
        head.goto(x - 600, y)
    elif head.xcor()<-290:
        x = head.xcor()
        y = head.ycor()
        head.goto(x + 600, y)
    elif head.ycor()>290:
        x = head.xcor()
        y = head.ycor()
        head.goto(x, y - 600)
    elif head.ycor()<-290:
        x = head.xcor()
        y = head.ycor()
        head.goto(x, y + 600)


    # Check for a collision with the border
#    if head.xcor() > 290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
#        time.sleep(1)
#        head.goto(0, 0)
#        head.direction = "stop"

        # Hide the segments
#        for segment in segments:
#             segment.goto(1000, 1000)

        # Clear the segments list
#        segments.clear()

        # Reset the Score
#        score = 0
#        pen.clear()
#        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))



    # Check for a Collision with the food
    if head.distance(food) < 25:

        # Move the food to random spot on the screen
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)
        for segment in segments:
            if food.distance(segment) < 40:
                food.goto(2000, 2000)
            elif food.distance(segment) > 1200:
                x = random.randint(-290, 290)
                y = random.randint(-290, 290)
                food.goto(x,y)

                
                

#        x = random.randint(-290, 290)
#        y = random.randint(-290, 290)
#        food.goto(x,y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Increase the score
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # Move the end segments first in reverse
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)


    move()

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the segments list
            segments.clear()

            # Reset the Score
            score = 0
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))


    time.sleep(delay - score/10000.0)

wn.mainloop()