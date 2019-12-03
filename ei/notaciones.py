from ei.q_s import Stack


class Operador:
    def __init__(self, oper):
        '''
        Documentación:
        Este método dentro de la clase Operador se encarga de inicializar un
        operador aritmético.

        Parámetros:
        * oper: Es el operador aritmético que va a ser asignado.

        Retornos:
        Sin retornos
        '''
        self.operador = oper
        if oper == ')':
            self.prioridad = 1
        elif oper == '^':
            self.prioridad = 2
        elif oper == '*' or oper == '/':
            self.prioridad = 3
        elif oper == '+' or oper == '-':
            self.prioridad = 4
        elif oper == '(':
            self.prioridad = 5


class Prefija:
    def __init__(self, expresión_infija):
        '''
        Documentación:
        Este método dentro de la clase Prefija se encarga de inicializar la
        expresión arimética en notación infija.

        Parámetros:
        * expresión_infija: Es la expresión aritmética infija la cual debe
        obligatoriamente ser una cadena.

        Retornos:
        Sin retornos
        '''
        self.exp_inf = expresión_infija
        self.operadores = (Operador('('), Operador(
            '+'), Operador('-'), Operador('*'), Operador('/'), Operador(
            '^'), Operador(')'))

    def __invertir_str(self, exp):
        '''
        Documentación:
        Este método dentro de la clase Prefija se encarga de invertir una
        cadena.

        Parámetros:
        * exp: Es la cadena que será invertida.

        Retornos:
        * invertido: Es la cadena "exp" invertida.
        '''
        invertido = ''
        for i in range(len(exp)-1, -1, -1):
            invertido += exp[i]
        return invertido

    def infija(self):
        '''
        Documentación:
        Este método dentro de la clase Prefija se encarga de reacomodar la
        expresión infija de tal manera de que quede cada operando y cada
        operador separado por un espacio en blanco.

        Parámetros:
        Sin Parámetros

        Retornos:
        * infija: Retorna la expresión infija ordenada.
        '''
        infija = ''
        operadores = ('(', '+', '-', '*', '/', '^', ')')
        numeros = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
        for c in self.exp_inf:
            if c in numeros:
                infija += c
            elif c in operadores:
                if infija != '' and infija[-1] != ' ':
                    infija += ' '
                infija += c + ' '
        return infija

    def prefija(self):
        '''
        Documentación:
        Este método dentro de la clase Prefija se encarga de transforma la
        expresión infija en notación prefija o polaca.

        Parámetros:
        Sin Parámetros

        Retornos:
        * str_pre_inv: Retorna la expresión infija en notación prefija.
        '''
        operadores = ('(', '+', '-', '*', '/', '^', ')')
        numeros = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
        str_prefija = ''
        pil_operadores = Stack()
        con = 0
        for c in self.__invertir_str(self.exp_inf):
            if c in numeros:
                str_prefija += c
            elif c in operadores:
                if pil_operadores.es_vacio():
                    if str_prefija != '' and str_prefija[-1] != ' ':
                        str_prefija += ' '
                    operador = Operador(c)
                    if operador.operador is ')':
                        con += 1
                    if con == 0:
                        if operador.prioridad >= pil_operadores.cima().prioridad:
                            while (pil_operadores.cima() is not None):
                                operador_des = pil_operadores.desapilar()
                                str_prefija += operador_des.operador
                                if str_prefija[-1] != ' ':
                                    str_prefija += ' '
                        pil_operadores.apilar(operador)
                    else:
                        if operador.operador is not '(':
                            if (operador.prioridad >= pil_operadores.cima().prioridad and
                                    pil_operadores.cima().operador is not ')'):
                                while (pil_operadores.cima() is not None and
                                       pil_operadores.cima().operador is not ')'):
                                    operador_des = pil_operadores.desapilar()
                                    str_prefija += operador_des.operador
                                    if str_prefija[-1] != ' ':
                                        str_prefija += ' '
                            pil_operadores.apilar(operador)
                        else:
                            while (pil_operadores.es_vacio() and
                                   pil_operadores.cima().operador is not ')'):
                                operador_des = pil_operadores.desapilar()
                                str_prefija += operador_des.operador
                                if str_prefija[-1] != ' ':
                                    str_prefija += ' '
                            if pil_operadores.cima().operador == ')':
                                con -= 1
                            pil_operadores.desapilar()
                else:
                    if c is ')':
                        con += 1
                    pil_operadores.apilar(Operador(c))
                    if str_prefija != '' and str_prefija[-1] != ' ':
                        str_prefija += ' '
        if pil_operadores.es_vacio():
            while pil_operadores.cima() is not None:
                operador_des = pil_operadores.desapilar()
                str_prefija += ' ' + operador_des.operador + ' '
        str_pre_inv = self.__invertir_str(str_prefija)
        return str_pre_inv[1:]

    def eval_expr_aritm(self):
        '''
        Documentación:
        Este método dentro de la clase Prefija se encarga de calcular el
        resultado de la expresión en notación prefija.

        Parámetros:
        Sin Parámetros

        Retornos:
        * operandos.desapilar(): Retorna el último elemento de la pila operandos
        el cual será el resultado final de la evaluación de la expresión.
        '''
        operadores = ('+', '-', '*', '/', '^')
        numeros = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
        prefija = self.prefija()
        operandos = Stack()
        digito = ''
        for c in self.__invertir_str(prefija):
            if c in numeros:
                digito += c
            elif c is ' ':
                if len(digito) == 1:
                    operandos.apilar(float(digito))
                elif len(digito) > 1:
                    operandos.apilar(float(self.__invertir_str(digito)))
                digito = ''
            elif c in operadores:
                valor1 = operandos.desapilar()
                valor2 = operandos.desapilar()
                if c is '+':
                    operandos.apilar(valor1 + valor2)
                elif c is '-':
                    operandos.apilar(valor1 - valor2)
                elif c is '*':
                    operandos.apilar(valor1 * valor2)
                elif c is '/':
                    operandos.apilar(valor1 / valor2)
                elif c is '^':
                    operandos.apilar(valor1 ** valor2)
        return operandos.desapilar()
