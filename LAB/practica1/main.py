from easygui import fileopenbox
#egdemo()


def main():
    while(True):

        print("Bienvenido al programa de practica 1 de LFP")
        print("1. Cargar archivo de entrada")
        print("2. Desplegar listas ordenadas")
        print("3. Desplegar busquedas")
        print("4. Desplegar todas")
        print("5. Desplegar todas a archivo")
        print("6. Salir")

        option = input("Ingrese la opcion deseada \n")
        if(option == "1"):
            open_file()



        elif(option == "2"):
            print("2")
        elif(option == "3"):
            print("3")
        elif(option == "4"):
            print("4")
        elif(option == "5"):
            print("5")
        elif(option == "6"):
            print("Adios :D")
            exit()
        else:
            "No has ingresado una opcion valida, intentalo otra vez"





def open_file():
    file = fileopenbox("Python files", "Open files", default="*.txt")
    print(f'Se selecciono el archivo {file}')
    file1 = open(file, 'r')
    Lines = file1.readlines()

    #megaArrays = []
    #for i in range(0,len(Lines)):
    #    megaArrays = megaArrays + [Lines[i],"a","b"]



    for line in Lines:
        equalI = line.index("=")
        letterI = len(line)
        print("Equal Index:" + str(equalI))

        for i in range(equalI,len(line)):
            if (line[i].isalpha()):
                print("First letter index:" + str(i))
                letterI = i
                break

    


if __name__ == '__main__':
    main()
