def search_and_print(word, word_list):
    print("Список:")
    for w in word_list:
        print(w)

    found = False
    for w in word_list:
        if w.lower() == word.lower():  # Порівняння без урахування регістру
            found = True
            break
    if found:
        print(f"Слово '{word}' знайдено у списку.")
    else:
        print(f"Слово '{word}' не знайдено у списку.")

# Функція для введення списку з клавіатури
def input_list():
    word_list = []
    n = int(input("Введіть кількість слів у списку: "))
    for i in range(n):
        word = input(f"Введіть слово {i+1}: ")
        word_list.append(word)
    return word_list

# Приклад використання:
word_list = input_list()
search_word = input("Введіть слово для пошуку: ")
search_and_print(search_word, word_list)
