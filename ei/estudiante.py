
class Estudiante:

    def __init__(self):
        ''' Constructor de la clase Estudiante, donde se piden los datos para la
        inicializacion de los datos.

        Atributos:
        * self.codigo: unico identificador para cada estudiante
        * self.nombre: nombre del estudiante
        * self.direccion: direccion del estudiante
        * self.programa: programa de estudio en el que se encuentra registrado
        el estudiante'''
        while True:
            try:
                self.codigo = int(input('Codigo: '))
                break
            except ValueError:
                print('Oops!!, solo numeros enteros como dato permitido')
        self.nombre = input('Nombre: ')
        self.direccion = input('Direccion: ')
        self.programa = input('Programa: ')

    def __eq__(self, objeto):
        ''' metodo que permite la comparacion de dos estudiantes para determinar
        su igualdad.

        Parametros:
        * objeto: objeto estudiante con el cual se debe comparar el codigo

        Retornos:
        True: si el codigo de los estudiantes son iguales
        False: si el codigos de los estudiantes son diferentes'''

        if type(self) == type(objeto):
            if self.codigo == objeto.codigo:
                return True
            return False
        return False

    def __str__(self):
        ''' metodo que crea la presentacion de la informacion del estudiante
        cuando el objeto sea llamado por una salida por pantalla

        Retorno:
        * una cadena con la informacion del estudiante para su presentacion. '''

        return('{},{},{},{}'.format(self.codigo, self.nombre, self.direccion,self.programa))
