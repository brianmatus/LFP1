import textwrap
def wrap(string, max_width):
    s = ""
    aux = 0
    for c in string:
        s = s + c
        aux = aux + 1;
        if (aux == max_width):
            s = s + "\n"
            aux = 0
    return s

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
