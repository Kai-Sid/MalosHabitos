# Función para calcular el área de un rectángulo
def rectangulo(ancho, largo):
    areaR = ancho * largo
    return areaR


# Función para calcular el área de un triángulo
def triangulo(base, altura):
    areaT = 0.5 * base * altura
    return areaT


# Función principal
def main():
    ancho = float(input("Ingrese el ancho del rectángulo: "))
    largo = float(input("Ingrese el largo del rectángulo: "))
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))

    print("#########################################################")

    rect_area = rectangulo(ancho, largo)
    print(f"Área del rectángulo: {ancho} * {largo} = ", rect_area)

    tri_area = triangulo(base, altura)
    print(f"Área del triángulo: {0.5} * {base} * {altura} = ", tri_area)


main()
