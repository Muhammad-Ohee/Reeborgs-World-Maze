def turn_right():
    turn_left()
    turn_left()
    turn_left()

# front_is_clear()
# wall_in_front()
# right_is_clear()
# wall_on_right()

loop = 0

while at_goal() != True:
    if right_is_clear() == True:
        turn_right()
        move()
        loop += 1
        if loop > 4:
            while front_is_clear() == True:
                move()
    elif front_is_clear() == True:
        move()
        loop = 0
    else:
        turn_left()
        loop = 0