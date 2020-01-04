def mutate_string(string, position, character):
    listed_string = list(string)
    listed_string[position] = character
    resultant_string = ''.join(listed_string)
    return resultant_string


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
