# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.
# in
# 7

# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]

# in
# -1

# out
# Negative value of the number of numbers!
# []

# in
# 10

# out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]

from random import randint 


def create_list(size):
    if size < 0: 
        print("Negative value of the number of numbers!")

    my_list = [randint(1, 10) for i in range(size)]
    return my_list

def get_non_repeating_elements(my_list: list):
    temp = []
    
    for i in range(len(my_list)):
        if my_list.count(my_list[i]) == 1:
            temp.append(my_list[i])
    return temp         


my_list = create_list(int(input("Размер списка: ")))
print(my_list)
new_list = get_non_repeating_elements(my_list)
print(new_list)