from paquete_archivos.miarchivo import MiArchivo, MiArchivoEscribir
from modelado.modelo import *

m = MiArchivo() # objeto para leer el archivo
m2 = MiArchivoEscribir() # objeto para escribir el archivo

lista = m.obtener_informacion()
lista = [l.split("|") for l in lista]




for d in lista:
    p = Equipo(d[0], d[1], d[2], d[3])
    operacion = Operaciones(p)
    print(p)
    m2.agregar_informacion(p)

m.cerrar_archivo()
m2.cerrar_archivo()