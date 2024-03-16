import turtle


def square(t, side_length, fill_color):
    
    t.pensize(20)
    t.penup()
    t.goto(-side_length / 2, side_length / 2)  
    t.pendown()
    t.color("black", fill_color) 
    t.begin_fill()
    for _ in range(4):
        t.forward(side_length)
        t.right(90)
    t.end_fill()
    t.penup()



def starry_eye(t, colors):

    t.showturtle()
    initial_size = 100
    t.pendown()
    
    #recursive to expand
    for i in range(150):
        t.color(colors[i % 6])
        t.forward(initial_size + i)
        t.left(150)

    t.hideturtle()
    t.penup()
    t.goto(-210, 100)



def mouth(t, bradius, radius, colors):
    
    #black semi
    t.penup()
    t.goto(-200,-70)
    t.color("black")
    t.begin_fill()
    t.setheading(270)  
    t.circle(bradius, 180)  
    t.left(90)
    t.forward(bradius * 2)
    t.left(90)
    t.end_fill()
    

    # stripes
    t.width(2)
    t.penup()
    t.goto(-130,-110)
    
    vertical_offset = -80

    for x in range(-radius, radius, 4): 
        t.penup()
        t.goto(x, 0 + vertical_offset)  #v offset made to move whole thing dow 
        t.pendown()
        t.color(colors[(x + radius) // 4 % len(colors)])  
        t.goto(x, -abs((radius**2 - x**2)**0.5) + vertical_offset)  #semicircle math 

    t.penup()



                #i.e. radius
def pupils(t, pupil_dilation): 
    
    def pupil(x, y): 
        t.penup()
        t.goto(x, y - pupil_dilation)  
        t.pendown()
        t.color("black")
        t.begin_fill()
        t.circle(pupil_dilation)
        t.end_fill()
        t.penup()

    pupil(-168,132)  
    pupil(132, 133) 



def main():
  
  
  colors = ["red", "orange", "yellow", "green", "blue", "purple"]

  facecolor = "light blue"

  pen = turtle.Turtle()
  pen.speed("fastest")
  turtle.colormode(255)
  turtle.bgcolor((204, 51, 153))  
  
  square(pen, 600, facecolor)

  pen.pensize(2)

  pen.goto(-200, 100)

  starry_eye(pen, colors)

  pen.goto(200, 128)

  starry_eye(pen, colors) 

  pen.penup()
  pen.goto(-150, -100)  
  pen.pendown()

  mouth(pen, 200, 180, colors)
  
      
  pupils(pen, 20)

  pen.hideturtle()
  turtle.done()




if __name__ == "__main__":
   main()