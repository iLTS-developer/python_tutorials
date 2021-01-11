%matplotlib inline

from sklearn.datasets import load_iris
import math as m
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as clrs
import random as rand
import copy

# просто контейнер для данных
class DsStorage:
    def __init__(self):
        self.X = load_iris().data
        self.Y = load_iris().target
        self.N_obj = len(self.X)
        self.N_attr = len(self.X[0])


class MyClustering:

    x0 = set()  # номера обьектов - начальных центров
    qual = 0.0  # функционал качества

    def __init__(self, ds, ncl):
        self.Y_new = np.empty(shape=(ds.N_obj), dtype=int)
        self.x1 = np.zeros(shape=(ncl, ds.N_attr))
        self.x1_cnt = np.zeros(shape=(ncl))
        self.q = np.zeros(shape=(ncl))
        self.ncl = ncl

    # начальная инициалзация центров
    def gen_sp(self, N_obj):
        self.x0.clear()
        rand.seed()
        for i in range(0, self.ncl):
            r_int = rand.randint(0, N_obj)
            if r_int in self.x0:
                i -= 1
                continue
            self.x0.add(r_int)
            self.Y_new[r_int] = i

    def sqr_dist(self, x1, x2):
        d = 0.0
        for i in range(len(self.x1[0])):
            d += (x2[i] - x1[i]) ** 2
        return d

    def dist(self, x1, x2):
        return m.sqrt(self.sqr_dist(x1, x2))

    # начальное разбиение
    def st_cl(self, N_obj, data):
        l = []
        for i in range(N_obj):
            for j in self.x0:
                l.append([self.dist(data[i], data[j]), j])
            lmin = min(l, key=lambda a: a[0])
            self.Y_new[i] = self.Y_new[lmin[1]]
            l.clear()

    # обновление центров
    def upd_c(self, N_obj, data):
        for i in range(N_obj):
            for j in range(len(self.x1[0])):
                self.x1[self.Y_new[i]][j] += data[i][j]
            self.x1_cnt[self.Y_new[i]] += 1.0
        for i in range(self.ncl):
            if self.x1_cnt[i] == 0:
                r_new = rand.randint(0, 149)
                self.x1[i] = copy.deepcopy(data[r_new])
                continue
            for j in range(len(self.x1[0])):
                self.x1[i][j] /= self.x1_cnt[i]

    # обновление разбиения
    def upd_cl(self, N_obj, data):
        l = []
        l1 = False
        for i in range(N_obj):
            for j in range(self.ncl):
                l.append([self.dist(data[i], self.x1[j]), j])
            lmin = min(l, key=lambda a: a[0])
            if self.Y_new[i] != lmin[1]:
                l1 = True
                self.Y_new[i] = lmin[1]
            l.clear()
        return l1

    # подсчет qual
    def cl_qual(self, N_obj, data):
        self.q.fill(0.0)
        for i in range(N_obj):
            self.q[self.Y_new[i]] += self.sqr_dist(data[i], self.x1[self.Y_new[i]])
        self.qual = 0.0
        for i in self.q:
            self.qual += i

    # фиксация оптимального
    def selfcopy(self, copy2):
        copy2.qual = copy.deepcopy(self.qual)
        copy2.Y_new = copy.deepcopy(self.Y_new)
        copy2.x1 = copy.deepcopy(self.x1)
        copy2.x1_cnt = copy.deepcopy(self.x1_cnt)
        copy2.q = copy.deepcopy(self.q)

    # 1 итерация
    def test(self, N_obj, data):
        self.gen_sp(N_obj)
        self.st_cl(N_obj, data)

        while True:
            self.upd_c(N_obj, data)
            if self.upd_cl(N_obj, data) == False:
                break
            self.x1_cnt.fill(0)
            self.x1.fill(0.0)

        self.cl_qual(N_obj, data)

    # график
    def vim(self, N_obj, data):
        gr = plt.subplot()
        rand.seed()
        colors = ["red", "green", "blue", "yellow"]
        # for i in range(self.ncl):
        #     colors.append('#06x' % rand.randint(0, 0xFFFFFF))
        c = []
        for j in range(self.ncl):
            c.append([data[i] for i in range(N_obj) if self.Y_new[i] == j])

        for j in range(self.ncl):
            for i in range(len(c[j])):
                gr.scatter(c[j][i][2], c[j][i][3], c=colors[j])

        plt.show()

    # main
    def run():
        ds = DsStorage()
        ncl, ntests = [int(a) for a in input().split()]
        iris_ws = MyClustering(ds, ncl)
        iris_opt_cl = MyClustering(ds, ncl)

        for i in range(ntests):
            iris_ws.test(ds.N_obj, ds.X)
            if i == 0 or iris_ws.qual < iris_opt_cl.qual:
                iris_ws.selfcopy(iris_opt_cl)

        print(iris_opt_cl.x0)
        print(iris_opt_cl.Y_new)
        iris_opt_cl.vim(ds.N_obj, ds.X)


# -----
MyClustering.run()
