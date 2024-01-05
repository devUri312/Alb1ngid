class Calculator:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

    def __sub__(self, other):
        return self.value - other.value

    def __mul__(self, other):
        return self.value * other.value

    def __truediv__(self, other):
        if other.value != 0:
            return self.value / other.value
        else:
            raise ValueError("Деление на ноль невозможно.")

num1 = Calculator(10)
num2 = Calculator(5)

result_add = num1 + num2
result_sub = num1 - num2
result_mul = num1 * num2
result_div = num1 / num2

print(f"Сложение: {result_add}")
print(f"Вычитание: {result_sub}")
print(f"Умножение: {result_mul}")
print(f"Деление: {result_div}")
