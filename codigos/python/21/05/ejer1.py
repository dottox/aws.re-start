# Escribe un programa que pida al usuario que ingrese la temperatura en grados Celsius y clasifique la temperatura según la siguiente tabla:
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

