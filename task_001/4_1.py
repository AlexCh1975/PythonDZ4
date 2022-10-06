# Вычислить число с заданной точностью d.

# in Enter a real number: 9
#    Enter the required accuracy '0.0001': 0.000001
# out 9.000000

# in Enter a real number: 8.98765
#    Enter the required accuracy '0.0001': 0.001
# out 8.988

from decimal import *

def get_num_with_precision(num, accuracy):
    num = Decimal(num).quantize(Decimal(accuracy), rounding=ROUND_UP)
    return num

num = input("Число: ")
accuracy = input("Точность: ")   
print(input(get_num_with_precision(num, accuracy)))
