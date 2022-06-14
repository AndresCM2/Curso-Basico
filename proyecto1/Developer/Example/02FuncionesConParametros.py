
def conversacion (mensaje):
    print("Hola")
    print("Como estas")
    print(mensaje)
    print("Como estas")

option=int(input("Elige una option(1.2.3)"))
if option==1:
   conversacion("Elegiste la opcion 1")
elif option==2:
   conversacion("Elegiste la opcion 2")
elif option==3:
   conversacion("Elegiste la opcion 3")
else:
    print("Esta es la option correcto")
    