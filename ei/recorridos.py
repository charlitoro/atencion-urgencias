def __ver_nodo(sub_arbol):
    ''' Documentación:
    Esta función oculta se encarga de hacer visible si un nodo tiene hijos
    tanto por izquierda como por derecha.

    Parámetros:
    *sub_arbol: Árbol para visualizar.

    Retornos:
    Sin Retornos
    '''
    print(f"[{sub_arbol.clave}]")
    print('O' if sub_arbol.izq is not None else 'X', end=':')
    print('O' if sub_arbol.der is not None else 'X')


def __pre_orden(sub_arbol):
    ''' Documentación:
    Esta función oculta se encarga de recorrer un árbol binario priorizando un
    nodo para luego recorrerlo por izquierda y después de terminar con los
    nodos por izquierda continuar con los nodos por derecha.

    Parámetros:
    *sub_arbol: Árbol para recorrer.

    Retornos:
    Sin Retornos
    '''
    if sub_arbol is not None:
        __ver_nodo(sub_arbol)
        # print(sub_arbol.clave)
        __pre_orden(sub_arbol.izq)
        __pre_orden(sub_arbol.der)


def __in_orden(sub_arbol):
    ''' Documentación:
    Esta función oculta se encarga de recorrer un árbol binario priorizando su
    recorrido por izquierda para luego visualizar un nodo y después recorrer
    sus nodos por derecha.

    Parámetros:
    *sub_arbol: Árbol para recorrer.

    Retornos:
    Sin Retornos
    '''
    if sub_arbol is not None:
        __in_orden(sub_arbol.izq)
        # __ver_nodo(sub_arbol)
        print(sub_arbol.clave)
        __in_orden(sub_arbol.der)


def __post_orden(sub_arbol):
    ''' Documentación:
    Esta función oculta se encarga de recorrer un árbol binario priorizando su
    recorrido por izquierda para luego recorrerlo por derecha y terminar en un
    nodo en específico.

    Parámetros:
    *sub_arbol: Árbol para recorrer.

    Retornos:
    Sin Retornos
    '''
    if sub_arbol is not None:
        __post_orden(sub_arbol.izq)
        __post_orden(sub_arbol.der)
        # __ver_nodo(sub_arbol)
        print(sub_arbol.clave)


def pre_orden(arbol):
    ''' Documentación:
    Esta función se encarga de recorrer un árbol mediante la técnica pre orden
    a través de una función oculta.

    Parámetros:
    *arbol: Árbol para recorrer.

    Retornos:
    Sin Retornos
    '''
    __pre_orden(arbol.raiz)


def post_orden(arbol):
    ''' Documentación:
    Esta función se encarga de recorrer un árbol mediante la técnica post orden
    a través de una función oculta.

    Parámetros:
    *arbol: Árbol para recorrer.

    Retornos:
    Sin Retornos
    '''
    __post_orden(arbol.raiz)


def in_orden(arbol):
    ''' Documentación:
    Esta función se encarga de recorrer un árbol mediante la técnica in orden
    a través de una función oculta.

    Parámetros:
    *arbol: Árbol para recorrer.

    Retornos:
    Sin Retornos
    '''
    __in_orden(arbol.raiz)


# Tarea
def __str_pre_orden(sub_arbol, str_pre):
    '''Documentación:
    Función oculta que retorna una cadena con el siguiente formato
    formato de impresión -> [clave][clave][clave]...

    Parámetros:
    *sub_arbol: Árbol para imprimir.

    Retornos:
    *Retorna una cadena con las claves del árbol.
    '''
    if sub_arbol is not None:
        str_pre += f'[{str(sub_arbol.clave)}]'
        str_pre = __str_pre_orden(sub_arbol.izq, str_pre)
        str_pre = __str_pre_orden(sub_arbol.der, str_pre)
    return str_pre


def str_pre_orden(arbol):
    '''Documentación:
    Función que retorna una cadena con las claves del árbol.

    Parámetros:
    *arbol: Árbol para imprimir.

    Retornos:
    *Retorna una cadena con las claves del árbol.
    '''
    return __str_pre_orden(arbol.raiz, str_pre='')


def __str_post_orden(sub_arbol, str_post):
    '''Documentación:
    Función oculta que retorna una cadena con el siguiente formato
    formato de impresión -> [clave][clave][clave]...

    Parámetros:
    *sub_arbol: Árbol para imprimir.

    Retornos:
    *Retorna una cadena con las claves del árbol.
    '''
    if sub_arbol is not None:
        str_post = __str_post_orden(sub_arbol.izq, str_post)
        str_post = __str_post_orden(sub_arbol.der, str_post)
        str_post += f'[{str(sub_arbol.clave)}]'
    return str_post


def str_post_orden(arbol):
    '''Documentación:
    Función que retorna una cadena con las claves del árbol.

    Parámetros:
    *arbol: Árbol para imprimir.

    Retornos:
    *Retorna una cadena con las claves del árbol.
    '''
    return __str_post_orden(arbol.raiz, str_post='')


def __str_in_orden(sub_arbol, str_in=''):
    ''' Documentación:
    Esta función oculta se encarga de recorrer un árbol de forma recursiva por
    el método in orden e ir concatenando en una cadena sus nodos.

    Parámetros:
    *sub_arbol: Árbol a recorrer.
    *str_in: Por defecto una cadena vacía. Cadena a la cual se concatenarán los
    nodos recorridos.

    Retornos:
    *str_in: Cadena con los nodos concatenados.
    '''
    if sub_arbol is not None:
        str_in = __str_in_orden(sub_arbol.izq, str_in)
        str_in += f'[{str(sub_arbol.clave)}]'
        str_in = __str_in_orden(sub_arbol.der, str_in)
    return str_in


def str_in_orden(arbol):
    ''' Documentación:
    Esta función se encarga de devolver una cadena recorrida a través del
    método in orden.

    Parámetros:
    *arbol: Árbol a recorrer.

    Retornos:
    Cadena con todos los nodos del árbol.
    '''
    return __str_in_orden(arbol.raiz)
