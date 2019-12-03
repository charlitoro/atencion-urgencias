import sqlite3
from ei.arboles import AHeap
from ei.listas import LSE


class Paciente:
    '''Clase que modela los métodos y atributos que tendrá un paciente dentro
    del sistema.
    '''
    def __init__(self, id, nom='', tel='', edad=0, eps=''):
        '''Método de la clase Paciente que se encarga de inicializar un nuevo
        paciente.
        Parámetros:
        *id: Identificación del paciente.
        *nom: Nombre del paciente, por defecto vacío.
        *tel: Teléfono del paciente, por defecto vacío.
        *edad: Edad del paciente, por defecto 0.
        *eps: EPS a la cual se encuentra afiliado el paciente, por defecto
        vacío.
        '''
        self.__id_pac = id
        self.__nombre = nom
        self.__telefono = tel
        self.__edad = edad
        self.__eps = eps

    def get_id(self):
        '''Método de la clase Paciente que devuelve la identificación del
        paciente.
        Retornos:
        *self.__id_pac: Identificación actual del paciente.
        '''
        return self.__id_pac

    def get_nombre(self):
        '''Método de la clase Paciente que devuelve el nombre del paciente.
        Retornos:
        *self.__nombre: Nombre actual del paciente.
        '''
        return self.__nombre

    def get_telefono(self):
        '''Método de la clase Paciente que devuelve el teléfono del paciente.
        Retornos:
        *self.__telefono: Télefono actual del paciente.
        '''
        return self.__telefono

    def get_edad(self):
        '''Método de la clase Paciente que devuelve la edad del paciente.
        Retornos:
        *self.__edad: Edad actual del paciente.
        '''
        return self.__edad

    def get_eps(self):
        '''Método de la clase Paciente que devuelve la EPS afiliada al
        paciente.
        Retornos:
        *self.__eps: EPS actual del paciente.
        '''
        return self.__eps

    def __str__(self):
        return (f'[|{self.__id_pac}|{self.__nombre}]')


class Triaje:
    '''Clase que modela los métodos y atributos que tendrá un triaje dentro
    del sistema.
    '''
    def __init__(self, cod_tri, des='', pri=0):
        '''Método de la clase Triaje que se encarga de inicializar un nuevo
        triaje.
        Parámetros:
        *cod_tri: Código perteneciente al triaje.
        *des: Descripción de las prioridades del triaje, por defecto vacío.
        *pri: Prioridad que tendrá la urgencia, por defecto 0.
        '''
        self.__cod_tri = cod_tri
        self.__descripion = des
        self.__prioridad = pri

    def get_codigo(self):
        '''Método de la clase Triaje que devuelve el código del triaje.
        Retornos:
        *self.__cod_tri: Código actual del triaje.
        '''
        return self.__cod_tri

    def get_descripcion(self):
        '''Método de la clase Triaje que devuelve la descripción del triaje.
        Retornos:
        *self.__descripion: Descripción actual del triaje.
        '''
        return self.__descripion

    def get_prioridad(self):
        '''Método de la clase Triaje que devuelve la prioridad de la urgencia.
        Retornos:
        *self.__prioridad: Prioridad actual del triaje.
        '''
        return self.__prioridad

    def __eq__(self, obj):
        '''Método de la clase Triaje que se encarga de comparar dos objetos de
        tipo Triaje para comprobar si son iguales mediante la prioridad.
        Retornos:
        *True: Se retornará verdadero si los objetos son iguales.
        *False: Se retornará falso si los objetos no son iguales.
        '''
        if isinstance(obj, Triaje):
            if self.__prioridad == obj.get_prioridad():
                return True
        return False

    def __lt__(self, obj):
        '''Método de la clase Triaje que se encarga de comparar dos objetos de
        tipo Triaje para comprobar si el objeto actual es menor al nuevo
        objeto mediante la prioridad.
        Retornos:
        *True: Se retornará verdadero si el objeto actual es menor.
        *False: Se retornará falso si el objeto actual es mayor o igual.
        '''
        if isinstance(obj, Triaje):
            if self.__prioridad < obj.get_prioridad():
                return True
        return False

    def __gt__(self, obj):
        '''Método de la clase Triaje que se encarga de comparar dos objetos de
        tipo Triaje para comprobar si el objeto actual es mayor al nuevo
        objeto mediante la prioridad.
        Retornos:
        *True: Se retornará verdadero si el objeto actual es mayor.
        *False: Se retornará falso si el objeto actual es menor o igual.
        '''
        if isinstance(obj, Triaje):
            if self.__prioridad > obj.get_prioridad():
                return True
        return False


class Urgencia:
    '''Clase que modela los métodos y atributos que tendrá una triaje dentro
    del sistema.
    '''
    def __init__(self, cod_urg, pac='', tri=None, obs=None, fecha='', estado=0):
        '''Método de la clase Urgencia que se encarga de inicializar una nueva
        urgencia.
        Parámetros:
        *cod_urg: Código perteneciente a la urgencia.
        *pac: Paciente que presenta la urgencia, por defecto vacío.
        *tri: Triaje que diagnosticó la urgencia, por defecto nulo.
        *obs: Observaciones del paciente diagnosticadas mediante el triaje, por
        defecto nulo.
        *fecha: Fecha en la que se registró la urgencia, por defecto vacío.
        *estado: Estado que describe si la urgencia ya ha sido atendida o no,
        por defecto 0(False).
        '''
        self.__cod_urg = cod_urg
        self.__paciente = pac
        self.__triaje = tri
        self.__observacion = obs
        self.__fecha = fecha
        self.__estado = estado

    def get_codigo(self):
        '''Método de la clase Urgencia que devuelve el código de la urgencia.
        Retornos:
        *self.__cod_urg: Código actual de la urgencia.
        '''
        return self.__cod_urg

    def get_paciente(self):
        '''Método de la clase Urgencia que devuelve el paciente de la urgencia.
        Retornos:
        *self.__paciente: Paciente actual de la urgencia.
        '''
        return self.__paciente

    def get_triaje(self):
        '''Método de la clase Urgencia que devuelve el triaje de la urgencia.
        Retornos:
        *self.__triaje: Triaje actual de la urgencia.
        '''
        return self.__triaje

    def get_observacion(self):
        '''Método de la clase Urgencia que devuelve la observación de la
        urgencia.
        Retornos:
        *self.__observacion: Óbservación actual de la urgencia.
        '''
        return self.__observacion

    def get_fecha(self):
        '''Método de la clase Urgencia que devuelve la fecha de la urgencia.
        Retornos:
        *self.__fecha: Fecha actual de la urgencia.
        '''
        return self.__fecha

    def get_estado(self):
        '''Método de la clase Urgencia que devuelve el estado de la urgencia.
        Retornos:
        *self.__estado: Estado actual de la urgencia.
        '''
        return self.__estado

    def set_paciente(self, pac):
        '''Método de la clase Urgencia que asigna el paciente de la urgencia.
        Parámetros:
        *pac: Paciente de la urgencia.
        '''
        self.__paciente = pac

    def set_triaje(self, tri):
        '''Método de la clase Urgencia que asigna el triaje de la urgencia.
        Parámetros:
        *tri: Triaje de la urgencia.
        '''
        self.__triaje = tri

    def __eq__(self, obj):
        '''Método de la clase Urgencia que se encarga de comparar dos objetos
        de tipo Urgencia para comprobar si son iguales mediante el triaje.
        Retornos:
        *True: Se retornará verdadero si los objetos son iguales.
        *False: Se retornará falso si los objetos no son iguales.
        '''
        if isinstance(obj, Urgencia):
            if self.__triaje == obj.get_triaje():
                return True
        return False

    def __lt__(self, obj):
        '''Método de la clase Urgencia que se encarga de comparar dos objetos
        de tipo Urgencia para comprobar si el objeto actual es menor al nuevo
        objeto mediante el triaje y la fecha.
        Retornos:
        *True: Se retornará verdadero si el objeto actual es menor o si los
        triajes son iguales pero la fecha del objeto actual es mayor a la
        del otro objeto.
        *False: Se retornará falso si el objeto actual es mayor o igual y con
        fecha mayor.
        '''
        if isinstance(obj, Urgencia):
            if self.__triaje < obj.get_triaje():
                return True
            if self.__triaje == obj.get_triaje() and self.__fecha > obj.get_fecha():
                return True
        return False

    def __gt__(self, obj):
        '''Método de la clase Urgencia que se encarga de comparar dos objetos
        de tipo Urgencia para comprobar si el objeto actual es mayor al nuevo
        objeto mediante el triaje y la fecha.
        Retornos:
        *True: Se retornará verdadero si el objeto actual es mayor o si los
        triajes son iguales pero la fecha del objeto actual es menor a la
        del otro objeto.
        *False: Se retornará falso si el objeto actual es menor o igual y con
        fecha menor.
        '''
        if isinstance(obj, Urgencia):
            if self.__triaje > obj.get_triaje():
                return True
            if self.__triaje == obj.get_triaje() and self.__fecha < obj.get_fecha():
                return True
        return False

    def __str__(self):
        '''Método de la clase Urgencia que se encarga de presentar la urgencia
        con su paciente, teiaje y fecha.
        Retornos:
        *Una cadena con los objetos anteriormente mencionados.
        '''
        return (f'[|{self.__paciente.get_nombre()}|{self.__triaje.get_prioridad()}|{self.__fecha}]')


class Administracion:
    '''Clase que modela los métodos y atributos que tendrá la administración
    del sistema.
    '''
    def __init__(self):
        '''Método de la clase Administracion que se encarga de conectar la base
        de datos con el sistema.
        '''
        self.conx_db = sqlite3.connect('db/db_urgencias.db')
        self.cursor = self.conx_db.cursor()

    def get_paciente(self, id_pac):
        '''Método de la clase Administracion que devuelve un paciente de la
        base de datos.
        Parámetros:
        *id_pac: Identificación del paciente que se desea buscar.
        Retornos:
        *paciente: Paciente cuya identificación coincide con la de la búsqueda.
        *None: Retorna nulo si no se encuentra en la base de datos.
        '''
        self.cursor.execute(''' SELECT * FROM pacientes
                            WHERE id_pac = '%s';''' %id_pac)
        for pac in self.cursor:
            id, nom, tel, edad, eps = pac
            paciente = Paciente(id, nom, tel, edad, eps)
            return paciente
        return None

    def get_triaje(self, cod_tri):
        '''Método de la clase Administracion que devuelve un triaje de la
        base de datos.
        Parámetros:
        *cod_tri: Código del triaje que se desea buscar.
        Retornos:
        *triaje: Triaje cuyo código coincide con el de la búsqueda.
        *None: Retorna nulo si no se encuentra en la base de datos.
        '''
        self.cursor.execute(''' SELECT * FROM triajes
                            WHERE cod_tri = '%s';''' %cod_tri)
        for tri in self.cursor:
            cod, des, pri = tri
            triaje = Triaje(cod, des, pri)
            return triaje
        return None

    def get_conse_cod_urg(self):
        self.cursor.execute(''' SELECT MAX(cod_urg) FROM urgencias;''')
        for max in self.cursor:
            if max[0] is None:
                return 1
            return 1 + max[0]

    def agregar_paciente(self, pac):
        '''Método de la clase Administracion que se encarga de añadir un nuevo
        paciente a la base de datos.
        Parámetros:
        *pac: Paciente que se desea añadir.
        '''
        datos = [pac.get_id(), pac.get_nombre(), pac.get_telefono(), pac.get_edad(), pac.get_eps()]
        self.cursor.execute(''' INSERT INTO pacientes VALUES(?, ?, ?, ?, ?);''', datos)
        self.conx_db.commit()

    def agregar_urgencia(self, urg):
        '''Método de la clase Administracion que se encarga de añadir una nueva
        urgencia a la base de datos.
        Parámetros:
        *urg: Urgencia que se desea añadir.
        '''
        cod_pac = urg.get_paciente().get_id()
        cod_tri = urg.get_triaje().get_codigo()
        datos = [urg.get_codigo(), cod_pac, cod_tri, urg.get_observacion(), urg.get_fecha(), urg.get_estado()]
        self.cursor.execute(''' INSERT INTO urgencias VALUES(?, ?, ?, ?, ?, ?);''', datos)
        self.conx_db.commit()

    def update_estado_urgencia(self, cod_urg):
        '''Metodo que se encarga de cambiar el etado de una urgencia a true,
        indicando que ha sido atendida.
        Parametros:
        * cod_urg: coidigo de la urgencia.
        '''
        self.cursor.execute(''' UPDATE urgencias SET estado=1
                                        WHERE cod_urg ='%s ';''' %cod_urg)
        self.conx_db.commit()

    def init_list_id(self, listS_id):
        listS_id.clear()
        self.cursor.execute(''' SELECT id_pac FROM pacientes;''')
        for pac in self.cursor:
            id, = pac
            listS_id.append([id])

    def init_listS_triajes(self, listS_triaje):
        self.cursor.execute(''' SELECT descripcion, prioridad
                            FROM triajes;''')
        for tri in self.cursor:
            des, pri = tri
            listS_triaje.append([des, pri, False])

    def init_listS_historial(self, listS_historial, cod_pac):
        listS_historial.clear()
        self.cursor.execute(''' SELECT fecha, observacion FROM urgencias
                                        WHERE paciente = '%s' and estado = 1;''' %cod_pac)
        for his in self.cursor:
            fecha, observacion = his
            listS_historial.append([fecha, observacion])

    def init_arb_heap_inicial(self, arb_heap):
        arb_aux = AHeap()
        self.cursor.execute(''' SELECT * FROM urgencias
                            WHERE estado = 0''')
        for urg in self.cursor:
            cod_urg, pac, tri, obs, fech, estado = urg
            urgencia = Urgencia(cod_urg, pac, tri, obs, fech, estado)
            arb_aux.agregar(urgencia)
        while arb_aux.raiz is not None:
            urg = arb_aux.traer_cima()
            arb_aux.remover_cima()
            pac = self.get_paciente(urg.get_paciente())
            tri = self.get_triaje(urg.get_triaje())
            urg.set_paciente(pac)
            urg.set_triaje(tri)
            arb_heap.agregar(urg)
