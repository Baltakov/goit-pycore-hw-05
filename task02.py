import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[float, None, None]:
    # Регулярний вираз для пошуку дійсних чисел, відокремлених пробілами
    pattern = re.compile(r'\b\d+\.\d+\b')
    # Знаходимо всі збіги в тексті
    matches = pattern.findall(text)
    # Ітеруємо по всіх знайдених числах
    for match in matches:
        yield float(match)

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    # Використовуємо генератор для отримання всіх чисел і підсумовуємо їх
    return sum(func(text))

# Приклад використання
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
