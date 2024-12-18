def validate_expression(expression):
    stack = []
    opening = "({["
    closing = ")}]"
    matching = dict(zip(closing, opening))
    valid_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+-*/"

    for char in expression:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack or stack[-1] != matching[char]:
                return {"valid": False, "error": "Paréntesis desbalanceados"}
            stack.pop()
        elif char not in valid_chars and char != " ":
            return {"valid": False, "error": f"Carácter inválido: {char}"}

    if stack:
        return {"valid": False, "error": "Paréntesis desbalanceados"}

    return {"valid": True}
