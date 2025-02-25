ERROR_DIVISION_BY_ZERO = "0으로 나눌 수 없습니다"  # 추출된 상수


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    return ERROR_DIVISION_BY_ZERO


def power(num1, num2):
    return num1 ** num2


def mod(num1, num2):
    return num1 % num2


def print_operations(num1, num2):  # 추출된 재사용 가능 함수
    print(f"{num1} + {num2} = {add(num1, num2)}")
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
    print(f"{num1} / {num2} = {divide(num1, num2)}")
    print(f"{num1} ** {num2} = {power(num1, num2)}")
    print(f"{num1} % {num2} = {mod(num1, num2)}")


