import operator

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def evaluate(self):
        if self.value in OPERATORS:
            left_val = self.left.evaluate()
            right_val = self.right.evaluate()
            return OPERATORS[self.value](left_val, right_val)
        else:
            return float(self.value)

OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

def build_expression_tree(tokens):
    stack = []
    for token in tokens:
        if token in OPERATORS:
            right = stack.pop()
            left = stack.pop()
            stack.append(Node(token, left, right))
        else:
            stack.append(Node(token))
    return stack[0]

def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    output = []
    stack = []
    tokens = expression.replace('(', ' ( ').replace(')', ' ) ').split()
    
    for token in tokens:
        if token.isnumeric() or '.' in token:
            output.append(token)
        elif token in precedence:
            while (stack and stack[-1] != '(' and precedence[stack[-1]] >= precedence[token]):
                output.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
    
    while stack:
        output.append(stack.pop())
    
    return output

# Uso del árbol de expresión
expression = "3 + 5 * ( 2 - 8 )"
postfix_expr = infix_to_postfix(expression)
tree = build_expression_tree(postfix_expr)
result = tree.evaluate()
print("Resultado:", result)
