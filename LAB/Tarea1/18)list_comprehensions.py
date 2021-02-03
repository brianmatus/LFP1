if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    s = "["
    for i in range(0,x+1):
        for j in range(0,y+1):
            for k in range(0,z+1):
                if (i+j+k != n):
                    s = s +  "[" + str(i) + ", " + str(j) + ", " + str(k) + "], "
    if (len(s) > 1):
        s = s[0:len(s)-2]
    s = s + "]"
    print(s)
