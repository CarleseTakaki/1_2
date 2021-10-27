
# a121_catch_a_turtle.py

#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----
spot_color = "purple"
spot_size = int(2)
spot_shape = "circle"
a=0
b=400
c=0
d=300

#-----initialize turtle-----
spot = trtl.Turtle()

#-----game functions--------
spot.fillcolor(spot_color)
spot.shapesize(spot_size)
spot.shape(spot_shape)

def change_position ():
  new_xpos = rand.randint(a,b)
  new_ypos = rand.randint(c,d)
  spot.goto(new_xpos, new_ypos)

def spot_clicked(x,y):
  spot.hideturtle()
  spot.penup()
  change_position()
  spot.showturtle()
#-----events----------------
spot.onclick(spot_clicked)

wn=trtl.Screen ()
wn.mainloop ()