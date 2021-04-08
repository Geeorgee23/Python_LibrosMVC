from libros import Libros
from controlador import Controlador


controlador=Controlador()


while True:

    print("Actualmente hay ",controlador.numLibros()," libros")
    print("1.- Añadir Libro")
    print("2.- Eliminar Libro")
    print("3.- Mejor y Peor Libro")
    print("4.- Listar Libros")
    print("5.- Salir")

    while True:
        try:
            op=int(input("Introduce opción:"))
            if op>=1 and op<=6:
                break
            else:
                print("Introduce un numero entre el 1 y el 6")
        except ValueError:
            print("Introduce un numero")

    if op==5:
        break

    if op==1:
        print()
        print("Añadiendo Libro...")
        isbn=input("Introduce ISBN: ")
        titulo=input("Introduce Titulo: ")
        autor=input("Introduce Autor: ")
        numPag=input("Introduce el número de páginas: ")
        nota=input("Introduce nota: ")

        libro = Libros(isbn,titulo,autor,numPag,nota)

        if (controlador.addLibro(libro)):
            print("Libro añadido correctamente!")
        else:
            print("Error al añadir el libro!")

        print()

    if op==2:
        print()
        print("Eliminando libro...")
        isbn=input("Introduce el isbn del libro a eliminar: ")

        if (controlador.delLibro(isbn)):
            print("Libro eliminado correctamente!")
        else:
            print("Error al eliminar el libro!")
        print()


    if op==3:
        print()
        print("Libro con mejor nota: ")
        print(controlador.mejorNota())
        print()

        print("Libro con peor nota: ")
        print(controlador.peorNota())
        print()

    if op==4:
        print()
        print("Lista de Libros: ")
        for i in controlador.listarLibros():
            print(i)

        print()