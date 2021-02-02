def print_rangoli(size):
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    final = ""

    spacingSize = 4*size -3
    #print(str(spacingSize))


    for i in range(0,size):
        s = alphabet[size-i-1]
        for j in range(i+1,1,-1):
            s = alphabet[size-j+1] + "-" + s + "-" + alphabet[size-j+1]


        #s = "-"*int((spacingSize-len(s))/2) + s + "-"*int((spacingSize-len(s))/2)
        final = final + s + "\n"

    for i in range(0,size):
        s = s[  0:int(              (len(s)-1)/2 -2       )    ] + s[int(                      (len(s)+1)/2+1):]
        #s = "-"*int((spacingSize-len(s))/2) + s + "-"*int((spacingSize-len(s))/2)


        final = final + s + "\n"

    final = final[0:len(final)-2] #Remove last \n

    #print(final)


    finalWithSpacing = ""

    for line in final.split("\n"):
        finalWithSpacing = finalWithSpacing +  "-"*int((spacingSize-len(line))/2) + line + "-"*int((spacingSize-len(line))/2) + "\n"

    finalWithSpacing = finalWithSpacing[0:len(finalWithSpacing)-1] #Remove last \n

    print(finalWithSpacing)



if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
