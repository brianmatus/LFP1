if __name__ == '__main__':
    n = int(input())
    _arr = map(int, input().split())
    arr = []
    for a in _arr:
        _a = [a]
        arr = arr + _a

    minimun = 0
    for a in arr:
        if a < minimun:
            minimun = a

    first = minimun
    second = minimun

    for a in arr:
        #print("examining" + str(a))
        if a>first:
            #print("first: " + str(a) + " is greater than " + str(first))
            second = first

            first = a

            #print("first is now " + str(first))
            #print("second is now " + str(second))

            continue
        if (a>second and a!= first):
            #print("second: " + str(a) + " is greater than " + str(first))
            second = a
            #print("second is now " + str(second))
            continue
    #print(first)
    print(second)
