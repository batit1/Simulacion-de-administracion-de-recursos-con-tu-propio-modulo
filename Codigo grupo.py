COSTES = {
    "house": 10000,
    "school": 50000,
    "warehouse": 30000
}

def ordenar_array(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

def sumar_array(arr):
    total = 0
    for num in arr:
        total += num
    return total

def sumar_matriz(matriz):
    total = 0
    for fila in matriz:
        for valor in fila:
            total += valor
    return total

def coste_edificio(tipo):
    if tipo in COSTES:
        return COSTES[tipo]
    else:
        print(f"Tipo de edificio desconocido: {tipo}")
        return 0

def coste_total_proyecto(tipos, cantidades):
    total = 0
    for i in range(len(tipos)):
        tipo = tipos[i]
        cantidad = cantidades[i]
        coste_unitario = coste_edificio(tipo)
        total += coste_unitario * cantidad
    return total


if __name__ == "__main__":
    estructuras = ["house", "school", "warehouse"]
    cantidades = [3, 2, 1]

    print("Estructuras originales:", estructuras)
    print("Estructuras ordenadas:", ordenar_array(estructuras.copy()))
    print("Coste total del proyecto:", coste_total_proyecto(estructuras, cantidades))


    matriz_recursos = [
        [100, 200, 300],
        [400, 500],
        [600]
    ]
    print("Suma total de recursos en matriz:", sumar_matriz(matriz_recursos))
