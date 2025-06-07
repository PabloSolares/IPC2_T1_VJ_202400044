import xml.etree.ElementTree as ET
import os

class Vuelo:
    def __init__(self, codigo, origen, destino, duracion, aerolinea):
        self.codigo= codigo
        self.origen= origen
        self.destino= destino
        self.duracion= duracion
        self.aerolinea= aerolinea

    def __repr__(self):
        return f'El codigo es {self.codigo} la duracion es de {self.duracion} horas'
    def getCodigo(self):
        return self.codigo
    def getOrigen(self):
        return self.origen
    def getDestino(self):
        return self.destino
    def getDuracion(self):
        return self.duracion
    def getAerolinea(self):
        return self.aerolinea
    def descripcion(self):
        return f'El codigo es {self.codigo}, el origen del vuelo es {self.origen}, su destino es {self.destino}, la duracion es de {self.duracion} horas, y la aerolinea es {self.aerolinea}'

class Node: 
    def __init__(self, dato):
        self.dato = dato
        self.siguente = None

class Lista:
    def __init__(self):
        self.primero = None
        self.ultimo = None
    def vacia(self):
        return self.primero == None
    def agregarUltimo(self, dato):
        if self.vacia():
            self.primero = self.ultimo = Node(dato)
        else :
            aux = self.ultimo
            self.ultimo = aux.siguente = Node(dato)
    def recorrido(self):
        aux = self.primero
        while aux != None:
            print(aux.dato.descripcion())
            aux = aux.siguente
    def codigoExistente(self, codigo):
        aux = self.primero
        while aux != None:
            if aux.dato.getCodigo() == codigo:
                return True
            aux = aux.siguente
        return False
    def buscarCodigo(self, codigo):
        aux = self.primero
        while aux != None:
            if aux.dato.getCodigo() == codigo:
                return aux.dato
            aux = aux.siguente
        return None
    def aerolineas(self, aero):
        nodo = aero.primero
        while nodo != None:
            aerolinea = nodo.dato  
            print(f"Aerolínea: {aerolinea}")
            
            auxAe = self.primero
            contador = 1
            while auxAe != None:
                if auxAe.dato.getAerolinea() == aerolinea:
                    print(f'{contador}. {auxAe.dato.getCodigo()}')
                    contador += 1
                auxAe = auxAe.siguente
            nodo = nodo.siguente
    def aerolineaExistente(self, aerolinea):
        aux = self.primero
        while aux != None:
            if aux.dato == aerolinea:
                return True
            aux = aux.siguente
        return False 

lista = Lista()
aerolineas = Lista()
vuelosLista = []
def leerArchivo(path):
    tree = ET.parse(path)
    root = tree.getroot()

    
    for vuelos in root.findall('vuelo'):
        codigo = vuelos.find('codigo').text
        origen = vuelos.find('origen').text
        destino = vuelos.find('destino').text
        duracion = vuelos.find('duracion').text
        aerolinea = vuelos.find('aerolinea').text

        vuelo = Vuelo(codigo,origen,destino,int(duracion),aerolinea)
        vuelosLista.append(vuelo)
        if lista.codigoExistente(codigo):
            pass
        else:
            lista.agregarUltimo(vuelo)
        
        if aerolineas.aerolineaExistente(aerolinea):
            pass
        else:
            aerolineas.agregarUltimo(aerolinea)  

def menu():
    while True: 
        print("\n--- Menu---")
        print('1. Cargar Archivo')
        print('2. Detalle de vuelo especifico')
        print('3. Agrupar vuelos por aerolínea')
        print('4. Ordenar más duración a menor duración')
        print('5. Salir')
        opcion = input('Selecciona una opcion: ')

        if opcion == '1' : 
            path = input('Ingrese la ruta del archivo .xml: ')
            if os.path.exists(path):
                print('El archivo existe.')
                if path.endswith('.xml') :
                    print('El archivo cargado correctamente')
                    leerArchivo(path)
                else : 
                    print('La ruta del archivo es incorreta. Solo es valido el formato .xml')
            else:
                print('El archivo con la ruta ingresada no existe. Vuelva a ingresar otra ruta.')
        elif opcion == '2':
            if lista.vacia(): 
                print('No has agregado los vuelos. Agrega los vuelos en 1. ') 
            else :  
                codigo = input('Ingrese codigo a buscar: ')
                busqueda = lista.buscarCodigo(codigo)
                if busqueda != None:
                    print(busqueda.descripcion())
                else:
                    print('Codigo no encontrado')
        elif opcion == '3':
            print('Aerolineas: ')
            if lista.vacia(): 
                print('No has agregado los vuelos. Agrega los vuelos en 1. ') 
            else :  
                lista.aerolineas(aerolineas)
        elif opcion == '4': 
            print('Duracion: ')
            if lista.vacia(): 
                print('No has agregado los vuelos. Agrega los vuelos en 1. ') 
            else :  
               vuelosLista.sort(key=lambda vuelo:int(vuelo.duracion), reverse=True)
               for vuelo in vuelosLista:
                   print(f'{vuelo.getCodigo()} - {vuelo.getDuracion()}')
        elif opcion == '5':
            print('Saliendo del programa...')
            break
        else:
            print('Opción no valida')

if __name__ == '__main__':
    menu()
