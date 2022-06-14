# Dicionarion compresiones

## Conceptualizacion Dicionario comprasión
![Dicionario compresiones](https://i.ibb.co/nMDSG6X/DICIONARIOCOMPRESIONES1.png)

## Ejemplo
![Dicionario compresiones](https://i.ibb.co/CMswhpV/LISTA-DE-COMPRESIONES.png)

> Ejemplo codigo largo
```py
def run():
    my_dict = {}

    for i in range(1, 101):
        if i % 3 !=0:
            my_dict[i] = i**2

    print(my_dict)
    print(my_dict)


if __name__ == "__main__":
    run()
```
>Ejemplo comprimido
```py
def run():
  
    my_dict = {i: i**3 for i in range(1, 101) if i % 3 != 0}
    print(my_dict)


if __name__ == "__main__":
    run()
```