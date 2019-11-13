def divideBy(denom):
    return 42/denom


try:
    print(divideBy(2))
    print(divideBy(12))
    print(divideBy(0))
    print(divideBy(1))
except ZeroDivisionError:
    print('Error. Invalid argument.')
