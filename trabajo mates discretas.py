def euclides(a, b):
    while b:
        a, b = b, a % b
    return a

def main():
    try:
        num1 = int(input("Introduce el primer número: "))
        num2 = int(input("Introduce el segundo número: "))

        mcd = euclides(num1, num2)
        print(f"El MCD de {num1} y {num2} es: {mcd}")
    except ValueError:
        print("Por favor, introduce números enteros válidos.")

if __name__ == "__main__":
    main()
