import sys
import os
import numpy as np
from scipy.spatial.distance import pdist

def main():
    if len(sys.argv) < 2:
        print("Uso: python programa.py datos.txt")
        sys.exit(1)

    filename = sys.argv[1]

    # Verificar que el archivo exista
    if not os.path.exists(filename):
        print(f"El archivo '{filename}' no fue encontrado. Verifica la ruta y el nombre del archivo.")
        sys.exit(1)

    try:
        # Se asume que el archivo contiene tres columnas de números separados por espacios o tabulaciones
        points = np.loadtxt(filename)
    except Exception as e:
        print(f"Error al leer el archivo '{filename}': {e}")
        sys.exit(1)
    
    # Verificar que el archivo tenga tres columnas
    if points.ndim != 2 or points.shape[1] != 3:
        print("El archivo debe contener tres columnas con las coordenadas de los puntos.")
        sys.exit(1)

    # Calcular todas las distancias entre pares de puntos de forma vectorizada
    distances = pdist(points)
    
    # Calcular la distancia promedio
    average_distance = np.mean(distances)
    
    print("La distancia promedio entre los puntos es:", average_distance)

if __name__ == '__main__':
    main()
