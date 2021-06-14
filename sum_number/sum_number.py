def sum(number):
    if number == 0:
        return 0
    elif number > 0:
        result = number
        number -= 1
        result += sum(number)
        return result


print(sum(10))
