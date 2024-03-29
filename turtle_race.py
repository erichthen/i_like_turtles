import turtle
import random

BG_COLOR = "orange"
turtle.Screen().bgcolor(BG_COLOR)

pen = turtle.Turtle()
pen.speed(0)
pen.penup()

def draw_border():
    pen.goto(-320, 140)
    pen.pendown()
    pen.forward(640)
    pen.right(90)
    pen.forward(330)
    pen.right(90)
    pen.forward(640)
    pen.right(90)
    pen.forward(330)
    pen.right(90)
    pen.penup()

def draw_title():
    pen.goto(0, 200)
    pen.write("TURTLE RACE", align="center", font=("Arial", 24, "bold"))

def celebration_spin(winner):
    for _ in range(180):
        winner.right(10)
    
def main():
  
  draw_border()
  draw_title()

  pen.goto(-320, 160)
  for _ in range(16):

      pen.right(90)
      pen.forward(20)
      pen.pendown()
      pen.forward(330)
      pen.penup()
      pen.backward(350)
      pen.left(90)
      pen.forward(40)

  pen.hideturtle()

  #this is our first turtle
  turtle_1 = turtle.Turtle()
  turtle_1.color("black")
  turtle_1.shape("turtle")
  turtle_1.penup()
  turtle_1.goto(-320, 100)
  turtle_1.speed(1)
  turtle_1.pendown()
  
  #this is our second turtle
  turtle_2 = turtle.Turtle()
  turtle_2.color("green")
  turtle_2.shape("turtle")
  turtle_2.penup()
  turtle_2.goto(-320, 40)
  turtle_2.speed(1)
  turtle_2.pendown()
  
  #third turtle
  turtle_3 = turtle.Turtle()
  turtle_3.color("red")
  turtle_3.shape("turtle")
  turtle_3.penup()
  turtle_3.goto(-320, -20)
  turtle_3.speed(1)
  turtle_3.pendown()
  
  #fourth turtle
  turtle_4 = turtle.Turtle()
  turtle_4.color("blue")
  turtle_4.shape("turtle")
  turtle_4.penup()
  turtle_4.goto(-320, -80)
  turtle_4.speed(1)
  turtle_4.pendown()
  
  turtle_5 = turtle.Turtle()
  turtle_5.color("cyan")
  turtle_5.shape("turtle")
  turtle_5.penup()
  turtle_5.goto(-320, -140)
  turtle_5.speed(1)
  turtle_5.pendown()
  
  turtle_1_progress = 0
  turtle_2_progress = 0
  turtle_3_progress = 0
  turtle_4_progress = 0
  turtle_5_progress = 0
  
  #run the race
  for i in range(205):
  
      turtle_1_steps = random.randint(1,5)
      turtle_1.forward(turtle_1_steps)
      turtle_1_progress += turtle_1_steps
  
      turtle_2_steps = random.randint(1,5)
      turtle_2.forward(turtle_2_steps)
      turtle_2_progress += turtle_2_steps
  
      turtle_3_steps = random.randint(1,5)
      turtle_3.forward(turtle_3_steps)
      turtle_3_progress += turtle_3_steps
  
      turtle_4_steps = random.randint(1,5)
      turtle_4.forward(turtle_4_steps)
      turtle_4_progress += turtle_4_steps
  
      turtle_5_steps = random.randint(1,5)
      turtle_5.forward(turtle_5_steps)
      turtle_5_progress += turtle_5_steps
  
  
  progress_list = [turtle_1_progress, turtle_2_progress, turtle_3_progress, 
                  turtle_4_progress, turtle_5_progress]

  winner = max(progress_list)

  if winner == turtle_1_progress:
      print("Turtle 1 (black) wins!\n")
      celebration_spin(turtle_1)
  elif winner == turtle_2_progress:
      print("Turtle 2 (green) wins!\n")
      celebration_spin(turtle_2)
  elif winner == turtle_3_progress:
      print("Turtle 3 (red) wins!\n")
      celebration_spin(turtle_3)
  elif winner == turtle_4_progress:
      print("Turtle 4 (blue) wins!\n")
      celebration_spin(turtle_4)
  else:
      print("There was a tie, that's crazy")
      
  for progress in progress_list:
      print(progress) #see how close it was

  turtle.Screen().exitonclick()



if __name__ == "__main__":
    main()




