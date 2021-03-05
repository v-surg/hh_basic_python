# from decorators import cache_decorator

class IlleagalOperaonException(Exception):
    pass


operations = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
    '**': lambda a, b: a ** b,
}

def calculator(a, b, operation):
    # Здесь нужно реализовать функцию,
    # которая реализует основные арифметические операции между числами: +, -, /, *, **.
    # Так же следует сделать проверку, что поступивший оператор корректен (присутствует в этом списке +, -, /, *, **)

    if operation not in operations:
        raise IlleagalOperaonException("Unsupported operation")
    else:
        return operations[operation](a, b)


if __name__ == '__main__':

    try:
        a = int(input('Введите число: '))  # Тут было бы неплохо обрабатывать ошибку в случае передачи некорректных символов
        b = int(input('Введите число: '))
        operation = input('Введите операцию')
        print('Результат: ', calculator(a, b, operation))
    except IlleagalOperaonException as e:
        print("Операция не поддерживается")
    except ValueError as e:
        print("Недопустимое значение переменной")
    except ZeroDivisionError as e:
        print("Деление не ноль")
