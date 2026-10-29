# src/calculos.py

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("Erro: Divisão por zero!")
    return a / b

def potencia(base, expoente):
    return base ** expoente

def raiz_quadrada(numero):
    if numero < 0:
        raise ValueError("Erro: Raiz quadrada de número negativo!")
    return numero ** 0.5

def porcentagem(valor, percentual):
    return (valor * percentual) / 100