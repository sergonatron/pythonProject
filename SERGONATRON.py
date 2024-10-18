# Получение коэффициентов
first_coefficient = int(input('a = ', ))
second_coefficient = int(input('b = ', ))
third_coefficient = int(input('c = ', ))

# Решение по сокращенной формуле, т.к. b - четное
if first_coefficient != 0 and second_coefficient % 2 == 0 and third_coefficient != 0:
    k = second_coefficient / 2
    d1 = k ** 2 - first_coefficient * third_coefficient
    root_1 = (-k + d1 ** 0.5) / first_coefficient
    root_2 = (-k - d1 ** 0.5) / first_coefficient

    print('Так как второй коэффициент - четное число, решаем по сокращенной формуле')
    print(f'Первый корень: {root_1}')
    print(f'Второй корень: {root_2}')

# Решение уравнения при с = 0
if first_coefficient != 0 and third_coefficient == 0 and second_coefficient != 0:
    print(f'корень уравнения равен либо нулю, либо {-second_coefficient / first_coefficient}')

# Решение уравнения при b = 0 и c = 0
if first_coefficient != 0 and second_coefficient == 0 and third_coefficient == 0:
    print(f'корни уравнения равны нулю, peremennaya1 * x ** 2 = 0')

# Решение полного уравнения
if first_coefficient != 0 and second_coefficient % 2 != 0 and third_coefficient != 0:
    d = second_coefficient ** 2 - 4 * first_coefficient * third_coefficient
    if d > 0:
        root_1 = (-second_coefficient + d ** 0.5) / (2 * first_coefficient)
        print(f'дискриминант равен: {d}')
        print(f'первый корень равен: {round(root_1, 2)}')
        root_2 = (-second_coefficient - d ** 0.5) / (2 * first_coefficient)
        print(f'второй корень равен: {round(root_2, 2)}')
    elif d < 0:
        print(f'так как дискриминант меньше нуля и равен: {d}')
        print('действительных корней нет')
    else:
        k = -second_coefficient / (2 * first_coefficient)
        print(f'уравнение имеет один корень: {k}')

        # решение уравнения при b = 0
        if first_coefficient != 0 and third_coefficient != 0 and second_coefficient == 0:
            if (- third_coefficient / first_coefficient) >= 0:
                root_1 = (-third_coefficient / first_coefficient) ** 0.5
                print(f'первый корень равен: {root_1}')
                root_2 = (-1) * ((-third_coefficient / first_coefficient) ** 0.5)
                print(f'второй корень равен: {root_2}')
        if (- third_coefficient / first_coefficient) < 0:
            print(
                f' -c / peremennaya1 = : {-third_coefficient / first_coefficient}, '
                f'т.е. < 0, поэтому действительных корней нет')
