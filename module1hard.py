grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list({'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'})
students.sort()

A = sum(grades[0]) / 5
B = sum(grades[1]) / 4
J = sum(grades[2]) / 4
K = sum(grades[3]) / 3
S = sum(grades[4]) / 5

journal = {}
journal[students[0]] = A
journal[students[1]] = B
journal[students[2]] = J
journal[students[3]] = K
journal[students[4]] = S
print(journal)
