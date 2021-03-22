from TDA import *
from Elements import *
# from xml.dom import minidom
# from graphviz import Digraph
from easygui import fileopenbox

menu_string, order_string = " ", " "

restaurant = Restaurant("", LinkedList())
order = Order("", "", "", "", LinkedList())

error_list = LinkedList()
token_list = LinkedList()

restaurant_word = "restaurante"


def main():
    while True:

        print("---------------------------------------------")
        print("Proyecto 1 - LFP")
        print("LFP-A+ 1S2021, Brian Matus 201801290")
        print("1. Cargar menu")
        print("2. Cargar orden")
        print("3. Generar menu")
        print("4. Generar factura")
        print("5. Generar Árbol")
        print("6. Salir")
        print("7. Imprimir Estructura Interna")
        print("---------------------------------------------")
        debug_load()
        option = input("Ingrese la opción deseada \n")
        if option == "1":
            open_menu()
        elif option == "2":
            open_order()
        elif option == "3":
            load_menu()
        elif option == "4":
            load_order()
            pass
        elif option == "5":
            pass
        elif option == "6":
            print("Adios :D")
            exit()
        elif option == "7":
            print_structure()
        elif option == "0":
            debug_load()
        else:
            "No has ingresado una opción valida, inténtalo otra vez"


def print_structure():
    print("************************************************************************************")
    print("************************************************************************************")
    for c in restaurant.categories:
        print(f'--------------Category name:{c.name}------------')
        for p in c.elements:
            print(f'id:{p.name} name:{p.real_name} price:{p.price} description:{p.description}')

    print("************************************************************************************")
    print("************************************************************************************")
    for error in error_list:
        print(f'row={error.row} index={error.index} msg={error.msg}')

    print("************************************************************************************")
    print("************************************************************************************")
    for el in token_list:
        print(f'row={el.row} index={el.i} token={el.token} lex={el.lex}')

    print("************************************************************************************")
    print("************************************************************************************")
    print(f'Order client:{order.client_name}')
    print(f'Order address:{order.address}')
    print(f'Order nit:{order.nit}')
    print(f'Order tip:{order.tip}')
    for p in order.shopped_products:
        print(f'Quantity:{p.quantity}  Name:{p.name}')


def load_menu():

    global menu_string
    global restaurant

    # print(menu_string)

    global_i, local_i, row = 0, 1, 1

    nombre_id, global_i, local_i, row = afd_id_eq(menu_string, global_i, local_i, row)

    print(f'Nuevo i(global): {global_i}')
    print(f'Nuevo row: {row}')
    print(f'Nuevo i(local): {local_i}')

    print(f'load_menu:::nombre_id reconocida:{nombre_id}')

    if nombre_id.lower() == restaurant_word:
        name, global_i, local_i, row = afd_chain(menu_string, global_i, local_i, row)

        print(f'Nuevo i(global): {global_i}')
        print(f'Nuevo row: {row}')
        print(f'Nuevo i(local): {local_i}')

        print(f'load_menu:::nombre_restaurante reconocida: {name}')

        restaurant = Restaurant(name, LinkedList())

        # Se debe iniciar si o si con una sección, el resto se usa afd_section_or_product repetidas veces
        section_name, global_i, local_i, row = afd_section(menu_string, global_i, local_i, row)
        print(f'load_menu:::section_name reconocida: {section_name}')
        restaurant.categories.insert(Category(section_name, LinkedList()))

        last_section = section_name

        # Hasta que sigan habiendo secciones/productos
        while global_i < len(menu_string):
            # Analizar sección

            next_type, global_i, local_i, row = afd_section_or_product(menu_string, global_i, local_i, row)

            print(f'load_menu:::type reconocida: {next_type}')

            if next_type == "Section":
                section_name, global_i, local_i, row = afd_section(menu_string, global_i, local_i, row)
                print(f'load_menu:::section_name reconocida: {section_name}')

                #

                restaurant.categories.insert(Category(section_name, LinkedList()))
                last_section = section_name
            elif next_type == "Product":

                product_data, global_i, local_i, row = afd_product(menu_string, global_i, local_i, row)

                restaurant.categories.get(last_section).elements.insert(Product(*product_data))

                pass
            elif next_type == "End":
                print(f'load_menu:::Carga de datos de menu completa, no mas datos por cargar')
            else:
                print(f'load_menu:::signo no reconocido o fin inesperado: {next_type}')

    else:
        print(f'Resultado de id inicial, {nombre_id}, comando no reconocido')
        return


def load_order():
    global order_string
    global order

    # print(menu_string)

    global_i, local_i, row = 0, 1, 1

    data, global_i, local_i, row = afd_order_data(order_string, global_i, local_i, row)
    order.client_name = data[0]
    order.nit = data[1]
    order.address = data[2]
    order.tip = data[3]

    global_i += 1  # initial \n
    print(f'load_order:::data reconocida: {data}')
    while global_i < len(order_string):
        data, global_i, local_i, row = afd_product_buy(order_string, global_i, local_i, row)
        # global_i += 1
        print(f'load_order:::product reconocida: {data}')
        print(f'substring at {global_i}: {order_string[global_i:]}')
        order.shopped_products.insert(ShoppedProduct(data[1], data[0]))


def afd_product_buy(s, _i, i, row):
    buffer = []
    state = 0
    diff = 0

    print(f'afd_product_buy:::analyzing at _i={_i} row={row} i={i}:  {s[_i:]}')

    for _c in list(s[_i:]):
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        c = ord(_c)
        print(f'afd_product_buy:::state = {state} row={row} i={i} {c}:{_c}')
        if state == 0:
            print(f'afd_product_buy:::diff es: {diff} _i:{_i} row:{row} i:{i} ')
            if diff == 0:
                pre = _i
                quantity, post, i, row = afd_integer_comma(s, _i, i, row)
                diff = post - pre  # -1 for ;
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(f'afd_product_buy:::state = {state}  quantity reconocida: {quantity} con diff={diff}')
                print(f'afd_product_buy:::state = {state} _i={_i} row={row} i={i} substring is {s[pre+diff:]}')
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                buffer.append(quantity)
            elif diff > 2:
                diff -= 1
            elif diff == 2:
                diff = 0
                # i += 1
                # print(f'afd_product_buy:::state = {state}  cambiando estado a 1 con _i={_i} row={row} i={i}')
                state = 1

        elif state == 1:
            # print(f'afd_order_data:::diff es: {diff} _i:{_i}  i:{i} row:{row}')
            if diff == 0:
                print("initial, diff 0")
                pre = _i
                product_id, post, i, row = afd_id_ln(s, _i, i, row)
                diff = post - pre  # -1 for ;
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(f'afd_product_buy:::state = {state}  product_id reconocida: {product_id}')
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                buffer.append(product_id)
            elif diff > 1:
                diff -= 1
            elif diff == 1:
                # diff = 0  #TODO uncomment, it was just to comply with compiler
                # i += 1
                _i += 1
                return buffer, _i, i, row
        _i += 1


def afd_integer_comma(s, _i, i, row):
    buffer = ""
    state = 0
    first_i = i

    # print(f'afd_integer_comma:::string to analyze: {s[_i:]}')

    for _c in list(s[_i:]):
        c = ord(_c)
        print(f'afd_integer_comma:::state = {state} row={row} i={i} {c}:{_c}')

        if state == 0:
            if 48 <= c <= 57:  # 0-9
                first_i = i
                i += 1
                buffer += _c

            elif c == 10:  # \n
                i = 1
                row += 1
                report_error(i, row, f'afd_integer_comma:::state = {state} Se esperaba [0-9] , se encontró "{_c}"')

            elif c == 32 or c == 9:  # tab space
                i += 1

            elif c == 44:  # ,
                i += 1
                _i += 1

                print(f'comma at row={row} i={i}')
                report_token(first_i, row, buffer, "integer")
                return buffer, _i, i, row

            else:
                # i += 1
                _i += 1
                report_error(i, row, f'afd_integer_comma:::state = {state} Se esperaba [0-9] , se encontró "{_c}"')
        _i += 1


def afd_id_ln(s, _i, i, row):
    # global menu_string
    buffer = ""
    state = 0
    first_i = i

    # print(f'afd_id_ln:::string to analyze: {s[_i:]}')

    for _c in list(s[_i:]):
        c = ord(_c)
        print(f'afd_id_ln:::state = {state} row={row} i={i} {c}:{_c}')

        if state == 0:

            if c == 10:  # \n
                i = 1
                row += 1
                report_error(i, row, f'afd_id_ln:::state = {state} \\n antes de tiempo, Se esperaba id')

            elif 97 <= c <= 122:
                first_i = i
                i += 1
                buffer += _c
                state = 1

            elif c == 32 or c == 9:  # tab space
                i += 1

            else:
                i += 1
                report_error(i, row, f'afd_id_ln:::state = {state} Se esperaba a-z, se encontró "{_c}"')

        elif state == 1:
            if (48 <= c <= 57) or (65 <= c <= 90) or (97 <= c <= 122) or c == 95:
                i += 1
                buffer += _c

            elif c == 10:  # \n
                i = 1
                row += 1
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(f'afd_id_eq:::final:{buffer}')
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                report_token(first_i, row, buffer, "id")
                return buffer, _i, i, row


            elif c == 32 or c == 9:  # tab space
                i += 1

            else:
                report_error(i, row, f'afd_id_ln:::state = {state} Se esperaba [id], se encontró "{_c}"')
                i += 1
        _i += 1


def afd_order_data(s, _i, i, row):
    client_name, nit, address, tip = "", "", "", ""
    buffer = []
    state = 0
    diff = 0

    for _c in list(s[_i:]):
        c = ord(_c)
        # print(f'afd_order_data:::state = {state} row={row} i={i} {c}:{_c}')
        if state == 0:
            # print(f'afd_order_data:::diff es: {diff} _i:{_i}  i:{i} row:{row}')
            if diff == 0:
                pre = _i
                client_name, post, i, row = afd_chain(s, _i, i, row)
                diff = post - pre - 1  # -1 for ;
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(f'afd_order_data:::state = {state}  client_name reconocida: {client_name}')
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                buffer.append(client_name)
            elif diff > 1:
                diff -= 1
            elif diff == 1:
                diff = 0
                # print(f'afd_order_data:::state = {state} last to jump')
                i += 1
                state = 1

        elif state == 1:
            if c == 10:  # \n
                i = 1
                row += 1
            elif c == 32 or c == 9:  # space tab
                i += 1
            elif c == 44:  # ,
                i += 1
                state = 2
            else:
                report_error(i, row, f'afd_order_data:::state = {state} Se esperaba "," , se encontró "{_c}"')

        elif state == 2:
            # print(f'afd_order_data:::diff es: {diff} _i:{_i}  i:{i} row:{row}')
            if diff == 0:
                pre = _i
                print("the pre pre pre " + str(pre))
                nit, post, i, row = afd_chain(s, _i, i, row)
                diff = post - pre - 1  # -1 for ;
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(f'afd_order_data:::state = {state}  nit reconocida: {nit}')
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                buffer.append(nit)
            elif diff > 1:
                diff -= 1
            elif diff == 1:
                diff = 0
                # print(f'afd_order_data:::state = {state} last to jump')
                i += 1
                state = 3

        elif state == 3:
            if c == 10:  # \n
                i = 1
                row += 1
            elif c == 32 or c == 9:  # space tab
                i += 1
            elif c == 44:  # ,
                i += 1
                state = 4
            else:
                report_error(i, row, f'afd_order_data:::state = {state} Se esperaba "," , se encontró "{_c}"')

        elif state == 4:
            # print(f'afd_order_data:::diff es: {diff} _i:{_i}  i:{i} row:{row}')
            if diff == 0:
                pre = _i
                address, post, i, row = afd_chain(s, _i, i, row)
                diff = post - pre - 1  # -1 for ;
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(f'afd_order_data:::state = {state}  address reconocida: {address}')
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                buffer.append(address)
            elif diff > 1:
                diff -= 1
            elif diff == 1:
                diff = 0
                # print(f'afd_order_data:::state = {state} last to jump')
                i += 1
                state = 5

        elif state == 5:
            if c == 10:  # \n
                i = 1
                row += 1
            elif c == 32 or c == 9:  # space tab
                i += 1
            elif c == 44:  # ,
                i += 1
                state = 6
            else:
                report_error(i, row, f'afd_order_data:::state = {state} Se esperaba "," , se encontró "{_c}"')

        elif state == 6:
            # print(f'afd_order_data:::diff es: {diff} _i:{_i}  i:{i} row:{row}')
            if diff == 0:
                pre = _i
                tip, post, i, row = afd_number_percentage(s, _i, i, row)
                diff = post - pre - 1  # -1 for ;
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(f'afd_order_data:::state = {state}  tip reconocida: {tip}')
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                buffer.append(tip)
            elif diff > 1:
                diff -= 1
            elif diff == 1:
                diff = 0
                # print(f'afd_order_data:::state = {state} last to jump')
                i += 1
                state = 7

        elif state == 7:
            if c == 10:  # \n
                i = 1
                row += 1
                return buffer, _i, i, row
            elif c == 32 or c == 9:  # space tab
                i += 1
            elif c == 44:  # ,
                _i += 1  # Not
                i += 1
                state = 6
            else:
                report_error(i, row, f'afd_order_data:::state = {state} Se esperaba "\\n" , se encontró "{_c}"')
        _i += 1


def afd_product(s, _i, i, row):
    product_id, product_name, product_price, product_description = "", "", 0, ""
    buffer = []
    state = 0

    # pre = 0
    # post = 0
    diff = 0
    for _c in list(s[_i:]):
        c = ord(_c)
        print(f'afd_product:::state = {state} row={row} i={i} {c}:{_c}')
        if state == 0:
            if c == 10:  # \n
                i = 1
                row += 1
            elif c == 32 or c == 9:  # space tab
                i += 1
            elif c == 91:  # [
                # _i += 1  # Not
                i += 1
                state = 1
            else:
                report_error(i, row, f'afd_product:::state = {state} Se esperaba [, se encontró "{_c}"')

        elif state == 1:
            # print(f'afd_product:::diff es: {diff} _i:{_i}  i:{i} row:{row}')
            if diff == 0:
                pre = _i
                product_id, post, i, row = afd_id_sem(s, _i, i, row)
                diff = post - pre - 1  # -1 for ;
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(f'afd_product:::state = {state}  product_id reconocida: {product_id}')
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                buffer.append(product_id)
            elif diff > 1:
                diff -= 1
            elif diff == 1:
                diff = 0
                print(f'afd_product:::state = {state} last to jump')
                # i += 1  # commented to compensate for -1 in diff
                state = 2

        elif state == 2:
            if c == 10:  # \n
                i = 1
                row += 1
            elif c == 32 or c == 9:  # space tab
                i += 1
            elif c == 59:  # ;
                # _i += 1  # Not
                i += 1
                print(f'afd_product:::state = {state} ; reconocido')
                state = 3
            else:
                report_error(i, row, f'afd_product:::state = {state} Se esperaba ; , se encontró "{_c}"')

        elif state == 3:
            # print(f'afd_product:::diff es: {diff}')
            if diff == 0:
                pre = _i
                product_name, post, i, row = afd_chain(s, _i, i, row)
                diff = post - pre - 1  # -1 for ;
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(f'afd_product:::product_name reconocida: {product_name}')
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                buffer.append(product_name)
            elif diff > 1:
                diff -= 1
            elif diff == 1:
                diff = 0
                print(f'afd_product:::state = {state} last to jump')
                i += 1
                state = 4

        elif state == 4:
            if c == 10:  # \n
                i = 1
                row += 1
            elif c == 32 or c == 9:  # space tab
                i += 1
            elif c == 59:  # ;
                # _i += 1  # Not
                i += 1
                print(f'afd_product:::state = {state} ; reconocido')
                state = 5
            else:
                report_error(i, row, f'afd_product:::state = {state} Se esperaba ; , se encontró "{_c}"')

        elif state == 5:
            # print(f'afd_product:::diff es: {diff}')
            if diff == 0:
                pre = _i
                product_price, post, i, row = afd_number(s, _i, i, row)
                diff = post - pre - 1
                i -= 1
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(f'afd_product:::state = {state} product_price reconocida: {product_price}')
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                buffer.append(float(product_price))
            elif diff > 1:
                diff -= 1
            elif diff == 1:
                diff = 0
                print(f'afd_product:::state = {state} last to jump')
                state = 6

        elif state == 6:
            if c == 10:  # \n
                i = 1
                row += 1
            elif c == 32 or c == 9:  # space tab
                i += 1
            elif c == 59:  # ;
                # _i += 1  # Not
                # i += 1
                print(f'afd_product:::state = {state} ; reconocido')
                i += 1
                state = 7
            else:
                report_error(i, row, f'afd_product:::state = {state} Se esperaba ; , se encontró "{_c}"')
        elif state == 7:
            # print(f'afd_product:::diff es: {diff}')
            if diff == 0:
                pre = _i
                product_description, post, i, row = afd_chain(s, _i, i, row)
                diff = post - pre - 1  # -1 for ;
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(f'afd_product:::product_description reconocida: {product_description}')
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                buffer.append(product_description)
            elif diff > 1:
                diff -= 1
            elif diff == 1:
                diff = 0
                print(f'afd_product:::state = {state} last to jump')
                i += 1
                state = 8
        elif state == 8:
            if c == 10:  # \n
                i = 1
                row += 1
            elif c == 32 or c == 9:  # space tab
                i += 1
            elif c == 93:  # ]
                _i += 1  # Not
                i += 1
                # state = 9
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(f'afd_product:::state = {state} Resultado final:{product_id}:{product_name}:{product_price}:{product_description}')
                return buffer, _i, i, row

            else:
                report_error(i, row, f'afd_product:::state = {state} Se esperaba ], se encontró "{_c}"')
        _i += 1


def afd_id_eq(s, _i, i, row):
    # global menu_string
    buffer = ""
    state = 0
    first_i = i

    for _c in list(s[_i:]):
        c = ord(_c)
        print(f'afd_id_eq:::state = {state} row={row} i={i} {c}:{_c}')

        if state == 0:

            if c == 10:
                i = 1
                row += 1

            elif c == 32 or c == 9:  # Space Tab
                i += 1

            elif 97 <= c <= 122:
                first_i = i
                i += 1
                buffer += _c
                state = 1
            else:
                report_error(i, row, f'afd_id_eq:::state = {state} Se esperaba a-z, se encontró "{_c}"')
                i += 1

        elif state == 1:
            if (48 <= c <= 57) or (65 <= c <= 90) or (97 <= c <= 122) or c == 95:
                i += 1
                buffer += _c

            elif c == 10:  # \n
                i = 1
                row += 1

            # elif c == 32 or c == 9:  # tab space
                # i += 1

            elif c == 61:
                i += 1
                state = 2
            else:
                report_error(i, row, f'afd_id_eq:::state = {state}:Se esperaba a-z, se encontró "{_c}"')
                i += 1

        elif state == 2:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(f'afd_id_eq:::final:{buffer}')
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            report_token(first_i, row, buffer, "id")
            return buffer, _i, i, row

        elif state == 2:
            pass

        _i += 1


def afd_id_sem(s, _i, i, row):
    buffer = ""
    state = 0
    first_i = i

    for _c in list(s[_i:]):
        c = ord(_c)
        print(f'afd_id_sem:::state = {state} row={row} i={i} {c}:{_c}')

        if state == 0:

            if c == 10:
                i = 1
                row += 1

            elif c == 32 or c == 9:
                i += 1

            elif 97 <= c <= 122:
                first_i = i
                i += 1
                buffer += _c
                state = 1
            else:
                report_error(i, row, f'afd_id_sem:::state = {state}:Se esperaba a-z, se encontró "{_c}"')
                i += 1

        elif state == 1:
            if (48 <= c <= 57) or (65 <= c <= 90) or (97 <= c <= 122) or c == 95:
                i += 1
                buffer += _c

            elif c == 10:  # \n
                i = 1
                row += 1

            elif c == 32 or c == 9:  # tab space
                i += 1

            elif c == 59:  # ;
                i += 1
                state = 2
            else:
                report_error(i, row, f'afd_id_sem:::state = {state} Se esperaba [a-z0-9_] o =, se encontró "{_c}"')
                i += 1

        elif state == 2:
            print(f'afd_id_sem:::final:{buffer}')
            report_token(first_i, row, buffer, "id")
            return buffer, _i-1, i-1, row

        _i += 1


def afd_chain(s, _i, i, row):
    buffer = ""
    state = 0
    first_i = i

    for _c in list(s[_i:]):
        c = ord(_c)
        print(f'afd_cadena:::state = {state} row={row} i={i} {c}:{_c}')
        if state == 0:
            if c == 39:  # '
                i += 1
                first_i = i  # Yes, after i++
                state = 1

            elif c == 10:  # \n
                i = 1
                row += 1
            elif c == 32 or c == 9:  # space tab
                i += 1

            else:
                report_error(i, row, f'afd_cadena:::state = {state} Se esperaba \', se encontró "{_c}"')

        elif state == 1:

            if c == 10:  # \n
                i = 1
                row += 1

            # elif c == 32 or c == 9:  # space tab
                # i += 1

            elif c != 39:  # not '
                buffer += _c
                i += 1

            else:
                # Terminado
                _i += 1
                report_token(first_i, row, buffer, "chain")
                return buffer, _i, i, row

        _i += 1


def afd_section(s, _i, i, row):
    buffer = ""
    state = 0

    for _c in list(s[_i:]):
        c = ord(_c)
        print(f'afd_section:::state = {state} row={row} i={i} {c}:{_c}')
        if state == 0:
            if c == 39:
                i += 1
                state = 1

            elif c == 10:
                i = 1
                row += 1
            elif c == 32 or c == 9:
                i += 1

            else:
                report_error(i, row, f'afd_section:::state = {state} Se esperaba \', se encontró "{_c}"')

        elif state == 1:

            if c == 10:
                i = 1
                row += 1

            elif c != 39:
                buffer += _c
                i += 1

            else:
                i += 1
                state = 2

        elif state == 2:

            if c == 10:  # \n
                i = 1
                row += 1

            elif c == 32 or c == 9:  # space tab
                i += 1

            elif c == 58:
                # Terminado
                _i += 1
                return buffer, _i, i, row

            else:
                report_error(i, row, f'afd_section:::state = {state} Se esperaba \', se encontró "{_c}"')

        _i += 1


def afd_section_or_product(s, _i, i, row):
    # buffer = ""
    state = 0
    for _c in list(s[_i:]):
        c = ord(_c)
        print(f'afd_section_or_product:::state = {state} row={row} i={i} {c}:{_c}')
        if state == 0:
            if c == 10:  # \n
                i = 1
                row += 1
            elif c == 32 or c == 9:  # space tab
                i += 1
            elif c == 91:  # [
                # _i += 1  # Not
                return "Product", _i, i, row
            elif c == 39:  # '
                # _i += 1  # Not
                return "Section", _i, i, row
            else:
                report_error(i, row, f'afd_section_or_product:::state = {state} Se esperaba [ o \', se encontró "{_c}"')
        _i += 1

    # Si nada fue retornado
    return "End", _i, i, row


def afd_number(s, _i, i, row):
    buffer = ""
    state = 0
    first_i = i

    for _c in list(s[_i:]):
        c = ord(_c)
        print(f'afd_number:::state = {state} _i:{_i} i={i} row={row}  {c}:{_c}')

        if state == 0:
            if 48 <= c <= 57:  # 0-9
                first_i = i
                i += 1
                buffer += _c
                state = 1

            elif c == 10:  # \n
                i = 1
                row += 1

            elif c == 32 or c == 9:  # tab space
                i += 1

            else:
                report_error(i, row, f'afd_number:::state = {state} Se esperaba [0-9] , se encontró "{_c}"')
                i += 1

        elif state == 1:
            if 48 <= c <= 57:
                i += 1
                buffer += _c

            elif c == 46:  # .
                state = 2
                i += 1
                buffer += _c

            elif c == 10:  # \n
                i = 1
                row += 1

            elif c == 32 or c == 9:  # tab space
                i += 1

            else:
                # report_error(i, row, f'afd_number:::state = {state} Se esperaba [0-9] , se encontró "{_c}"')
                i += 1
                report_token(first_i, row, buffer, "number")
                return buffer, _i, i, row

        elif state == 2:
            if 48 <= c <= 57:
                i += 1
                buffer += _c

            elif c == 10:  # \n
                i = 1
                row += 1

            elif c == 32 or c == 9:  # tab space
                i += 1

            # elif c == 46:  # .
                # report_error(i, row, f'afd_number:::state = {state} Se esperaba [0-9] , se encontró "{_c}"')  # always .

            else:
                i += 1
                return buffer, _i, i, row
        _i += 1


def afd_number_percentage(s, _i, i, row):
    buffer = ""
    state = 0
    first_i = i

    for _c in list(s[_i:]):
        c = ord(_c)
        print(f'afd_number_percentage:::state = {state} _i:{_i} i={i} row={row}  {c}:{_c}')

        if state == 0:
            if 48 <= c <= 57:  # 0-9
                first_i = i
                i += 1
                buffer += _c
                state = 1

            elif c == 10:  # \n
                i = 1
                row += 1

            elif c == 32 or c == 9:  # tab space
                i += 1

            else:
                report_error(i, row, f'afd_number_percentage:::state = {state} Se esperaba [0-9] , se encontró "{_c}"')
                i += 1

        elif state == 1:
            if 48 <= c <= 57:
                i += 1
                buffer += _c

            elif c == 46:  # .
                state = 2
                i += 1
                buffer += _c

            elif c == 37:  # %
                _i += 1
                # i += 1  # idk why, it just didn't work
                report_token(first_i, row, buffer, "number_percentage")
                return buffer, _i, i, row

            elif c == 10:  # \n
                i = 1
                row += 1

            elif c == 32 or c == 9:  # tab space
                i += 1

            else:
                report_error(i, row, f'afd_number_percentage:::state = {state} Se esperaba [0-9] , se encontró "{_c}"')
                i += 1

        elif state == 2:
            if 48 <= c <= 57:
                i += 1
                buffer += _c

            elif c == 37:  # %
                # i += 1  # idk why just it didn't work
                _i += 1
                report_token(first_i, row, buffer, "number_percentage")
                return buffer, _i, i, row

            elif c == 10:  # \n
                i = 1
                row += 1

            elif c == 32 or c == 9:  # tab space
                i += 1

            else:
                report_error(i, row, f'afd_number_percentage:::state = {state} Se esperaba [0-9] , se encontró "{_c}"')
                i += 1
        _i += 1


def report_error(i, row, msg):
    print(f'row:{i} _ column:{row}:: {msg}')
    error_list.insert(ParseError(row, i, msg))


def report_token(i, row, lex, token):
    print(f'row:{i} _ column:{row}:: type={token} lex={lex}')
    token_list.insert(Element(row, i, token, lex))


def open_menu():
    global menu_string
    menu_string = open_file()


def open_order():
    global order_string
    order_string = open_file()


# Returns array of lines of file to open
def open_file():

    file = fileopenbox("Python files", "Open files", default="*.lfp")
    print(f'Se selecciono el archivo {file}')

    with open(file, 'r', encoding="utf-8") as file1:
        file_string = "".join(line.rstrip() for line in file1)

    file1.close()
    return file_string


def debug_load():
    global menu_string
    global order_string

    with open("C:\\Users\\Matus\\Documents\\USAC\\LFP1\\LAB\\proyecto1\\menu.lfp", 'r', encoding="utf-8") as file:
        menu_string = "".join(line for line in file) + "\n"

    with open("C:\\Users\\Matus\\Documents\\USAC\\LFP1\\LAB\\proyecto1\\orden.lfp", 'r', encoding="utf-8") as file:
        order_string = "".join(line for line in file) + "\n"


if __name__ == '__main__':
    main()

# Abi
