def fact(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        result = number*fact(number-1)
        return result

print(fact(3))
