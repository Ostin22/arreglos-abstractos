"""
Ejercicio 5: Transformaciones Básicas de Coordenadas
Objetivo: Aprender operaciones básicas con puntos en una tabla 2D
"""

# Lista de puntos [x, y] que forman un triángulo simple
puntos_originales = [
    [1, 1],  # Punto A
    [4, 1],  # Punto B  
    [2, 3]   # Punto C
]

print("=== EJERCICIO 5: COORDENADAS ===")
print("\nPuntos originales del triángulo:")
for i in range(3):
    x = puntos_originales[i][0]
    y = puntos_originales[i][1]
    print(f"  Punto {i}: ({x}, {y})")

print("\n--- TRANSFORMACIÓN 1: TRASLACIÓN ---")
print("Mover todos los puntos 2 unidades a la derecha y 1 hacia arriba")

# Crear nueva lista para puntos trasladados
puntos_trasladados = []
desplazamiento_x = 2
desplazamiento_y = 1

for i in range(3):
    x_original = puntos_originales[i][0]
    y_original = puntos_originales[i][1]
    
    x_nuevo = x_original + desplazamiento_x
    y_nuevo = y_original + desplazamiento_y
    
    puntos_trasladados.append([x_nuevo, y_nuevo])

print("Puntos después de traslación:")
for i in range(3):
    x_orig = puntos_originales[i][0]
    y_orig = puntos_originales[i][1]
    x_nuevo = puntos_trasladados[i][0] 
    y_nuevo = puntos_trasladados[i][1]
    print(f"  Punto {i}: ({x_orig}, {y_orig}) → ({x_nuevo}, {y_nuevo})")

print("\n--- TRANSFORMACIÓN 2: ESCALADO ---")
print("Hacer el triángulo 2 veces más grande")

# Escalar desde el origen (0,0)
puntos_escalados = []
factor_escala = 2

for i in range(3):
    x_original = puntos_originales[i][0]
    y_original = puntos_originales[i][1]
    
    x_escalado = x_original * factor_escala
    y_escalado = y_original * factor_escala
    
    puntos_escalados.append([x_escalado, y_escalado])

print("Puntos después de escalado:")
for i in range(3):
    x_orig = puntos_originales[i][0]
    y_orig = puntos_originales[i][1]
    x_escalado = puntos_escalados[i][0]
    y_escalado = puntos_escalados[i][1]
    print(f"  Punto {i}: ({x_orig}, {y_orig}) → ({x_escalado}, {y_escalado})")

print("\n--- ANÁLISIS GEOMÉTRICO ---")

# Calcular centro del triángulo original
suma_x = 0
suma_y = 0
for i in range(3):
    suma_x += puntos_originales[i][0] 
    suma_y += puntos_originales[i][1]

centro_x = suma_x / 3
centro_y = suma_y / 3
print(f"Centro del triángulo original: ({centro_x:.2f}, {centro_y:.2f})")

# Calcular centro del triángulo trasladado
suma_x_tras = 0
suma_y_tras = 0
for i in range(3):
    suma_x_tras += puntos_trasladados[i][0]
    suma_y_tras += puntos_trasladados[i][1]

centro_x_tras = suma_x_tras / 3
centro_y_tras = suma_y_tras / 3
print(f"Centro del triángulo trasladado: ({centro_x_tras:.2f}, {centro_y_tras:.2f})")

# Verificar que el desplazamiento del centro coincide con la traslación
desplaz_centro_x = centro_x_tras - centro_x
desplaz_centro_y = centro_y_tras - centro_y
print(f"Desplazamiento del centro: ({desplaz_centro_x:.2f}, {desplaz_centro_y:.2f})")
print(f"Traslación aplicada: ({desplazamiento_x}, {desplazamiento_y})")

print("\n--- CÁLCULO DE DISTANCIAS ---")

# Calcular distancia entre dos puntos (Punto 0 y Punto 1)
def calcular_distancia(punto1, punto2):
    dx = punto2[0] - punto1[0]
    dy = punto2[1] - punto1[1]
    distancia = (dx * dx + dy * dy) ** 0.5  # Raíz cuadrada
    return distancia

dist_original = calcular_distancia(puntos_originales[0], puntos_originales[1])
dist_escalada = calcular_distancia(puntos_escalados[0], puntos_escalados[1])

print(f"Distancia entre punto 0 y 1 (original): {dist_original:.2f}")
print(f"Distancia entre punto 0 y 1 (escalado): {dist_escalada:.2f}")
print(f"Factor de escalado calculado: {dist_escalada / dist_original:.2f}")

print("\n--- CREAR TRANSFORMACIÓN COMBINADA ---")
print("Aplicar escalado Y DESPUÉS traslación")

# Primero escalar, después trasladar
puntos_combinados = []

for i in range(3):
    # Paso 1: Escalar
    x_escalado = puntos_originales[i][0] * factor_escala
    y_escalado = puntos_originales[i][1] * factor_escala
    
    # Paso 2: Trasladar
    x_final = x_escalado + desplazamiento_x
    y_final = y_escalado + desplazamiento_y
    
    puntos_combinados.append([x_final, y_final])

print("Puntos con transformación combinada (escalar → trasladar):")
for i in range(3):
    x_orig = puntos_originales[i][0]
    y_orig = puntos_originales[i][1]
    x_final = puntos_combinados[i][0]
    y_final = puntos_combinados[i][1]
    print(f"  Punto {i}: ({x_orig}, {y_orig}) → ({x_final}, {y_final})")

print("\n--- TABLA COMPARATIVA ---")
print("Punto | Original | Trasladado | Escalado | Combinado")
print("------|----------|------------|----------|----------")
for i in range(3):
    orig = puntos_originales[i]
    tras = puntos_trasladados[i] 
    esc = puntos_escalados[i]
    comb = puntos_combinados[i]
    print(f"  {i}   | ({orig[0]}, {orig[1]})   | ({tras[0]}, {tras[1]})     | ({esc[0]}, {esc[1]})    | ({comb[0]}, {comb[1]})")

print("\n=== FIN DEL EJERCICIO 5 ===")