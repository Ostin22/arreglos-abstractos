"""
Ejercicio 4: Manejo Básico de Datos de Sensores
Objetivo: Organizar y analizar datos en una tabla 2D
"""

# Tabla de temperaturas: 4 sensores en 3 momentos de tiempo
# sensores[momento][sensor] = temperatura en °C
sensores = [
    [22, 25, 23, 24],  # Momento 0 (8:00 AM)
    [25, 28, 26, 27],  # Momento 1 (12:00 PM)  
    [20, 23, 21, 22]   # Momento 2 (6:00 PM)
]

print("=== EJERCICIO 4: DATOS DE SENSORES ===")
print("\nTabla de temperaturas (°C):")
print("Momentos vs Sensores")
print("        Sensor0  Sensor1  Sensor2  Sensor3")

for momento in range(3):
    momento_str = f"Momento{momento}"
    fila_str = f"{momento_str:8}"
    for sensor in range(4):
        fila_str += f"{sensores[momento][sensor]:8d}"
    print(fila_str)

print("\n--- ANÁLISIS POR SENSOR ---")

# 1. Calcular promedio de cada sensor (por columnas)
print("Temperatura promedio por sensor:")
for sensor in range(4):
    suma_sensor = 0
    for momento in range(3):
        suma_sensor += sensores[momento][sensor]
    promedio = suma_sensor / 3
    print(f"  Sensor {sensor}: {promedio:.2f}°C")

# 2. Encontrar el sensor más caliente y más frío
print("\nComparación de sensores:")
for sensor in range(4):
    suma = 0
    for momento in range(3):
        suma += sensores[momento][sensor]
    promedio = suma / 3
    
    if sensor == 0:  # Primer sensor
        sensor_mas_caliente = sensor
        sensor_mas_frio = sensor
        temp_max = promedio
        temp_min = promedio
    else:
        if promedio > temp_max:
            temp_max = promedio
            sensor_mas_caliente = sensor
        if promedio < temp_min:
            temp_min = promedio
            sensor_mas_frio = sensor

print(f"  Sensor más caliente: Sensor {sensor_mas_caliente} ({temp_max:.2f}°C)")
print(f"  Sensor más frío: Sensor {sensor_mas_frio} ({temp_min:.2f}°C)")

print("\n--- ANÁLISIS POR MOMENTO ---")

# 3. Calcular promedio de cada momento (por filas)
print("Temperatura promedio por momento:")
momentos_nombres = ["8:00 AM", "12:00 PM", "6:00 PM"]
for momento in range(3):
    suma_momento = 0
    for sensor in range(4):
        suma_momento += sensores[momento][sensor]
    promedio = suma_momento / 4
    print(f"  {momentos_nombres[momento]}: {promedio:.2f}°C")

# 4. Encontrar el momento más caliente
print("\nComparación de momentos:")
momento_mas_caliente = 0
temp_momento_max = 0

for momento in range(3):
    suma = 0
    for sensor in range(4):
        suma += sensores[momento][sensor]
    promedio = suma / 4
    
    if momento == 0 or promedio > temp_momento_max:
        temp_momento_max = promedio
        momento_mas_caliente = momento

print(f"  Momento más caliente: {momentos_nombres[momento_mas_caliente]} ({temp_momento_max:.2f}°C)")

print("\n--- ANÁLISIS GENERAL ---")

# 5. Estadísticas generales
total_lecturas = 0
suma_total = 0
temp_max_global = sensores[0][0]
temp_min_global = sensores[0][0]
pos_max = (0, 0)
pos_min = (0, 0)

for momento in range(3):
    for sensor in range(4):
        temperatura = sensores[momento][sensor]
        suma_total += temperatura
        total_lecturas += 1
        
        if temperatura > temp_max_global:
            temp_max_global = temperatura
            pos_max = (momento, sensor)
        if temperatura < temp_min_global:
            temp_min_global = temperatura
            pos_min = (momento, sensor)

promedio_global = suma_total / total_lecturas

print(f"Total de lecturas: {total_lecturas}")
print(f"Temperatura promedio global: {promedio_global:.2f}°C")
print(f"Temperatura máxima: {temp_max_global}°C en momento {pos_max[0]}, sensor {pos_max[1]}")
print(f"Temperatura mínima: {temp_min_global}°C en momento {pos_min[0]}, sensor {pos_min[1]}")
print(f"Rango de temperaturas: {temp_max_global - temp_min_global}°C")

# 6. Detectar lecturas inusuales (muy diferentes del promedio)
print(f"\nLecturas que se alejan más de 3°C del promedio ({promedio_global:.2f}°C):")
encontrado_inusual = False
for momento in range(3):
    for sensor in range(4):
        diferencia = abs(sensores[momento][sensor] - promedio_global)
        if diferencia > 3:
            print(f"  Momento {momento}, Sensor {sensor}: {sensores[momento][sensor]}°C (diferencia: {diferencia:.2f}°C)")
            encontrado_inusual = True

if not encontrado_inusual:
    print("  No se encontraron lecturas inusuales")

print("\n=== FIN DEL EJERCICIO 4 ===")