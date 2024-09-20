def sumaPares(matriz, n):
    #input: la matriz nxn
    #output: la suma de todos los numeros pares de la matriz
    
    suma = 0
    n = 3
   
    
    # i son las filas, j las columnas 
    
    for i in range(n):
        for j in range(n):
            if (matriz[i][j] % 2)  == 0:
                suma += matriz[i][j]
    
    return suma

A = [
    [0, 2, 1],
    [1, 2, 0],
    [0, 2, 1]
]


print(sumaPares(A, n)) 