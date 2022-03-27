from Book import Book

allBooks = [[], []]
titleCode_list = []

def hashCode(number1, number2, book):

    hashC = (number1 + number2)%2

#Función hash que permite dependiendo de la cota ubicar a cuál índice de la lista el libro será almacenado

    if hashC == 0:
        if len(allBooks[0]) < 7: #Con esta condición se revisa si en las listas hash ya se alcanzó el máximo de overflow posible
            if len(allBooks[0]) == 0:
                allBooks[0].append([])
                allBooks[0][-1].append(book)

            elif len(allBooks[0][-1]) < 3:
                allBooks[0][-1].append(book)

                
            elif len(allBooks[0][-1]) == 3: #Con esta condición se chequea si el grupo al que se esté insertando ya tiene un límite de 3 libros, y que en caso de que sí, se cree un overflow
                allBooks[0].append([])
                allBooks[0][-1].append(book)
        else:
            print('no hay espacio mor')

    else:
        if len(allBooks[1]) < 7:
            if len(allBooks[1]) == 0:
                allBooks[1].append([])
                allBooks[1][-1].append(book)

            elif len(allBooks[1][-1]) < 3:
                allBooks[1][-1].append(book)

                
            elif len(allBooks[0][-1]) == 3:
                allBooks[1].append([])
                allBooks[1][-1].append(book)
        else:
            print('no hay espacio mor')
  
    return allBooks #se retorna la lista con la organización ya hecha

def title_code(title, code):

    titleCode = title + code

    titleCode_list.append(titleCode)

    titleCode_list.sort()




    print(titleCode_list)