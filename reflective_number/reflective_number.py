def reflect(number):
    if number > 0:
        print(number, end=" ")
        reflect(number-1)
        print(number, end=" ")
    elif number == 0:
        print(number, end=' ')


reflect(3)
