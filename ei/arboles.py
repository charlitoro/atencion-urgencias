from ei.nodos import NodoABin
from random import random


class ABin:
    def __init__(self):
        ''' Documentación:
        Este método dentro de la clase ABin se encarga de inicializar el árbol
        binario.

        Parámetros:
        Sin Parámetros

        Retornos:
        Sin Retornos
        '''
        self.raiz = None

    def es_vacia(self):
        ''' Documentación:
        Este método dentro de la clase ABin se encarga de validar si el árbol
        binario se encuentra vacío.

        Parámetros:
        Sin Parámetros

        Retornos:
        *True: Si el árbol binario se encuentra vacío.
        *False: Si el árbol binario se encuentra vacío.
        '''
        if self.raiz is None:
            return True
        return False

    def __agregar(self, sub_arbol, nueva_clave):
        ''' Documentación:
        Este método oculto dentro de la clase ABin se encarga de agregar un
        nuevo nodo a el árbol binario de manera recursiva.

        Parámetros:
        *sub_arbol: Árbol donde se agregará el nuevo nodo.
        *nueva_clave: Clave que se asignará al nuevo nodo.

        Retornos:
        *sub_arbol: Retorna el sub_arbol donde se agregó el nuevo nodo.
        '''
        if sub_arbol is None:
            sub_arbol = NodoABin(nueva_clave)
        elif random() <= 0.5:  # por izquierda
            sub_arbol.izq = self.__agregar(sub_arbol.izq, nueva_clave)
        else:
            sub_arbol.der = self.__agregar(sub_arbol.der, nueva_clave)
        return sub_arbol

    def __encontrar(self, sub_arbol, clave_buscar):
        ''' Documentación:
        Este método oculto dentro de la clase ABin se encarga de encontrar una
        clave dentro del árbol binario de forma recursiva.

        Parámetros:
        *sub_arbol: Árbol donde se buscará la clave.
        *clave_buscar: Clave a encontrar.

        Retornos:
        *sub_arbol.clave: Retorna la clave hallada.
        *busqueda_izq: Retorna el árbol a buscar por su hijo izquierdo.
        *busqueda_der: Retorna el árbol a buscar por su hijo derecho.
        *None: Retorna None si no se encontró la clave o el árbol es vacío.
        '''
        if sub_arbol is not None:
            if sub_arbol.clave == clave_buscar:
                return sub_arbol.clave
            else:
                busqueda_izq = self.__encontrar(sub_arbol.izq, clave_buscar)
                if busqueda_izq is not None:
                    return busqueda_izq
                busqueda_der = self.__encontrar(sub_arbol.der, clave_buscar)
                if busqueda_der is not None:
                    return busqueda_der
        return None

    def __tamaño(self, sub_arbol):
        ''' Documentación:
        Este método oculto dentro de la clase ABin se encarga de retornar el
        tamaño del árbol binario de manera recursiva.

        Parámetros:
        *sub_arbol: Árbol que se contará para el tamaño.

        Retornos:
        *Retorna el tamaño del árbol.
        *0: Retorna 0 si el árbol se encuentra vacío.
        '''
        if sub_arbol is not None:
            return (1 + self.__tamaño(sub_arbol.izq) +
                    self.__tamaño(sub_arbol.der))
        return 0

    def encontrar(self, clave_buscar):
        ''' Documentación:
        Este método dentro de la clase ABin se encarga de devolver la clave
        encontrada del árbol binario a través de un método oculto.

        Parámetros:
        *clave_buscar: La clave que se requiere encontrar.

        Retornos:
        *Retorna la clave encontrada.
        '''
        return self.__encontrar(self.raiz, clave_buscar)

    def agregar(self, nueva_clave):
        ''' Documentación:
        Este método dentro de la clase ABin se encarga de agregar un nuevo nodo
        a el árbol binario a través de un método oculto.

        Parámetros:
        *nueva_clave: Clave que se agregará al nuevo nodo.

        Retornos:
        Sin Retornos
        '''
        self.raiz = self.__agregar(self.raiz, nueva_clave)

    def __len__(self):
        ''' Documentación:
        Este método dentro de la clase ABin se encarga de calcular el tamaño
        del árbol binario a través de un método oculto.

        Parámetros:
        Sin Parámetros

        Retornos:
        *Retorna el tamaño del árbol.
        '''
        return self.__tamaño(self.raiz)

    # Consulta ---------------------------------------------------------------
    def __num_hojas(self, sub_arbol):
        ''' Documentación:
        Este método oculto dentro de la clase ABin se encarga de calcular el
        número de hojas que contiene el árbol binario.

        Parámetros:
        *sub_arbol: Árbol donde se contarán sus hojas.

        Retornos:
        *con: Retorna el número de hojas que encontró en el árbol.
        *1: Retorna 1 si el árbol sólo contiene la raíz.
        '''
        con = 0
        if sub_arbol is not None:
            if sub_arbol.izq is None and sub_arbol.der is None:
                return 1
            else:
                con += self.__num_hojas(sub_arbol.izq)
                con += self.__num_hojas(sub_arbol.der)
        return con

    def num_hojas(self):
        ''' Documentación:
        Este método dentro de la clase ABin se encarga de retornar el número de
        hojas del árbol binario a través de un método oculto.

        Parámetros:
        Sin Parámetros

        Retornos:
        *Retorna el número de hojas que contiene el árbol.
        '''
        return self.__num_hojas(self.raiz)

    def __num_nodos_internos(self, sub_arbol):
        ''' Documentación:
        Este método oculto dentro de la clase ABin se encarga de calcular el
        número de nodos internos que contiene el árbol binario.

        Parámetros:
        *sub_arbol: Árbol donde se contarán sus nodos internos.

        Retornos:
        *con: Retorna el número de nodos internos que encontró en el árbol.
        *0: Retorna 0 si el árbol es vacío o no contiene nodos internos.
        '''
        con = 1
        if sub_arbol is not None:
            if sub_arbol.izq is None and sub_arbol.der is None:
                return 0
            else:
                con += self.__num_nodos_internos(sub_arbol.izq)
                con += self.__num_nodos_internos(sub_arbol.der)
                return con
        return 0

    def num_nodos_internos(self):
        ''' Documentación:
        Este método dentro de la clase ABin se encarga de retornar el número de
        nodos internos del árbol binario a través de un método oculto.

        Parámetros:
        Sin Parámetros

        Retornos:
        *Retorna el número de nodos internos que contiene el árbol.
        '''
        return self.__num_nodos_internos(self.raiz)

    def __altura(self, sub_arbol):
        ''' Documentación:
        Este método oculto dentro de la clase ABin se encarga de calcular la
        altura del árbol binario.

        Parámetros:
        *sub_arbol: Árbol donde se contará su altura interna.

        Retornos:
        *alt_der: Retorna la altura por la derecha del árbol si esta es mayor
        que la izquierda.
        *alt_izq: Retorna la altura por izquierda del árbol si esta es menor
        que la derecha
        *0: Retorna 0 si el árbol es vacío.
        '''
        alt_izq = alt_der = 1
        if sub_arbol is not None:
            alt_izq += self.__altura(sub_arbol.izq)
            alt_der += self.__altura(sub_arbol.der)
            if alt_der > alt_izq:
                return alt_der
            return alt_izq
        return 0

    def altura(self):
        ''' Documentación:
        Este método dentro de la clase ABin se encarga de retornar la altura
        del árbol binario a través de un método oculto.

        Parámetros:
        Sin Parámetros

        Retornos:
        *Retorna la altura del árbol binario.
        '''
        return self.__altura(self.raiz)


class ABinBus(ABin):

    def agregar(self, nueva_clave):
        ''' Documentación:
        Este método dentro de la clase ABinBus se encarga de agregar un nuevo
        nodo a el árbol binario de búsqueda a través de un método oculto.

        Parámetros:
        *nueva_clave: Clave que se agregará al nuevo nodo.

        Retornos:
        Sin Retornos
        '''
        self.raiz = self.__agregar(self.raiz, nueva_clave)

    def encontrar(self, clave_buscar):
        ''' Documentación:
        Este método dentro de la clase ABinBus se encarga de devolver la clave
        encontrada del árbol binario de búsqueda a través de un método oculto.

        Parámetros:
        *clave_buscar: La clave que se requiere encontrar.

        Retornos:
        *Retorna la clave encontrada.
        '''
        return self.__encontrar(self.raiz, clave_buscar)

    def __agregar(self, sub_arbol, nueva_clave):
        ''' Documentación:
        Este método oculto dentro de la clase ABinBus se encarga de agregar un
        nuevo nodo a el árbol binario de búsqueda de manera recursiva.

        Parámetros:
        *sub_arbol: Árbol donde se agregará el nuevo nodo.
        *nueva_clave: Clave que se asignará al nuevo nodo.

        Retornos:
        *sub_arbol: Retorna el sub_arbol donde se agregó el nuevo nodo.
        '''
        if sub_arbol is None:
            sub_arbol = NodoABin(nueva_clave)
        elif type(sub_arbol.clave) is type(nueva_clave):
            if sub_arbol.clave > nueva_clave:  # por izquierda
                sub_arbol.izq = self.__agregar(sub_arbol.izq, nueva_clave)
            elif sub_arbol.clave < nueva_clave:  # por derecha
                sub_arbol.der = self.__agregar(sub_arbol.der, nueva_clave)
        return sub_arbol

    def __encontrar(self, sub_arbol, clave_buscar):
        ''' Documentación:
        Este método oculto dentro de la clase ABinBus se encarga de encontrar
        una clave dentro del árbol binario de búsqueda de forma recursiva.

        Parámetros:
        *sub_arbol: Árbol donde se buscará la clave.
        *clave_buscar: Clave a encontrar.

        Retornos:
        *sub_arbol.clave: Retorna la clave hallada.
        *None: Retorna None si no se encontró la clave o el árbol es vacío.
        '''
        if sub_arbol is not None:
            if sub_arbol.clave == clave_buscar:
                return sub_arbol.clave
            elif sub_arbol.clave > clave_buscar:
                return self.__encontrar(sub_arbol.izq, clave_buscar)
            else:
                return self.__encontrar(sub_arbol.der, clave_buscar)
        return None

    # Consulta ----------------------------------------------------------------
    def __encontrar_min(self, sub_arbol):
        ''' Documentación:
        Este método oculto dentro de la clase ABinBus se encarga de encontrar
        la clave de menor valor dentro del árbol binario de búsqueda de forma
        recursiva.

        Parámetros:
        *sub_arbol: Árbol donde se buscará la clave.

        Retornos:
        *sub_arbol.clave: Retorna la clave de menor valor.
        *None: Retorna None si el árbol es vacío.
        '''
        if sub_arbol is not None:
            if sub_arbol.izq is None:
                return sub_arbol.clave
            return self.__encontrar_min(sub_arbol.izq)
        return None

    def encontrar_min(self):
        ''' Documentación:
        Este método dentro de la clase ABinBus se encarga de devolver la clave
        de menor valor del árbol binario de búsqueda a través de un método
        oculto.

        Parámetros:
        Sin Parámetros

        Retornos:
        *Retorna la clave de menor valor.
        '''
        return self.__encontrar_min(self.raiz)

    def __encontrar_max(self, sub_arbol):
        ''' Documentación:
        Este método oculto dentro de la clase ABinBus se encarga de encontrar
        la clave de mayor valor dentro del árbol binario de búsqueda de forma
        recursiva.

        Parámetros:
        *sub_arbol: Árbol donde se buscará la clave.

        Retornos:
        *sub_arbol.clave: Retorna la clave de mayor valor.
        *None: Retorna None si el árbol es vacío.
        '''
        if sub_arbol is not None:
            if sub_arbol.der is None:
                return sub_arbol.clave
            return self.__encontrar_max(sub_arbol.der)
        return None

    def encontrar_max(self):
        ''' Documentación:
        Este método dentro de la clase ABinBus se encarga de devolver la clave
        de mayor valor del árbol binario de búsqueda a través de un método
        oculto.

        Parámetros:
        Sin Parámetros

        Retornos:
        *Retorna la clave de mayor valor.
        '''
        return self.__encontrar_max(self.raiz)

    # Consulta ---------------------------------------------------------------
    def __remover(self, sub_arbol, clave_rem, menor):
        ''' Documentación:
        Este método oculto dentro de la clase ABinBus se encarga de remover
        la clave digitada dentro del árbol binario de búsqueda de forma
        recursiva teniendo en cuenta el parámetro menor para saber por cuál de
        sus hijos se reemplazará siempre y cuando este tenga dos hijos, de lo
        contrario el hijo reemplazará la posición de su padre.

        Parámetros:
        *sub_arbol: Árbol donde se buscará la clave.
        *clave_rem: Clave a remover.
        *menor: Si menor es True, se reemplazará el nodo por el menor de sus
        hijos, de lo contrario se reemplazará el nodo por el mayor de sus
        hijos.

        Retornos:
        *sub_arbol: Retorna el árbol modificado.
        '''
        if sub_arbol is not None:
            if type(sub_arbol.clave) == type(clave_rem):
                if sub_arbol.clave == clave_rem:
                    if sub_arbol.izq is None and sub_arbol.der is None:
                        sub_arbol = None
                    elif sub_arbol.izq is None and sub_arbol.der is not None:
                        sub_arbol = sub_arbol.der
                    elif sub_arbol.izq is not None and sub_arbol.der is None:
                        sub_arbol = sub_arbol.izq
                    else:
                        if menor:
                            reemplazo = self.__encontrar_min(sub_arbol.der)
                        else:
                            reemplazo = self.__encontrar_max(sub_arbol.izq)
                        self.__remover(sub_arbol, reemplazo, menor)
                        sub_arbol.clave = reemplazo
                    return sub_arbol
                elif sub_arbol.clave > clave_rem:
                    sub_arbol.izq = self.__remover(sub_arbol.izq, clave_rem, menor)
                else:
                    sub_arbol.der = self.__remover(sub_arbol.der, clave_rem, menor)
        return sub_arbol

    def remover(self, clave_rem, menor=True):
        ''' Documentación:
        Este método dentro de la clase ABinBus se encarga de remover una clave
        del árbol binario de búsqueda a través de un método oculto.

        Parámetros:
        *clave_rem: Clave que contiene el nodo a remover.
        *menor: Por defecto se inicializa en True. Si menor es True, se
        reemplazará el nodo por el menor de los mayores de sus hijos, de lo
        contrario se reemplazará el nodo por el mayor de los menores de sus
        hijos.

        Retornos:
        Sin Retornos.
        '''
        self.raiz = self.__remover(self.raiz, clave_rem, menor)


class AHeap(ABin):
    def __agregar(self, sub_arbol, nueva_clave):
        if sub_arbol is None:
            sub_arbol = NodoABin(nueva_clave)

        else:
            hizq = self.__altura(sub_arbol.izq)
            hder = self.__altura(sub_arbol.der)
            teizq = (2**hizq)-1
            teder = (2**hder)-1
            toizq = self.__tamaño(sub_arbol.izq)
            toder = self.__tamaño(sub_arbol.der)
            if teizq == toizq and toizq != toder:
                sub_arbol.der = self.__agregar(sub_arbol.der, nueva_clave)
                if sub_arbol.der.clave < sub_arbol.clave:
                    sub_arbol.der.clave, sub_arbol.clave = sub_arbol.clave, sub_arbol.der.clave
            elif teizq != toizq:
                sub_arbol.izq = self.__agregar(sub_arbol.izq, nueva_clave)
                if sub_arbol.izq.clave < sub_arbol.clave:
                    sub_arbol.izq.clave, sub_arbol.clave = sub_arbol.clave, sub_arbol.izq.clave
            elif (teizq == teder) and (toizq == toder):
                sub_arbol.izq = self.__agregar(sub_arbol.izq, nueva_clave)
                if sub_arbol.izq.clave < sub_arbol.clave:
                    sub_arbol.izq.clave, sub_arbol.clave = sub_arbol.clave, sub_arbol.izq.clave
        return sub_arbol

    def agregar(self, nueva_clave):
        self.raiz = self.__agregar(self.raiz, nueva_clave)

    def __altura(self, sub_arbol):
        ''' Documentación:
        Este método oculto dentro de la clase ABin se encarga de calcular la
        altura del árbol binario.

        Parámetros:
        *sub_arbol: Árbol donde se contará su altura interna.

        Retornos:
        *alt_der: Retorna la altura por la derecha del árbol si esta es mayor
        que la izquierda.
        *alt_izq: Retorna la altura por izquierda del árbol si esta es menor
        que la derecha
        *0: Retorna 0 si el árbol es vacío.
        '''
        alt_izq = alt_der = 1
        if sub_arbol is not None:
            alt_izq += self.__altura(sub_arbol.izq)
            alt_der += self.__altura(sub_arbol.der)
            if alt_der > alt_izq:
                return alt_der
            return alt_izq
        return 0

    def __remover_cima(self, sub_arbol, raiz):
        if sub_arbol is not None:
            if sub_arbol.izq is not None or sub_arbol.der is not None:
                hizq = self.__altura(sub_arbol.izq)
                hder = self.__altura(sub_arbol.der)
                teizq = (2**hizq)-1
                teder = (2**hder)-1
                toizq = self.__tamaño(sub_arbol.izq)
                toder = self.__tamaño(sub_arbol.der)
                if (teizq == toizq) and (teder == toder):
                    if toizq != toder:
                        sub_arbol.izq = self.__remover_cima(sub_arbol.izq, raiz)
                    else:
                        sub_arbol.der = self.__remover_cima(sub_arbol.der, raiz)
                elif teizq != toizq:
                    sub_arbol.izq = self.__remover_cima(sub_arbol.izq, raiz)
                else:
                    sub_arbol.der = self.__remover_cima(sub_arbol.der, raiz)
            else:
                raiz.clave = sub_arbol.clave
                sub_arbol = None
        return sub_arbol

    def __ordenar(self, sub_arbol):
        if sub_arbol is not None:
            if sub_arbol.izq is not None and sub_arbol.der is not None:
                if sub_arbol.izq.clave < sub_arbol.clave:
                    sub_arbol.clave, sub_arbol.izq.clave = sub_arbol.izq.clave, sub_arbol.clave
                    sub_arbol.izq = self.__ordenar(sub_arbol.izq)
                elif sub_arbol.der.clave < sub_arbol.clave:
                    sub_arbol.clave, sub_arbol.der.clave = sub_arbol.der.clave, sub_arbol.clave
                    sub_arbol.der = self.__ordenar(sub_arbol.der)
            if sub_arbol.izq is not None:
                if sub_arbol.izq.clave < sub_arbol.clave:
                    sub_arbol.clave, sub_arbol.izq.clave = sub_arbol.izq.clave, sub_arbol.clave
                    sub_arbol.izq = self.__ordenar(sub_arbol.izq)
        return sub_arbol

    def ordenar(self):
        self.raiz = self.__ordenar(self.raiz)

    def remover_cima(self):
        self.raiz = self.__remover_cima(self.raiz, self.raiz)
        self.ordenar()

    def __len__(self):
        ''' Documentación:
        Este método dentro de la clase ABin se encarga de calcular el tamaño
        del árbol binario a través de un método oculto.

        Parámetros:
        Sin Parámetros

        Retornos:
        *Retorna el tamaño del árbol.
        '''
        return self.__tamaño(self.raiz)

    def __tamaño(self, sub_arbol):
        ''' Documentación:
        Este método oculto dentro de la clase ABin se encarga de retornar el
        tamaño del árbol binario de manera recursiva.

        Parámetros:
        *sub_arbol: Árbol que se contará para el tamaño.

        Retornos:
        *Retorna el tamaño del árbol.
        *0: Retorna 0 si el árbol se encuentra vacío.
        '''
        if sub_arbol is not None:
            return (1 + self.__tamaño(sub_arbol.izq) +
                    self.__tamaño(sub_arbol.der))
        return 0

    def traer_cima(self):
        if self.raiz is not None:
            return self.raiz.clave
        return None
