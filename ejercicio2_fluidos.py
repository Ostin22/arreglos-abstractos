"""
Ejercicio 2: Manejo Básico de una Estructura 3D
Objetivo: Aprender a crear y acceder a elementos en un arreglo 3D
"""

# Crear un "cubo" 2x2x2 que representa temperaturas en diferentes puntos
# temperatura[profundidad][fila][columna]
temperatura = [
    [  # Profundidad 0 (capa frontal)
        [20, 25],  # fila 0
        [22, 28]   # fila 1
    ],
    [  # Profundidad 1 (capa trasera)  
        [18, 23],  # fila 0
        [21, 26]   # fila 1
    ]
]

print("=== EJERCICIO 2: TEMPERATURAS EN 3D ===")
print("\nEstructura 3D de temperaturas (°C):")

# Mostrar cada capa
for profundidad in range(2):
    print(f"\nCapa {profundidad}:")
    for fila in range(2):
        print(f"  Fila {fila}: {temperatura[profundidad][fila]}")

print("\n--- ANÁLISIS BÁSICO ---")

# 1. Acceder a elementos específicos
print("Acceso a elementos específicos:")
print(f"  Temperatura en posición [0][0][0]: {temperatura[0][0][0]}°C")
print(f"  Temperatura en posición [1][1][1]: {temperatura[1][1][1]}°C")
print(f"  Temperatura en posición [0][1][0]: {temperatura[0][1][0]}°C")

# 2. Calcular temperatura total
total_temp = 0
contador = 0
for prof in range(2):
    for fila in range(2):
        for col in range(2):
            total_temp += temperatura[prof][fila][col]
            contador += 1

print(f"\nTemperatura total: {total_temp}°C")
print(f"Número total de puntos: {contador}")

# 3. Calcular promedio
promedio = total_temp / contador
print(f"Temperatura promedio: {promedio:.2f}°C")

# 4. Temperatura por capa
print("\nTemperatura promedio por capa:")
for prof in range(2):
    suma_capa = 0
    puntos_capa = 0
    for fila in range(2):
        for col in range(2):
            suma_capa += temperatura[prof][fila][col]
            puntos_capa += 1
    promedio_capa = suma_capa / puntos_capa
    print(f"  Capa {prof}: {promedio_capa:.2f}°C")

# 5. Encontrar temperatura máxima y mínima
temp_max = temperatura[0][0][0]  # Empezar con el primer elemento
temp_min = temperatura[0][0][0]
pos_max = (0, 0, 0)
pos_min = (0, 0, 0)

for prof in range(2):
    for fila in range(2):
        for col in range(2):
            if temperatura[prof][fila][col] > temp_max:
                temp_max = temperatura[prof][fila][col]
                pos_max = (prof, fila, col)
            if temperatura[prof][fila][col] < temp_min:
                temp_min = temperatura[prof][fila][col]
                pos_min = (prof, fila, col)

print(f"\nTemperatura máxima: {temp_max}°C en posición {pos_max}")
print(f"Temperatura mínima: {temp_min}°C en posición {pos_min}")

# 6. Modificar un valor
print("\n--- MODIFICACIÓN ---")
print(f"Valor original en [0][0][1]: {temperatura[0][0][1]}°C")
temperatura[0][0][1] = 30  # Cambiar la temperatura
print(f"Nuevo valor en [0][0][1]: {temperatura[0][0][1]}°C")

print("\n=== FIN DEL EJERCICIO 2 ===")