def duplicados (numeros):
    
    if not numeros:
        return [], 0

    # Inicializamos un puntero 
    j = 1
    for i in range(1, len(numeros)):
        if numeros[i] != numeros[i - 1]:
            numeros[j] = numeros[i]
            j += 1

    return numeros[:j], j