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

zer = np.zeros((2, 3), dtype = int)
ones = np.ones((2, 3), dtype = float)
f = np.full((2, 3), 10)
# print(f)
# print(zer)
# print(ones)

g = np.arange(3)
# print(g)
g2 = np.arange(3, 7)
# print(g2)
g3 = np.arange(3, 8, 2)
# print(g3)

# срезы
# item[start:stop:step]
i1 = np.array([1, 3, 8, 7])
# print(i1[:])
# print(i1[2:])
# print(i1[:-1])
# print(i1[::-1])

i2 = [1, 3, 6, 7]
i2[1:3] = [0, 0, 0]# с numpy.array не работает
# print(i2)







