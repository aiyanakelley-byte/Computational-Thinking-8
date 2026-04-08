import turtle, time, random
from utils import *

# Section 1 - Variables
# TODO - add starting values for all the variables
x1 = -300
y1 = 270
x2 = -300
y2 = 100
x3 = -300
y3 = 0
x4 = -300
y4 = -100


# Section 2 - Setup
# # TODO - use your own background, and set your four turtles to images of your choice
set_background("ocean3")
t1 = create_sprite("my-turtle",x1,y1)
t2 = create_sprite("seahorse",x2,y2)
t3 = create_sprite("shark",x3,y3)
t4 = create_sprite("starfish",x4,y4)


# # Section 3 - Racing
# # TODO - set how much each variable changes by and increase the number of repeats to at least 30
# # TODO - explain here which sprites are faster or slower
# sprite 1 will be the slowest based on the randomness of sprites 2-4, sprite 2 is the second slowest based on sprites 3-4, sprite 3 with be the second fastest based on the randomness of sprite 4, and sprite 4 would most likely be the fasted based on the randomness of spires 1-3 amd the givin amounts of speed. 
for i in range(30):
    x1 += random.randint(1,15)
    x2 += random.randint(4,18)
    x3 += random.randint(7,21)
    x4 += random.randint(10,24)

t1.goto(x1, y1)
t2.goto(x2, y2)
t3.goto(x3, y3)
t4.goto(x4, y4)

window.update()
time.sleep(0.1)


# # Section 4 - Winner
# # TODO - complete the elif for player 2 winning
# #TODO - write another elif for player 3 and player 4
s5 = create_sprite("Blob",-200,-200)
if x1 >= x2 and x1 >= x3 and x1 >= x4:
    s5.write("Player 1 wins!")
elif x2 >= x1 and x2 >= x3 and x2 >= x4:
    s5.write("player 2 wins!")


turtle.exitonclick()