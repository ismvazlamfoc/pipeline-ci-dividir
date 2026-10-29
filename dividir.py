
def dividir(a: int, b: int) -> float:
    """Devuelve la division de dos numeros enteros."""
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero.")

    return a / b


def main():
    try:
        a = int(input("Introduce el primer numero entero: "))
        b = int(input("Introduce el segundo numero entero: "))

        resultado = dividir(a, b)
        print("El resultado de la division es:", resultado)

    except ValueError:
        print("Error: debes introducir numeros enteros.")
    except ZeroDivisionError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
