from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')


def calculate_square_root(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number):
    """Принимает число и проводит его сравнение."""
    result = calculate_square_root(your_number)
    if your_number <= 0:
        print('Выберите число больше нуля.')

    print(f'Мы вычислили квадратный корень'
          f'из введённого вами числа. '
          f'Это будет: {result}')


print(message)
calc(25.5)