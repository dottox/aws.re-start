# 1. Escribe un programa que pida al usuario que ingrese la temperatura en grados Celsius y clasifique la temperatura según la siguiente tabla:
# Menor a 0°C: "Hace mucho frío"
# Entre 0°C y 15°C: "Hace frío"
# Entre 16°C y 25°C: "Está templado"
# Mayor a 25°C: "Hace calor"

temp = int(input("Ingrese la temperatura en grados Celsius: "))

if temp < 0:
    print("Hace mucho frío")
elif temp <= 15:
    print("Hace frío")
elif temp <= 25:
    print("Está templado")
else:
    print("Hace calor")


# 2. Escribe una función llamada calcular_perimetro que reciba dos argumentos (base y altura) y devuelva el perímetro de un rectángulo.

def calcular_perimetro(base, altura):
    return 2 * (base + altura)


# 3. Escribe un programa que pida al usuario que ingrese un número entero y determine si el número es par o impar.

num = int(input("Ingrese un número entero: "))
if num % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")
