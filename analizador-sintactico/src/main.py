from validator import validate_expression

def main():
    print("Bienvenido al Analizador Sintáctico")
    expression = input("Ingresa una expresión: ")
    result = validate_expression(expression)

    if result["valid"]:
        print("La expresión es válida.")
    else:
        print(f"Error: {result['error']}")

if __name__ == "__main__":
    main()
