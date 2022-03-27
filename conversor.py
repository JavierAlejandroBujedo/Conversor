pesos = input("¿Cuántos pesos Argentinos tienes?: ")
pesos = float(pesos)
valor_dolar = 202
dolares = pesos / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print("Tienes $ " + dolares + " dólares")

