def turn_right():
    for i in range(3):
        turn_left()
def jump():
    turn_left()
    move()
    aux = 0
    enable = 0
    while wall_on_right() == True:
        move()
        aux += 1
        enable = 1
    for i in range(2):
        turn_right()
        move()
    if enable == 1:
        for i in range(aux):
            move()
    turn_left()
while not at_goal() == True:
    if front_is_clear() == True:
        move()
    else:
        jump()
