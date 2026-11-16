import numpy as np
#1
hours = np.arange(0,22,3)
line = np.linspace(0,1,5)
zeros = np.zeros(6, dtype=int)
unknown_table = np.full((2,3),-1)
identity = np.eye(3)
print(f'''\nhours = {hours}, shape = {hours.shape}, ndim = {hours.ndim},
size = {hours.size}, dtype = {hours.dtype}''')
#2
print(f'''\n3 эл. - {hours[2]}, последний эл. - {hours[-1]}, эл. 2-5 - {hours[2:6]},
каждый 2ой эл. - {hours[1::2]}, в обратном порядке - {hours[::-1]}''')
#3
temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])
c = temperatures[:2,1:3]
print(f'''\nформа - {temperatures.shape},
число измерений - {temperatures.ndim},
число эл. - {temperatures.size},
2 строка 3 столбец - {temperatures[1,2]},
1 строка - {temperatures[0]},
последний столбец - {temperatures[:,-1]},
строки 1-2 без 1 столбца - {temperatures[:2,1:]},
центральный фрагмент 2×2 - {c}
Проверка: {c.shape}''')
print()
#4
matrix = np.arange(1, 26).reshape(5, 5)
a1,a2,a3,a4,a5 = matrix[:3],matrix[-2:],matrix[:,:2],matrix[1:4,2:5],matrix[-2:,-2:]
print(f'''\nстроки 1-3: {a1}{a1.shape},
строки 4-5: {a2}{a2.shape},
столбцы 1-2: {a3}{a3.shape},
строки с инд. 1-3 столбцы с инд. 2-4: {a4}{a4.shape},
блок 2*2 в правим нижнем углу: {a5}{a5.shape}''')
#5
vector = np.array([10, 20, 30, 40, 50])
vector[1:4] = 0

small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9

changed_hours = hours.copy()
changed_hours[2:5] = 99
changed_hours[::2] = -1
print(f'''\nchanged_hours = {changed_hours},
hours = {hours}''')
#Если не использовать .copy(), то обе переменные будут указывать на один и тот же массив
changed_matrix = matrix.copy()
changed_matrix[1,:] = 0
changed_matrix[:,-1] = -1
changed_matrix[1:4,1:4] = 100
print(f'''\nchanged_matrix = {changed_matrix},
matrix = {matrix}''')
print()
#6
numbers = np.arange(0,12)
table = numbers.reshape(3,4)
transposed = table.T
print(numbers.shape,table.shape,transposed.shape)
#reshape(5, 3) вызовет ошибку, потому что в numbers толбко 12 эл., а метод требует 15

