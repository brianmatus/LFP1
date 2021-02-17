from easygui import fileopenbox

# egdemo()


# [name, unordered[], ordered[], itemSearched, indexesFound[], boolOrd, boolSearch]
Lines = []
megaArrays = []
empty_string = "---"


def main():
    while True:

        print("---------------------------------------------")
        print("Bienvenido al programa de practica 1 de LFP")
        print("1. Cargar archivo de entrada")
        print("2. Desplegar listas ordenadas")
        print("3. Desplegar busquedas")
        print("4. Desplegar todas")
        print("5. Desplegar todas a archivo")
        print("6. Salir")
        print("---------------------------------------------")

        # open_file()#TODO debug only, delete

        option = input("Ingrese la opcion deseada \n")
        if (option == "1"):
            open_file()
            # print(str(megaArrays))
        elif (option == "2"):
            for result in megaArrays:
                if (result[5]):
                    print(result[0] + "ORDENADA -> " + str(result[2]))
        elif (option == "3"):
            for result in megaArrays:
                if (result[6] == True):
                    if (len(result[4])) > 1:
                        print(result[0] + "  " + str(result[1]) + "---->DATO " + str(
                            result[3]) + " encontrado en indice(s) " + str(result[4]))
                    else:
                        print(result[0] + "  " + str(result[1]) + "---->DATO " + str(
                            result[3]) + " no se encontro en ninguna posicion")
        elif (option == "4"):
            for result in megaArrays:
                if (result[5]):
                    print(result[0] + "ORDENADA -> " + str(result[2]))

                if (result[6] == True):
                    if (len(result[4])) > 1:
                        print(result[0] + "  " + str(result[1]) + "---->DATO " + str(
                            result[3]) + " encontrado en indice(s) " + str(result[4]))
                    else:
                        print(result[0] + "  " + str(result[1]) + "---->DATO " + str(
                            result[3]) + " no se encontro en ninguna posicion")
        elif (option == "5"):
            save_html()
        elif (option == "6"):
            print("Adios :D")
            exit()
        else:
            "No has ingresado una opcion valida, intentalo otra vez"


def open_file():
    file = fileopenbox("Python files", "Open files", default="*.txt") #TODO descomentar
    print(f'Se selecciono el archivo {file}') #TODO descomentar
    #file = "C:\\Users\\Matus\\Documents\\USAC\\LFP1\\LAB\\practica1\\test.txt"  # TODO Only for debug, delete
    file1 = open(file, 'r')
    global Lines
    Lines = file1.readlines()

    for i in range(0, len(Lines)):
        Lines[i] = Lines[i].replace("\n", "")

    for line in Lines:
        # print("-----")
        # !Index of Equal sign
        equalI = line.index("=")
        letterI = len(line)
        # print("Equal Index:" + str(equalI))

        # !Index of First letter after data (referencing first command, if any)
        for i in range(equalI, len(line)):
            if (line[i].isalpha()):
                letterI = i
                # print("First letter index:" + str(letterI))
                break

        # Separating part of string to pertinent unparsed variables
        name = line[:equalI]
        _data = line[equalI + 1:letterI].replace(" ", "")
        _commands = line[letterI:].split(",")

        unordered = list(map(int, _data.split(",")))

        # print("UNORDERED LIST:" + str(unordered))

        ordered, numberSearched, indexesFound = [None] * 3
        requestedOrdering, requestedSearch = [False] * 2

        for _com in _commands:
            com = _com.replace(" ", "").upper()

            # !Searching
            searchWord = "BUSCAR"
            if com.find(searchWord) != -1:
                requestedSearch = True

                # Search
                numberSearched = int(com[len(searchWord):])
                # print("Number to search is:" + str(numberSearched))
                indexesFound = []
                for i in range(0, len(unordered)):
                    if unordered[i] == numberSearched:
                        indexesFound = indexesFound + [i]

            # !Ordering
            orderingWord = "ORDENAR"
            if com.find(orderingWord) != -1:
                # print("Ordering requested")
                requestedOrdering = True
                ordered = orderArray(unordered).copy()
                # print("Ordered:" + str(ordered))

        if ordered is None:
            # print("Order not needed, making copy")
            ordered = unordered.copy()

        # [name, unordered[], ordered[],           itemSearched, indexesFound[], requestedOrdering, requestedSearch]
        newOne = [name, unordered, ordered, numberSearched, indexesFound, requestedOrdering, requestedSearch]
        # print("NEW ONE: " + str(newOne))
        megaArrays.append(newOne)
        # print(str(unordered))
        # print(ordered)

def save_html():
    table = [["Titulo", "Datos", "Ordenados", "Busqueda", "Resultados Busqueda"]]
    for result in megaArrays:
        new = [result[0], result[1], result[2], result[3], result[4]]
        if not result[5]: #5:Requested ordering
            new[2] = empty_string
        if not result[6]:
            new[3] = empty_string
            new[4] = empty_string
        else:
            if len(new[4]) == 0:
                new[4] = "No encontrado"
        table.append(new)
    for l in table:
        print(str(l))
    html_table = tableToHTML(table)
    print(html_left + html_table + html_right)

    with open('index.html', 'a') as the_file:
        the_file.write(html_left + html_table + html_right)

def tableToHTML(data):
    q = "<table>\n"
    for i in [(data[0:1], 'th'), (data[1:], 'td')]:
        q += "\n".join(
            [
                "<tr>%s</tr>" % str(_mm)
                for _mm in [
                "".join(
                    [
                        "<%s>%s</%s>" % (i[1], str(_q), i[1])
                        for _q in _m
                    ]
                ) for _m in i[0]
            ]
            ]) + "\n"
    q += "</table>"
    return q


def orderArray(theArray):
    n = len(theArray)
    arr = theArray.copy()

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr




html_left = '''  <!DOCTYPE html> <html lang="en"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"> 	<title>Resultados Practica LFP</title> 	<meta name="viewport" content="width=device-width, initial-scale=1"> 	<link rel="icon" type="image/png" href="file:///C:/Users/Matus/Downloads/fixed-column-table/Table_Fixed_Column/images/icons/favicon.ico"> 	<link rel="stylesheet" type="text/css" href="./bootstrap.min.css"> 	<link rel="stylesheet" type="text/css" href="./main.css"> </head> <body> 	<div class="limiter"> 	<div class="container-table100"> <div class="wrap-table100"> <div class="table100 ver1"> <div class="table100"> '''
html_right = '''</div></div></div></div></div></body></html>'''


if __name__ == '__main__':
    main()
