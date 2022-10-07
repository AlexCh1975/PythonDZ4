# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# in                   
# 54

# out
# [2, 3, 3, 3]

# in
# 9990

# out
# [2, 3, 3, 3, 5, 37]

# in
# 650

# out
# [2, 5, 5, 13] 

def get_prime_factors(num):
   i = 2
   my_list = []
#    while i * i <= num:
#        while num % i == 0:
#            my_list.append(i)
#            num = num / i
#        i = i + 1
#    if num > 1:
#        my_list.append(int(num))
   while num > 1:
    if num % i == 0:
        my_list.append(i)
        num //= i
    else: i += 1

   return my_list

arr =get_prime_factors(int(input()))
print(arr)
