#Функция вычисления суммы четных чисел
def summa_even():
    even_list = [number * 2 for number in range(1, 51)]
    return sum(even_list)


#Функция списка квадратов нечетных чисел
def create_list_square():
    odd = [1, 3, 5, 7, 9]
    list_square = [number ** 2 for number in odd]
    return list_square


#Функция ввода чисел
def entering_numbers():
    number = 0
    counting = 0
    while number >= 0:
        try:
            number = int(input("Введите число: "))
            counting += 1
        except ValueError:
            print("Ошибка! Введено не число!")
    return counting


#Основное тело программы
print("Сумма четных чисел от 1 до 100: ", summa_even())
print("Список квадратов нечетных чисел", create_list_square())
print("Количество введеных чисел: ", entering_numbers())