%matplotlib inline
import math as m
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as clrs
import random as rand
import copy

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from collections import Counter

X = load_iris().data
Y = load_iris().target

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2)

# classifier decision
predicts = np.zeros(shape = len(X_test), dtype = int)

class MykNN:
    
    k = 1
    
    def __init__(self):
        pass
    
    def kern_ep(self, r):
        return 0.75*(1-r**2)*(m.fabs(r)<=1)
    
    # main algo
    def predict(self, k):
        for i in range(len(X_test)):
            # собирает веса соседей по классам
            votes = [0.0 for i in range(3)]
            # расстояния от текущего объекта из X_test до объектов из X_train
            dists = np.zeros(shape = len(X_train), dtype = [('dist', float), ('nobj', int)])
            
            for j in range(len(X_train)):
                dists[j][0] = np.linalg.norm(np.array(X_test[i]) - np.array(X_train[j]))
                dists[j][1] = j # номер обьекта из X_train 
            dists.sort(order = 'dist')
            
            for j in range(k):
                # подъядерная функция
                eq = (dists[j][0])/(dists[k][0])
                
                votes[Y_train[dists[j][1]]] += self.kern_ep(eq)
            
            predicts[i] = votes.index(max(votes))
    
    # cross_validation
    def crv_predict(self, k):
        errors = 0
        crv_predicts = np.zeros(shape = len(X_train), dtype = int)
        for i in range(len(X_train)):
            votes = [0.0 for i in range(3)]
            dists = np.zeros(shape = len(X_train), dtype = [('dist', float), ('nobj', int)])
            
            for j in range(len(X_train)):
                dists[j][0] = np.linalg.norm(np.array(X_train[i]) - np.array(X_train[j]))
                dists[j][1] = j # номер обьекта из X_train 
            dists.sort(order = 'dist')
            
            # рассматриваем всех соседей объекта, кроме самого себя
            for j in range(1, k):
                eq = (dists[j][0])/(dists[k][0])
                votes[Y_train[dists[j][1]]] += self.kern_ep(eq)
            crv_predicts[i] = votes.index(max(votes))
        
        for i in range(len(X_train)):
            errors += (Y_train[i]!=crv_predicts[i])
        return errors
    
    # определение оптимального k
    # построение графика LOO(k)    
    def crv(self):
        k_opt = 1
        errors = 0
        rm = np.zeros(shape = 100)
        for i in range(1, 101):
            cur_err = self.crv_predict(i)
            rm[i-1] = cur_err 
            if ((i == 1) or (cur_err < errors)):
                k_opt = i
                errors = cur_err
        print('k = ', k_opt)
        print('LOO = ', errors)
        pl = plt.plot([i for i in range(1, 101)], rm)
        plt.show()
        return k_opt
    
    def acc(self):
        errors = 0
        for i in range(len(X_test)):
            errors += (Y_test[i]!=predicts[i])
        return errors        
     
a = MykNN()            
MykNN.predict(a, a.crv())
print(((len(Y_test)) - MykNN.acc(a))/(len(Y_test)))