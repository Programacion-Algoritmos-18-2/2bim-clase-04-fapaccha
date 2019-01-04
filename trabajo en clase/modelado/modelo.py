class Equipo():
    
    def __init__(self, nom, ciu, camp,numj):
        self.nombre = nom
        self.ciudad = ciu
        self.campeonato = camp
        self.numJugadores = numj

    def agregar_nombre(self, n):
        """
        """
        self.nombre = n

    def obtener_nombre(self):
        """
        """
        return self.nombre

    def agregar_ciudad(self, a):
        """
        """
        self.ciudad = a
        
    def obtener_ciudad(self):
        """
        """
        return self.ciudad

    def agregar_campeonato(self, n):
        """
        """
        self.campeonato = n

    def obtener_campeonato(self):
        """
        """
        return self.campeonato
    
    def agregar_numJug(self, n):
        """
        """
        self.numJugadores = n

    def obtener_numJug(self):
        """
        """
        return self.numJugadores

    def __str__(self):
        """
        """
        return "%s - %s - %s - %s  " % (self.obtener_nombre() ,self.obtener_ciudad () ,self.obtener_campeonato (),self.obtener_numJug())

    def __repr__(self):
        """
        """
        return "%s - %s - %s - %s  " % (self.obtener_nombre() ,self.obtener_ciudad () ,self.obtener_campeonato (),self.obtener_numJug())
 

class Operaciones(object):
    
    def __init__(self, listado):
        self.listado_estudiantes = listado

    def ordenar(self):
        """
            https://docs.python.org/3/howto/sorting.html
            >>> sorted(student_objects, key=lambda student: student.age)   # sort by age
        """
        return sorted(self.listado_estudiantes, key=lambda equipo: equipo.obtener_nombre())    