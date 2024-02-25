def split_list_by_attribute(input_list, attribute_value):
    list1 = []
    list2 = []
    for item in input_list:
        if 'name' in item and item['name'] == attribute_value:
            list1.append(item)
        else:
            list2.append(item)
    return list1, list2



def main():
    input_list = []
    while True:
        item = input("Введіть елемент списку у форматі {'attribute': value}: ")
        if item.lower() == 'done':
            break
        try:
            input_list.append(eval(item))
        except:
            print("Неправильний формат. Спробуйте ще раз.")

    attribute_value = input("Введіть значення атрибуту для розбиття списку: ")

    list1, list2 = split_list_by_attribute(input_list, attribute_value)

    print("Список 1:")
    print(list1)
    print("Список 2:")
    print(list2)


if __name__ == "__main__":
    main()
