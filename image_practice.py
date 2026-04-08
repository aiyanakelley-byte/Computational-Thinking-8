# Section 1 - Your code
from utils import *
set_background("summer")

s1 = create_sprite("nani", 99, 99)
s2 = create_sprite("lilo", -88, 70)
s2 = create_sprite("stich", -32, -70)
s2 = create_sprite("turtle3", 60, -38)

message1 = create_sprite("alien",-200,200)
message1.color("orange")
message1.write("your fav image?",font = ("Arial", 40, "normal"))
message1.hideturtle()


######################################################################


# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()