
def cache_decorator(func):
    # Реализовать декоратор который кэширует результаты вызова функции (есть в лекции)
    # Применить для функции calculator (в calculator.py уже есть import функции cache_decorator)
    # Настоятельно прошу написать декоратор руками, а не копировать, т.к. важно запомнить как это работает
    result = None
    prev_args = None
    prev_kwargs = None
    def wrapper(*args, **kwargs):
        nonlocal prev_args
        nonlocal prev_kwargs
        nonlocal result
        if args == prev_args and kwargs == prev_kwargs:
            return result
        else:
            result = func(*args, **kwargs)
            prev_args = args
            prev_kwargs = kwargs
            return result
    return wrapper
