def move_tower(number, source, target, aux):
    if number > 0:
        print("move tower of height " + str(number) + " from " + source + " to " + target )
        move_tower(number-1, source, aux, target)
        move_disk(source,target)
        move_tower(number-1, aux, target, source)


def move_disk(pole_one, pole_two):
    print("move disk from " + pole_one + " to " + pole_two)


move_tower(2, '1','3','2')
