from src.pila import Pila

def precedencia(operador):
    """
    Retorna la precedencia de un operador matemático.
    """
    if operador == "+" or operador == "-":
        return 1
    if operador == "*" or operador == "/":
        return 2
    return 0

def aplicar_operacion(op, b, a):
    """
    Aplica la operación matemática entre dos operandos.
    """
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        return a / b

def evaluar_expresion(expresion):
    """
    Evalúa una expresión matemática en notación infija utilizando una pila.
    """
    pila_valores = Pila()
    pila_operadores = Pila()
    i = 0
    
    while i < len(expresion):
        if expresion[i] == ' ':
            i += 1
            continue

        if expresion[i] == '(':
            pila_operadores.push(expresion[i])

        elif expresion[i] == ')':
            while pila_operadores.peek() != '(':
                oper = pila_operadores.pop()
                val2 = pila_valores.pop()
                val1 = pila_valores.pop()
                pila_valores.push(aplicar_operacion(oper, val2, val1))
            pila_operadores.pop()  # Remueve '('

        elif expresion[i].isdigit():
            num = 0
            while i < len(expresion) and expresion[i].isdigit():
                num = num * 10 + int(expresion[i])
                i += 1
            pila_valores.push(num)
            continue

        else:
            while (not pila_operadores.is_empty() and
                   precedencia(pila_operadores.peek()) >= precedencia(expresion[i])):
                oper = pila_operadores.pop()
                val2 = pila_valores.pop()
                val1 = pila_valores.pop()
                pila_valores.push(aplicar_operacion(oper, val2, val1))
            pila_operadores.push(expresion[i])

        i += 1

    while not pila_operadores.is_empty():
        oper = pila_operadores.pop()
        val2 = pila_valores.pop()
        val1 = pila_valores.pop()
        pila_valores.push(aplicar_operacion(oper, val2, val1))

    return pila_valores.pop()
