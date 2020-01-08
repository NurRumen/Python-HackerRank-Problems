import os


def solve(s):
    sentence = s.split(sep=" ")
    new_sentence = []
    for each_string in sentence:
        new_sentence.append(each_string.capitalize())
    cap_str = " ".join(new_sentence)
    return cap_str


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
