def check_palindrome(any_string):
    string = str(any_string)
    reverse = string[::-1]
    if string == reverse:
        return True
    else:
        return False


print(check_palindrome('nursesrun'))
