
import random

# Generar 1000 números aleatorios entre -1000 y 1000
ordenada = []
for _ in range(1000):
    ordenada.append(random.randint(-1000, 1000))

# Mostrar los primeros números random antes de ordenar
print("=== NÚMEROS ALEATORIOS (antes de ordenar) ===")
print(f"Primeros 20 números random: {ordenada[:10]}")
print(f"Últimos 20 números random: {ordenada[-10:]}")
print(f"Total de números generados: {len(ordenada)}")
print()

# Ordenar de forma ascendente usando el método de burbuja
for i in range(len(ordenada)):
    for j in range(0, len(ordenada) - i - 1):
        if ordenada[j] > ordenada[j + 1]:
            # Intercambiar valores
            ordenada[j], ordenada[j + 1] = ordenada[j + 1], ordenada[j]
            
            
print("=== NÚMEROS ORDENADOS (después de ordenar) ===")
print(f"Primeros 20 números ordenados: {ordenada[:10]}")
print(f"Últimos 20 números ordenados: {ordenada[-10:]}")
print(f"Número más pequeño: {ordenada[0]}")
print(f"Número más grande: {ordenada[-1]}")

