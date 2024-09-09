def calcular(n1, n2, n3):
    respuesta = n1 * n2 + n3
    return respuesta


if __name__ == "__main__":
    n1 = float(input("Primer número: "))
    n2 = float(input("Segundo número: "))
    n3 = float(input("Tercer número: "))

    resultado = calcular(n1, n2, n3)
    print(f"El resultado es: {n1} * {n2} + {n3} = ", resultado)
