from pila_array import StackArray
from pila_linked_list import StackLinkedList

def evaluate_postfix(expression, stack_type="array"):
    # Elige el tipo de pila: 'array' o 'linked_list'
    stack = StackArray() if stack_type == "array" else StackLinkedList()

    for char in expression.split():
        if char.isdigit():  # Si es un operando
            stack.push(int(char))
        else:  # Si es un operador
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = None
            if char == "+":
                result = operand1 + operand2
            elif char == "-":
                result = operand1 - operand2
            elif char == "*":
                result = operand1 * operand2
            elif char == "/":
                result = operand1 / operand2
            else:
                raise ValueError(f"Unknown operator: {char}")
            stack.push(result)

    return stack.pop()
