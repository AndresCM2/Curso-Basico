def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 1:
            divisors.append(i)
    return divisors


def run():
    num = int(input('Ingresa un número: '))
    assert num.isnumeric(num), "Debes ingresar un numero"
    print(divisors(int(num)))
    print("Terminó mi programa")


if __name__ == '__main__':
    run()