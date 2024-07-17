def caching_fibonacci():
    # Створюємо порожній словник для кешу
    cache = {}

    def fibonacci(n):
        # Базові випадки
        if n <= 0:
            return 0
        if n == 1:
            return 1
        
        # Перевіряємо, чи є значення в кеші
        if n in cache:
            return cache[n]
        
        # Рекурсивно обчислюємо число Фібоначчі і зберігаємо в кеші
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    # Повертаємо внутрішню функцію fibonacci
    return fibonacci

# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610
