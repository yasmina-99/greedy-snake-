#importing the modules
import turtle
import time
import random
import os


each_step = 20
delay = 0.1  #the movement speed
candy_size = 15 
score = 0

# Setting window screen
screen = turtle.Screen()
screen.title("Greedy Snake")
screen.bgpic('/Users/leeeena/Desktop/Slide1.png')
screen.setup(800,800)
turtle.write(f"The instructions of this game are shown below: \n 1. Feed the snake with pink candies. \n 2. Do not touch the black traps or borders \n 3. Avoid colliding with your own tail!".format(score),align="center",font=("Courier", 20, "bold"))
turtle.hideturtle()
screen.bgpic("nopic")
time.sleep(8)
turtle.clear()
screen.bgcolor("beige")
screen.tracer(0)  #disable the animation


# Setting up snake head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("red")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Setting up Candy
candy = turtle.Turtle()
candy.speed(0) 
candy.shape("triangle") 
candy.color("pink")
candy.penup()
candy.goto(200, 250) #goto() sets to the absolute position


# Body of snake as list()
body = []

# Setting up the score
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.hideturtle() #if not hidden, the trap will show up
pen.goto(0, 300)
pen.write("Score : 0", align="center",
          font=("Calibri", 20, "bold"))

# Setting the trap on the screen 
trap = turtle.Turtle()
trap.speed(0) 
trap.shape("triangle")
trap.color("black")
trap.penup()
trap.goto(random.randrange(-390, 391), random.randrange(-390, 391))



# direction of head object 
def move_up():
    if head.direction != "down":
        head.direction = "up"

def move_down():
    if head.direction != "up":
        head.direction = "down"
        
def move_left():
    if head.direction != "right":
        head.direction = "left"

def move_right():
    if head.direction != "left":
        head.direction = "right"


def move_snake():
    if head.direction == "up":
         head.sety(head.ycor() + 20)
    elif head.direction == "down":
        head.sety(head.ycor() - 20)
    elif head.direction == "right":
        head.setx(head.xcor() + 20)
    elif head.direction == "left":
        head.setx(head.xcor() - 20)

# Keyboard settings 
turtle.listen()
turtle.onkeypress(move_left, "Left")
turtle.onkeypress(move_right, "Right")
turtle.onkeypress(move_up, "Up")
turtle.onkeypress(move_down, "Down")




##############################


# Main game loop
while True:
    screen.update()

    # game over when snake crosses a border
    if head.xcor() > 390 or head.xcor() < -390 or head.ycor() > 390 or head.ycor() <-390:
        time.sleep(1) # delay
        head.goto(0,0)
        head.direction = "stop" #game over
        
        for b in body:
            b.goto(1000,1000) # Hide
            
        body.clear() # clear body list() 
        score = 0    # reset score

        # score update 
        pen.clear() 
        pen.write("Score:{}".format(score),align="center",font=("Calibri", 20, "bold"))
    
        turtle.write("game over".format(score),align="center",font=("Arial", 40, "bold"))
        turtle.clear()
        time.sleep(2)
        turtle.hideturtle()


    # check for collision with candy
    if head.distance(candy) < 20: 
        # default turtle size: 20 
        # move to random location
        x = random.randint(-390,390) 
        y = random.randint(-390,390)
        candy.goto(x,y)
        
        #speed up 
        if head.distance(candy)<20:
            delay -= 0.005
        # append body as object 
        new_body = turtle.Turtle()
        new_body.speed() 
        new_body.shape("circle")
        new_body.color("green")
        new_body.penup()
        body.append(new_body)
        
        # add score
        score += 1
        pen.clear() # otherwise the old score would remain
        pen.write("Score:{}".format(score),align="center",
          font=("Calibri", 20, "bold"))

     #  body moves first (movement transmission to head)
    for i in range(len(body)-1, 0, -1):
        x = body[i-1].xcor()
        y = body[i-1].ycor()
        body[i].goto(x, y)
    
    # move the body 0 to the head
    if len(body) > 0:
        x = head.xcor()
        y = head.ycor()
        body[0].goto(x,y)
    
    
    move_snake()
    # check for self-collision  
    for b in body:
        if b.distance(head) < 20: # collision 
            time.sleep(1)
            head.goto(0,0) #re-start
            head.direction = "stop"

            # hide
            for b in body:
                b.goto(1000,1000)
            body.clear()
            #game_end(turtle.Turtle)

            # game over + restart
            score = 0 # update on screen
            pen.clear() 
            pen.write("Score:{}".format(score),align="center",font=("Calibri", 20, "bold"))
            turtle.write("game over".format(score),align="center",font=("Arial", 40, "bold"))
            turtle.clear()
            time.sleep(2)
            turtle.hideturtle()

    
    # collision with trap
    if head.distance(trap) < 20:
        time.sleep(1)
        head.goto(0,0)
        trap.hideturtle() 
        trap = turtle.Turtle() #new trap object 
        x = random.randint(-390,390)
        y = random.randint(-390,390)
        trap.goto(x,y) 
        trap.shape("triangle")
        trap.color("black")
        head.direction = "stop"
       

        trap.clear()
        time.sleep(0)
    
        # (- 2 points ) if the snake hits the trap 
        score = score - 2
        # screen update 
        pen.clear() 
        pen.write("Score:{}".format(score),align="center",font=("Calibri", 20, "bold"))
        

    time.sleep(delay)

   
turtle.done()

