

class Calculadora:

    def __init__(self, a: int, b: int, operacion: str) -> None:
        self.a = a
        self.b = b
        self.op = operacion
    
    def suma(self) -> int:
        return self.a + self.b

    def resta(self) -> int:
        return self.a - self.b

    def multiplicacion(self) -> int:
        return self.a * self.b

    def division(self) -> float:
        if b == 0:
            raise ValueError("No se puede dividir por cero.")
        return self.a / self.b
    
    def resultado(self, resultado) -> None:
        print(f"{self.a} {self.op} {self.b} = {resultado}")


def procesar():
    input("Presione Enter para iniciar la calculadora...")
    operacion = input("Escribe operación (+, -, *, /): ")
    numero_a = input("Digite o primer número: ")
    numero_b = input("Digite o segundo número: ")
    calculadora = Calculadora(int(numero_a), int(numero_b), operacion)
    if operacion == '+':
        calculadora.resultado(calculadora.suma())
    elif operacion == '-':
        calculadora.resultado(calculadora.resta())
    elif operacion == '*':
        calculadora.resultado(calculadora.multiplicacion())
    elif operacion == '/':
        calculadora.resultado(calculadora.division())
    else:
        raise ValueError("No es una operación válida.")
        exit(1)

procesar()