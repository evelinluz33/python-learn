


def suma(a: int, b: int) -> int:
    return a + b

def resta(a: int, b: int) -> int:
    return a - b

def multiplicacion(a: int, b: int) -> int:
    return a * b

def division(a: int, b: int) -> float:
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return a / b

def procesar(funcion):
    numero_a = input("Digite o primer número: ")
    numero_b = input("Digite o segundo número: ")
    print(f"{numero_a} + {numero_b} = {funcion(int(numero_a), int(numero_b))}")

input("Presione Enter para iniciar la calculadora...")

operacion = input("Escribe operación (+, -, *, /): ")

#if operacion not in ('+', '-', '*', '/'):

if operacion == '+':
    procesar(suma)
elif operacion == '-':
    procesar(resta)
elif operacion == '*':
    procesar(multiplicacion)
elif operacion == '/':
    procesar(division)
else:
    raise ValueError("No es una operación válida.")
    exit(1)
