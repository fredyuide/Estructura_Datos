from evaluator import evaluate_postfix

if __name__ == "__main__":
    # Expresión en notación posfija: "3 4 + 2 * 7 /"
    expression = input("Ingresa una expresión en notación posfija (separada por espacios): ")
    stack_type = input("Elige el tipo de pila ('array' o 'linked_list'): ").strip()

    try:
        result = evaluate_postfix(expression, stack_type)
        print(f"El resultado de la expresión es: {result}")
    except Exception as e:
        print(f"Error: {e}")
