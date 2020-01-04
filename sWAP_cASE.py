def swap_case(s):
    swapped_cased_string = ""
    for i in s:
        if i.isupper():
            swapped_cased_string += str.lower(i)
        elif i.islower():
            swapped_cased_string += str.upper(i)
        else:
            swapped_cased_string += i
    return swapped_cased_string


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
