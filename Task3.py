def add_digits_to_set(input_set):
    # Перевіряємо, чи є цифри у вхідній множині
    digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    if not any(digit in input_set for digit in digits):
        # Якщо в множині немає жодної цифри, додаємо цифри до списку
        input_set = list(input_set)
        input_set.extend(digits)
        # Перетворюємо список назад у множину
        input_set = set(input_set)
    return input_set

# Вхідна множина
input_set = {'c', 'd'}
# Виклик функції для додавання цифр до множини
result_set = add_digits_to_set(input_set)
# Друк результату
print("Результат:", result_set)
