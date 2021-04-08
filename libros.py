class Libros:
    def __init__ (self, isbn, titulo, autor, numPag, nota):
        self.isbn=isbn
        self.titulo=titulo
        self.autor=autor
        self.numPag=numPag
        self.nota=nota

    def getIsbn(self):
        return self.isbn

    def getTitulo(self):
        return self.titulo

    def getAutor(self):
        return self.autor

    def getNumPag(self):
        return self.numPag

    def getNota(self):
        return self.nota


    def modCalificacion(self,nota):
        self.nota=nota
    