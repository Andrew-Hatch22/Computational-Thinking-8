import random
import time
import turtle
from utils import create_sprite, set_background

window = turtle.Screen()

# Section 1 - Variables

x1 = -8
y1 = 4
x2 = -8
y2 = 3
x3 = -8
y3 = 2
x4 = -8
y4 = 1


# Section 2 - Setup
set_background("summer")
t1 = create_sprite("alien",x1,y1)
t2 = create_sprite("baseball",x2,y2)
t3 = create_sprite("cardinal2",x3,y3)
t4 = create_sprite("cat",x4,y4)


# # Section 3 - Racing
# # TODO - set how much each variable changes by and increase the number of repeats to at least 30
# # TODO - explain here which sprites are faster or slower
for i in range(30):
     x1 += random.randint(1,4)
     x2 += random.randint(2,3)
     x3 += 3
     x4 += random.randint(2,4)

     t1.goto(x1, y1)
     t2.goto(x2, y2)
     t3.goto(x3, y3)
     t4.goto(x4, y4)

     window.update()
     time.sleep(0.1)


# # Section 4 - Winner
# # TODO - complete the elif for player 2 winning
# # TODO - write another elif for player 3 and player 4
s5 = create_sprite("alien",-200,-200)
if x1 >= x2 and x1 >= x3 and x1 >= x4:
    s5.write("Player 1 wins!")
elif x2 >= x1 and x2 >= x3 and x2 >= x4:
    s5.write("Player 2 wins!")
elif x3 >= x1 and x3 >= x2 and x3 >= x4:
    s5.write("Player 3 wins!")
elif x4 >= x3 and x4 >= x2 and x4 >= x1:
    s5.write("Player 4 wins!")
  


turtle.exitonclick()
