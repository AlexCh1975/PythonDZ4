# 4.* Задана натуральная степень k. Сформировать случайным образом список коэффициентов (от 0 до 10) многочлена, записать в файл полученный многочлен не менее 3-х раз.
# in
# 9
# 5
# 3

# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0

# in
# 0
# -1
# 4

# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0
# 2*x^4 - 3*x^3 + 3*x^2 + 1*x^1 - 2 = 0

from encodings import utf_8
import random


def create_polynomial(k):
    with open('task_004/out.txt', 'a', encoding='utf_8') as data:
        temp = []
    
        while k > 0:
            coefficient = random.randint(0, 9)
            sign = ['+', '-']
            random.shuffle(sign)
            if coefficient:
                temp.append("{0}x^{1} {2}".format(coefficient, k, sign[0]))
            k -= 1
        coefficient = random.randint(0, 9)
       
        data.write(" ".join(temp))
        data.write("\n")

list1 = [9, 5, 3 , 4]

for i in range(len(list1)):
    create_polynomial(list1[i])

