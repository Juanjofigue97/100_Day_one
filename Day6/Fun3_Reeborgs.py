def turn_right():
    for i in range(3):
        turn_left()
def jump():
    turn_left()
    move()
    for i in range(2):
        turn_right()
        move()
    turn_left()
while not at_goal() == True:
    if front_is_clear() == True:
        move()
    else:
        jump()

