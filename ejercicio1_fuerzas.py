"""
Ejercicio 1: Análisis Básico de Fuerzas en una Estructura
Objetivo: Aprender a crear y manejar una matriz 2D simple
"""

# Crear una matriz 3x3 que representa fuerzas en una estructura
# Cada número representa la fuerza en Newtons en cada punto
fuerzas = [
    [10, 20, 15],  # Fila 0: fuerzas en el nivel superior
    [25, 30, 20],  # Fila 1: fuerzas en el nivel medio
    [15, 10, 25]   # Fila 2: fuerzas en el nivel inferior
]

print("=== EJERCICIO 1: TABLA DE FUERZAS ===")
print("\nMatriz de fuerzas (en Newtons):")

# Mostrar la matriz de forma bonita
for i in range(3):
    print(f"Fila {i}: {fuerzas[i]}")

print("\n--- ANÁLISIS BÁSICO ---")

# 1. Sumar todas las fuerzas (fuerza total)
total = 0
for fila in fuerzas:
    for fuerza in fila:
        total += fuerza

print(f"Fuerza total en toda la estructura: {total} N")

# 2. Calcular fuerzas por fila (cada nivel)
print("\nFuerzas por nivel:")
for i in range(3):
    suma_fila = 0
    for j in range(3):
        suma_fila += fuerzas[i][j]
    print(f"  Nivel {i}: {suma_fila} N")

# 3. Calcular fuerzas por columna (cada soporte)
print("\nFuerzas por soporte:")
for j in range(3):
    suma_columna = 0
    for i in range(3):
        suma_columna += fuerzas[i][j]
    print(f"  Soporte {j}: {suma_columna} N")

# 4. Encontrar la fuerza máxima y mínima
fuerza_max = fuerzas[0][0]  # Empezar con el primer elemento
fuerza_min = fuerzas[0][0]
pos_max = (0, 0)
pos_min = (0, 0)

for i in range(3):
    for j in range(3):
        if fuerzas[i][j] > fuerza_max:
            fuerza_max = fuerzas[i][j]
            pos_max = (i, j)
        if fuerzas[i][j] < fuerza_min:
            fuerza_min = fuerzas[i][j]
            pos_min = (i, j)

print(f"\nFuerza máxima: {fuerza_max} N en posición {pos_max}")
print(f"Fuerza mínima: {fuerza_min} N en posición {pos_min}")

# 5. Calcular promedio
promedio = total / (3 * 3)  # total dividido número de elementos
print(f"\nFuerza promedio: {promedio:.2f} N")

print("\n=== FIN DEL EJERCICIO 1 ===")