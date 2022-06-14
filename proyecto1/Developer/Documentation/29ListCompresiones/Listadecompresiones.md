# list de compresiones

## Conceptualizacion
![lista de compresiones1](https://i.ibb.co/CMswhpV/LISTA-DE-COMPRESIONES.png)

## Ejemplo

![lista de compresiones2](https://i.ibb.co/44CWpNV/LISTA-DE-COMPRESIONES2.png)


>Ejemplo largo

```py
def run():
    squares = []

    for i in range(1, 101):
        if i % 3 != 0:
            squares.append(i**2)

    print(squares)


if __name__ == "__main__":
    run()
```
>Ejemplo Compresión
```py
def run():
    my_list = [i for i in range(1, 100000) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]
    print(my_list)


if __name__ == '__main__':
    run()
```