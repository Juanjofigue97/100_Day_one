# Hurdle 1

def turn_right():
    for i in range(3):
        turn_left()
num = 6
while num>0:
    move()
    turn_left()
    move()
    for i in range(2):
        turn_right()
        move()
    turn_left()
    if at_goal() == True:
        num -= 1
