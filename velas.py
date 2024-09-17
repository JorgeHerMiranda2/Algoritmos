def velas(a: list[int]) -> int:
    """
  Args:
        a (list[int]): The candles heights.
    
    Returns:
        int: The number of candles that are tallest
    """
    altura_max = max(a)
    contador = 0
    for altura in a:
        if altura == altura_max:
            contador += 1
    return contador

# Ejemplos de uso
velas_alturas = [4, 4, 1, 3]
resultado = velas(velas_alturas)
print(resultado) 
if __name__ == "__main__":
    print(velas([4, 4, 1, 3])) # 2
    print(velas([1, 1, 1, 1, 1])) # 5
    print(velas([5, 3, 1, 3, 5, 3, 1, 3, 5])) # 3
    print(velas([10000, 10001, 10002, 10002, 10000]))#2
    print(velas([999, 1000, 99, 912, 100])) # 1