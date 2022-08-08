from inspect import stack


def parentesis_balanceado(text):
    stack = 0
    for el in text:
        if el == "(":
            stack += 1
        elif el == ")":
            stack -= 1
        if stack < 0:
            return False
    return stack == 0

print(parentesis_balanceado("()()(()())"))