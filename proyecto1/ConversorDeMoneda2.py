menu="""
Bienvenido al conversor de monedas diner

Elige un opcion segun el Pais:

1- Pesos Colombianos
2- Pesos Argentinos
3- Peses Mexicanos

Elige una opción
"""
opcion=int(input(menu))
         
if opcion==1:
    C="Pesos Colombianos"
    op=C
    moneda=float(input(f"¿Cuantos {op} tienes?"))
    print(C)
elif opcion ==2:
    A="Pesos Argentinos"
    op=A
    moneda=float(input(f"¿Cuantos {op} tienes?"))
    print(A)
elif opcion == 3:
    M="Pesos Mexicanos"
    op=M
    moneda=float(input(f"¿Cuantos {op} tienes?"))
    print(M)
else:
    N="nada"
    op=N

C="Pesos Colombianos"
A="Pesos Argentinos"
M="Pesos Mexicanos"


if op==C:
    valor_dolar=3875
    dolares=str(round(moneda/valor_dolar,2))
    print(f"Tiene $ {dolares} dolares convertidos con {op}")
elif op==A:
    valor_dolar=3875
    dolares=str(round(moneda/valor_dolar,2))
    print(f"Tiene $ {dolares} dolares convertidos con {op}")
elif op==M:
    valor_dolar=3875
    dolares=str(round(moneda/valor_dolar,2))
    print(f"Tiene $ {dolares} dolares convertidos con {op}")
else:
    print("Ingresa una opción correcta por favor")
    