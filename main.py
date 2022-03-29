import code
from Book import Book
from structures import*
#  ____________________________________________
# |                                            |
# |        FUNCIONES RESPECTO A:               |                                      
# |                                            |
# |____________________________________________|
#

def split(word):
    return [char for char in word]



#  ____________________________________________
# |                                            |
# |        FUNCIONES RESPECTO A:               |                                      
# |             PRINTS                         |
# |____________________________________________|
#        

def start():
    print('''
  _      _ _                   __        _____   __  _     _ _           
 | |    (_) |                 /_/       |  __ \ /_/ | |   | (_)          
 | |     _| |__  _ __ ___ _ __ _  __ _  | |__) |   _| |__ | |_  ___ __ _ 
 | |    | | '_ \| '__/ _ \ '__| |/ _` | |  ___/ | | | '_ \| | |/ __/ _` |
 | |____| | |_) | | |  __/ |  | | (_| | | |   | |_| | |_) | | | (_| (_| |
 |______|_|_.__/|_| _\___|_|  |_|\__,_| |_|    \__,_|_.__/|_|_|\___\__,_|
           _        _    _             _           _   _
          | |      |  \/  |           | |         | | | |                          
        __| | ___  | \  / | __ _ _ __ | |__   __ _| |_| |_ __ _ _ __               
       / _` |/ _ \ | |\/| |/ _` | '_ \| '_ \ / _` | __| __/ _` | '_ \              
      | (_| |  __/ | |  | | (_| | | | | | | | (_| | |_| || (_| | | | |             
       \__,_|\___| |_|  |_|\__,_|_| |_|_| |_|\__,_|\__|\__\__,_|_| |_|             
                                                                               
                                                                                   
    
                        .--.                   .---.
                    .---|__|           .-.     |~~~|
                    .--|===|--|_          |_|     |~~~|--.
                    |  |===|  |'\     .---!~|  .--|   |--|
                    |%%|   |  |.'\    |===| |--|%%|   |  |
                    |%%|   |  |\.'\   |   | |__|  |   |  |
                    |  |   |  | \  \  |===| |==|  |   |  |
                    |  |   |__|  \.'\ |   |_|__|  |~~~|__|
                    |  |===|--|   \.'\|===|~|--|%%|~~~|--|
                    ^--^---'--^    `-'`---^-^--^--^---'--'


                     ____________________________________
                    |                                    | 
                    |    Presione enter para ingresar    |   
                    |____________________________________|
    ''')

    input()
    menu()


#  ____________________________________________
# |                                            |
# |        FUNCIONES RESPECTO A:               |                                      
# |             BÚSQUEDA                       |
# |____________________________________________|
#        


def search():
    answerS = input('''Ingrese el tipo de búsqueda que desea hacer:

1. Por título
2. Por serial
    
''')

    while answerS != "1" and answerS != "2":
            answerS = input('''Ingreso inválido. Ingrese el tipo de búsqueda que desea hacer:

1. Por título
2. Por serial
    
''')

    if answerS == "1":
        code = returnT()

        if code == None:
            print('\nEl libro que ingresó no fue encontrado, intente de nuevo')
            search()

        else:

            hashC = hashCode(int(split(code)[-1]), int(split(code)[-2]))
            book = searchT(hashC, code)
            book.show_book()
            returnTo()



    else:
        code = returnS()

        if code == None:
            print('\nEl libro que ingresó no fue encontrado, intente de nuevo')
            search()

        else:

            hashC = hashCode(int(split(code)[-1]), int(split(code)[-2]))
            book = searchT(hashC, code)
            book.show_book()
            returnTo()


def searchT(hashC, code):

    for books in allBooks[hashC]:
        for book in books:
            if code == book.code:
                return book

#Funciones encargadas de retornar el código del libro en caso de que se encuentre, o si devuelve None decirle al usario que vuelva a intentar
def returnT():
    print(titleCode_list)
    answerT = input("\nIngrese el nombre del libro que desea buscar: ")

    for elements in titleCode_list:

        for key,value in elements.items():

            if answerT == key:
                return value



def returnS():
    print(titleCode_list)
    answerS = input("\nIngrese el serial del libro que desea buscar: ")

    for elements in serialCode_list:


        for key,value in elements.items():

            if answerS == key:
                return value




def returnTo():
    print('\n¿Quiére volver al menú')
    answerU = answers()
    if answerU:
        menu()
    else:
        exit()


#  ____________________________________________
# |                                            |
# |        FUNCIONES RESPECTO A:               |                                      
# |             PRÉSTAMO Y RETORNO             |
# |____________________________________________|
#        





def borrowed():

    code = returnT()
    
    hashC = hashCode(int(split(code)[-1]), int(split(code)[-2]))

    book = searchT(hashC, code)

    n = num_input()


    book.numD = int(book.numD) - n

    book.numB = int(book.numB) + n

    print(f'Se tomó prestado {n} libros y quedán disponibles un total de {book.numD} libros')
    book.show_book()

    returnTo()


def returnedBooks():

    code = returnT()
    
    hashC = hashCode(int(split(code)[-1]), int(split(code)[-2]))

    book = searchT(hashC, code)

    n = num_input()

    book.numD = book.numD + n

    book.numB = book.numB - n

    print(f'Se devolvió {n} libros y quedán disponibles un total de {book.numD} libros')
    book.show_book()

    returnTo()


#  ____________________________________________
# |                                            |
# |        FUNCIONES RESPECTO A:               |                                      
# |        ELIMINACIÓN                         |
# |____________________________________________|
#

def deleteBook():

    code = returnT()
    
    hashC = hashCode(int(split(code)[-1]), int(split(code)[-2]))

    book = searchT(hashC, code)

    boolval = delBook(book, hashC)

    if boolval == True:
    
        pass


    else:        

        pass



def delBook(book, hashC):

    for books in allBooks[hashC]:
        for bookI in books:

            if book == bookI:
                allBooks.remove(book)
                return True

    



#  ____________________________________________
# |                                            |
# |                  MENÚ                      |                                      
# |                                            |
# |____________________________________________|
#        




def menu():
    print(allBooks)
    print(serialCode_list)
    print(titleCode_list)

    print('''

     ___________________________________________________________
    |                 __  __              __                |   |
    |                |  \/  |            /_/                |   |
    |                | \  / | ___ _ __  _   _               |   |
    |                | |\/| |/ _ \ '_ \| | | |              |   |
    |                | |  | |  __/ | | | |_| |              |   |
    |                |_|  |_|\___|_| |_|\__,_|              |   |
    |_______________________________________________________|___|                      
                              
    
''')

    option = input('''Ingrese el número según lo que quiera realizar:
1. Inserción de un Nuevo Libro a la Base de Datos 
2. Búsqueda de un Libro en la Base de Datos
3. Préstamo de un Libro
4. Retorno de un Libro
5. Eliminación de un Libro de la Base de Datos
6. Salir

-->''')
    while option != "1" and option != "2" and option != "3" and option != "4" and option != "5" and option != "6":
            option = input('''Input inválido. Ingrese el número según lo que quiera realizar:
1. Inserción de un Nuevo Libro a la Base de Datos 
2. Búsqueda de un Libro en la Base de Datos
3. Préstamo de un Libro
4. Retorno de un Libro
5. Eliminación de un Libro de la Base de Datos
6. Salir

-->''')    

    if option == "1":
        data_input()
    elif option == "2":
        search()
    elif option == "3":
        borrowed()    
    elif option == "4":
        returnedBooks()
    elif option == "5":
        deleteBook()
    else:
        exit(0)

#  ____________________________________________
# |                                            |
# |        FUNCIONES RESPECTO A:               |                                      
# |        INPUTS                              |
# |____________________________________________|
#

def answers():
    option = input('''Ingrese el número de su respuesta:
1. Sí 
2. No

-->''')
    while option != "1" and option != "2":
            option = input('''Input inválido. Ingrese el número de su respuesta:
1. Sí 
2. No

-->''')
    
    if option == "1":
        return True

    else:
        return False

def serial_input():
    serial = input('Ingrese el serial del libro:\n')
    while len(serial) != 12:
        serial = input('Input inválido. Ingrese el serial del libro:\n')

    try:
            serial = int(serial)
    except ValueError:
            return serial_input()
    return serial



def num_input():
    num = input('Ingrese el número:\n')
    try:
            num = int(num)
    except ValueError:
            return num_input()
    return num



def data_input():
    code = input('Ingrese la cota del libro:\n')

    sliceWrd = slice(6)



    while code.isspace() or code == "" or len(code) != 8 or not split(code)[-1].isnumeric() or not split(code)[-2].isnumeric() or not code[sliceWrd].isalpha():
          code = input('Input inválido. Ingrese la cota del libro:\n')

    title = input('Ingrese el título del libro:\n')
    while title == "" or title.isspace() or len(title) > 30:
         title = input('Input inválido. Ingrese el título del libro:\n')

    serial = serial_input()

    print('\n¿Cuántos libros se encuentran disponibles?')

    numD = num_input() #Validación de input numérico

    book = Book(code, title, serial, numD, 0) #Se crea el objeto libro

    book.show_book() #Se muestran el libro al usuario

    allBooks = hashStructure(int(split(code)[-1]), int(split(code)[-2]), book) #Se ingresa a la bd el libro

#Uso de las estructuras auxiliares

    titleCode_list = title_code(title, code) 

    serialCode_list = serial_code(serial, code)


    returnTo()




#  ____________________________________________
# |                                            |
# |                 MENÚ                       |                                      
# |                                            |
# |____________________________________________|
#        





def main():
    start()

main()

