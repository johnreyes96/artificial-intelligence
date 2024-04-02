# -*- coding: utf-8 -*-
"""SupportVectorMachines.ipynb

Automatically generated by Colaboratory.
"""

# Support vector machines (SVMs)
from sklearn import svm

X = [[0, 0], [1, 1]]
y = [0, 1]
clf = svm.SVC()
clf.fit(X, y)

print(clf.support_vectors_)
