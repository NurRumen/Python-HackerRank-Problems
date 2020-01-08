def print_formatted(number):
    space_padding = len(bin(number).lstrip("0b"))
    for i in range(1, number+1):
        print(str(i).ljust(space_padding) + oct(i).lstrip("0o").ljust(space_padding) +
              hex(i).upper().lstrip("0X").ljust(space_padding) + bin(i).lstrip("0b").ljust(space_padding))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)