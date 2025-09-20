"""
Ejercicio 3: Procesamiento Básico de Datos Médicos
Objetivo: Trabajar con tablas 2D que representan datos médicos
"""

# Simular datos médicos en una tabla 4x4
# Cada número representa la intensidad de una imagen médica (0-100)
imagen_medica = [
    [10, 20, 80, 15],  # Fila 0
    [25, 90, 85, 30],  # Fila 1  
    [20, 85, 90, 25],  # Fila 2
    [15, 30, 20, 10]   # Fila 3
]

print("=== EJERCICIO 3: DATOS MÉDICOS ===")
print("\nImagen médica original (intensidades 0-100):")

# Mostrar la imagen como tabla
for i in range(4):
    fila_str = ""
    for j in range(4):
        fila_str += f"{imagen_medica[i][j]:3d} "
    print(f"Fila {i}: {fila_str}")

print("\n--- ANÁLISIS BÁSICO ---")

# 1. Encontrar áreas de alta intensidad (mayor a 70)
print("Posiciones con alta intensidad (>70):")
contador_alto = 0
for i in range(4):
    for j in range(4):
        if imagen_medica[i][j] > 70:
            print(f"  Posición [{i}][{j}]: {imagen_medica[i][j]}")
            contador_alto += 1

print(f"Total de puntos con alta intensidad: {contador_alto}")

# 2. Calcular promedio por fila
print("\nIntensidad promedio por fila:")
for i in range(4):
    suma_fila = 0
    for j in range(4):
        suma_fila += imagen_medica[i][j]
    promedio_fila = suma_fila / 4
    print(f"  Fila {i}: {promedio_fila:.2f}")

# 3. Calcular promedio por columna  
print("\nIntensidad promedio por columna:")
for j in range(4):
    suma_columna = 0
    for i in range(4):
        suma_columna += imagen_medica[i][j]
    promedio_columna = suma_columna / 4
    print(f"  Columna {j}: {promedio_columna:.2f}")

# 4. Aplicar filtro simple (reducir ruido)
print("\n--- APLICAR FILTRO SIMPLE ---")
print("Filtro: Si un valor es menor a 20, cambiarlo a 20")

# Crear copia de la imagen original
imagen_filtrada = []
for i in range(4):
    fila = []
    for j in range(4):
        if imagen_medica[i][j] < 20:
            fila.append(20)  # Valor mínimo
        else:
            fila.append(imagen_medica[i][j])  # Mantener original
    imagen_filtrada.append(fila)

print("\nImagen después del filtro:")
for i in range(4):
    fila_str = ""
    for j in range(4):
        fila_str += f"{imagen_filtrada[i][j]:3d} "
    print(f"Fila {i}: {fila_str}")

# 5. Comparar antes y después
print("\nComparación de cambios:")
cambios = 0
for i in range(4):
    for j in range(4):
        if imagen_medica[i][j] != imagen_filtrada[i][j]:
            print(f"  Posición [{i}][{j}]: {imagen_medica[i][j]} → {imagen_filtrada[i][j]}")
            cambios += 1

if cambios == 0:
    print("  No hubo cambios")
else:
    print(f"  Total de cambios: {cambios}")

# 6. Calcular diferencia en promedios
suma_original = 0
suma_filtrada = 0
for i in range(4):
    for j in range(4):
        suma_original += imagen_medica[i][j]
        suma_filtrada += imagen_filtrada[i][j]

promedio_original = suma_original / 16
promedio_filtrado = suma_filtrada / 16

print(f"\nPromedio original: {promedio_original:.2f}")
print(f"Promedio filtrado: {promedio_filtrado:.2f}")
print(f"Diferencia: {promedio_filtrado - promedio_original:.2f}")

print("\n=== FIN DEL EJERCICIO 3 ===")