operando_a = int(input("Operando A: "))
operando_b = int(input("Operando B: "))
operador = input("Digite o operador: ")

def calculadora(operando_a: int, operando_b: int) -> float:
    if operador == '+':
        return operando_a + operando_b
    elif operador == '-':
        return operando_a - operando_b
    elif operador == '*':
        return operando_a * operando_b
    else:
        return operando_a / operando_b
 
print(f"{operando_a} {operador} {operando_b} = {calculadora(operando_a, operando_b)}")
