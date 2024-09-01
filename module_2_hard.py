def result(n):
    password = ''
    for i in range(1, n):
        for j in range(i + 1, n):
            if n % (i + j) == 0:
                password += str(i) + str(j)
    return password

print('Введите число: ')
print(result(int(input())))