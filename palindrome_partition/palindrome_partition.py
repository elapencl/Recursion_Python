def is_palindrome(string):
    reverse = string[::-1]
    if string.lower() == reverse.lower():
        return True
    else:
        return False


def partition(string, partitions, result) -> None:
    result.append(partitions+[string])
    for i in range(1, len(string)):
        partition(string[i:], partitions+[string[:i]], result)
    return result


def check_partitions(list_of_partitions):
    list_num_part = []
    list_partitions = []
    for item in list_of_partitions:
        n = 0
        y = 0
        for j in item:
            if is_palindrome(j):
                y += 1
            else:
                n += 1

        if n == 0:
            number_of_partitions = int(len(item))-1
            list_num_part.append(number_of_partitions)
            list_partitions.append(item)
    return list_num_part, list_partitions


def palindrome(string):
    resultt = partition(string,[],[])

    result_final = check_partitions(resultt)

    return result_final


a = 'geek'

print(palindrome(a))
