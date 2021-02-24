#!/usr/bin/env python3


def fib(n):
    """O(n) Loesung."""
    try:
        assert n >= 0
    except AssertionError:
        raise ValueError("Der Eingang muss positiv sein.")

    if 0 <= n < 2:
        return n

    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a+b

    return b


def main():
    numbers = []
    while n := input():
        try:
            n = int(n)
            numbers.append(n)
        except ValueError:
            print(f'Überspringen {n}: keine gültige Ganzzahl.')

    for num in numbers:
        print(f'Die Fibonacci Zahl für {num} ist: {fib(num)}')


if __name__ == '__main__':
    main()
