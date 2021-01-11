import numpy as np
from sklearn import neighbors
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

X = load_iris().data
Y = load_iris().target

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2)

clf = neighbors.KNeighborsClassifier()
clf.fit(X_train, Y_train)

accuracy = clf.score(X_test, Y_test)
print(accuracy)

ex = [[6.5, 3.1, 4.1, 1.5], [6.5, 3.1, 6.1, 3.5]]
pred = clf.predict(ex)
print(pred)