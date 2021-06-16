def partition(string,substrings,result):
    result.append(substrings + [string])
    for i in range(1, int(len(string))):
        partition(string[i:],substrings + [string[:i]],result)
    return result


def check_letters(string):
    lista = []
    substrings = partition(string,[],[])
    for item in substrings:
        for j in item:
            print(f"j is {j}")
            if j[0] == j[int(len(j))-1]:
                if j not in lista:
                    lista.append(j)
    return lista


print(check_letters('abac'))
