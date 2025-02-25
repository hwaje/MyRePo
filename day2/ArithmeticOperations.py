ERROR_DIVISION_BY_ZERO = "0으로 나눌 수 없습니다"  # 에러 메시지 상수
MESSAGE_ERROR_DIVISION = "나눌 수 없는 값"  # 추가 메시지 상수


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    is_valid_divisor = num2 != 0  # 조건문 변수화
    if is_valid_divisor:
        return num1 / num2
    return ERROR_DIVISION_BY_ZERO


def power(num1, num2):
    return num1 ** num2


def mod(num1, num2):
    return num1 % num2


def format_operation_result(num1, num2, operation, result):  # 출력 형식 추출 함수
    return f"{num1} {operation} {num2} = {result}"


def display_operations(num1, num2):  # 함수 이름 변경
    print(format_operation_result(num1, num2, "+", add(num1, num2)))
    print(format_operation_result(num1, num2, "-", subtract(num1, num2)))
    print(format_operation_result(num1, num2, "*", multiply(num1, num2)))
    print(format_operation_result(num1, num2, "/", divide(num1, num2)))
    print(format_operation_result(num1, num2, "**", power(num1, num2)))
    print(format_operation_result(num1, num2, "%", mod(num1, num2)))
