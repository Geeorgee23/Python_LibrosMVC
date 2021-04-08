from libros import Libros


class Controlador:
    def __init__(self):
        self.listaLibros={}


    def numLibros(self):
        return len(self.listaLibros)

    def addLibro(self,libro):
        if (libro.getIsbn() not in self.listaLibros):
            self.listaLibros[libro.getIsbn()]=libro
            return True
        return False


    def delLibro(self,isbn):
        if (isbn in self.listaLibros):
            del self.listaLibros[isbn]
            return True
        return False


    def listarLibros(self):
        lista=[]
        for clave, valor in self.listaLibros.items():
            lista.append("ISBN: "+clave+"\n\tTitulo: "+valor.getTitulo()+"\n\tAutor: "+valor.getAutor()+"\n\tNumero de Paginas: "+valor.getNumPag()+"\n\tNota: "+valor.getNota())
        return lista


    def mejorNota(self):
        mejorlibro=[]
        nota=0
        for clave, valor in self.listaLibros.items():

            if (int(valor.getNota())>nota):
                nota=int(valor.getNota())
                mejorlibro=("ISBN: "+clave+"\n\tTitulo: "+valor.getTitulo()+"\n\tAutor: "+valor.getAutor()+"\n\tNumero de Paginas: "+valor.getNumPag()+"\n\tNota: "+valor.getNota())
        return mejorlibro


    def peorNota(self):
        peorlibro=[]
        nota=10
        for clave, valor in self.listaLibros.items():
            if (int(valor.getNota())<nota):
                nota=int(valor.getNota())
                peorlibro=("ISBN: "+clave+"\n\tTitulo: "+valor.getTitulo()+"\n\tAutor: "+valor.getAutor()+"\n\tNumero de Paginas: "+valor.getNumPag()+"\n\tNota: "+valor.getNota())
        return peorlibro