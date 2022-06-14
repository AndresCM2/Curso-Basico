from sys import dllhandle
from turtle import st


def conversor(tipo_pesos,valor_dolar):
    pesos=input("¿Cuantos pesos " + tipo_pesos + " tiene?")
    pesos=float(pesos)  
    dolares=pesos/valor_dolar
    dolares=float(round(dolares,2))
    dolares=str(dolares)
    print("Tienes $" + dolares + " dólares")

menu = """
Bienvenido al conversor de monedas multipais

1-Pesos Mexicanos
2-Pesos Colombianos
3-Pesos Argentinos

Elige una o1pción: 

"""
opcion = int(input(menu))

if opcion == 1: #pesos mexicanos
    conversor("Colombianos",3875)
elif opcion == 2: #pesos colombianos
    conversor("Argentinos",65)
elif opcion == 3: #pesos argentinos
    conversor("Mexicanos",24)
else:  #el usuario escribió algo diferente
	print('Escribe una opción correcta: ')


