# 사칙연산 함수 정의
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero is not allowed"

def power(a, b):
    return a ** b


def mod(a, b):
    return a%b

# 테스트 코드
if __name__ == '__main__':
    a = 5
    b = 10

    print(f"{a} + {b} = {add(a, b)}")
    print(f"{a} - {b} = {subtract(a, b)}")
    print(f"{a} * {b} = {multiply(a, b)}")
    print(f"{a} / {b} = {divide(a, b)}")
