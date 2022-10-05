# 5. ** Даны два файла, в каждом из которых находится запись многочленов. Задача - сформировать файл, содержащий сумму многочленов.
# in
# "poly.txt"
# "poly_2.txt"

# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 + 2*x^2 + 2*x^1 + 2 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 + 3*x^3 - 4*x^2 - 2*x^1 - 4 = 0
# 4*x^2 - 4 + 3*x^6 - 4*x^5 - 4*x^4 - 4*x^3 + 3*x^2 - 2*x^1 - 0 = 0

# in
# "poly.txt"
# "poly_2.txt"

# out
# The contents of the files do not match! 

def get_sum_polynomial():
    data1 = open('task_005/poly.txt', 'r', encoding='utf_8')
    data2 = open('task_005/poly_2.txt', 'r', encoding='utf_8')

    polynomial1 = data1.read()
    p1 = polynomial1.split(sep='\n')
    polynomial2 = data2.read()
    p2 = polynomial2.split(sep='\n')
    print(p1)
    print(p2)
    with open('task_005/out.txt', 'a', encoding='utf_8') as data_save:
        if len(p1) == len(p2): 
            data1.close()
            data2.close()
            
            polynomial = []
            for i in range(len(p1)):
                p1[i] = p1[i].replace(' = 0', "+")
                polynomial.append(p1[i] + p2[i])
                
                data_save.write('\n\n'.join(polynomial))
        else:
            print("The contents of the files do not match!")            
            data_save.write('\nThe contents of the files do not match!\n')

get_sum_polynomial()