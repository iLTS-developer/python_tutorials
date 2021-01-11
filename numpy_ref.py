import numpy as np

a = np.array([2, 4, 7])
b = np.array([5, 2, 4])

sc = np.dot(a, b)# скалярное произв.
# print(sc)

na = np.linalg.norm(a)# евклидова норма вектора
# print(na)

inn = np.inner(a, b)# скалярное произв.
# print(inn)

out = np.outer(a, b)# матрица попарных произведений элементов a, b
#print(out)

c = np.array([[3, 5, 8], [4, 2, 7], [8, 1, 6]])
d = np.array([[2, 4, 6], [3, 6, 1], [5, 7, 2]])
mul = np.matmul(c, d)# произведение матриц
# print(mul)

e = np.eye(2)# возвращает единичную матрицу размера 2
# print(e)

detc = np.linalg.det(c)
# print(detc)

rnk = np.linalg.matrix_rank(d)
# print(rnk)

x = np.linalg.solve(c, a)#  решает лин.ур. или систему лин.ур.
# с - коэффициенты, а - свб.члены
# print(x)

