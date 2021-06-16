def make_binary(number):
    if number == 0:
        return 0
    elif number > 0:
        make_binary(number//2)
    print(number%2,end="")


make_binary(21)
