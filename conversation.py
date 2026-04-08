# Section 1 - Your code
from utils import *
player_name = input("What is your name?    ")

set_background("candy_land.gif")

TW = create_sprite("Tiddlewink", -200, 0)
FM = create_sprite("Finklemiten", 200, 0)

TW.color("teal")
FM.color("dark red")
time.sleep(5)

TW.write("Where are we?",font = ("Arial", 20, "normal"))
window.update()
time.sleep(1)

TW.clear()
window.update()
time.sleep(1)

FM.write("On the moon!",font = ("Arial", 20, "normal"))
window.update()
time.sleep(1)

FM.clear()
window.update()
time.sleep(1)

TW.write(f"I'm looking for {player_name}",font = ("Arial", 20, "normal"))
window.update()
time.sleep(1)

TW.clear()
TW.write("Have you seen them?",font = ("Arial", 20, "normal"))
window.update()
time.sleep(1)

######################################################################
# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()