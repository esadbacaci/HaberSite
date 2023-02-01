# -*- coding: utf-8 -*-
"""
Created on Mon May 17 01:14:53 2021

@author: SerdarKR
"""


import pandas
from sklearn import tree
import pydotplus 
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg
from sklearn.model_selection import train_test_split

df = pandas.read_csv("SosyalMedyaReklamKampanyasi.csv")

x = df.iloc[:, [2,3]].values
y = df.iloc[:, 4].values
import time
start_time = time.time()#baslangic zamanını belirliyoruz.

d = {'Erkek': 0, 'Kadin':1}
df['Cinsiyet'] = df['Cinsiyet'].map(d)

features = ["Yas","TahminiMaas"]

X = df[features]
y = df['SatinAldiMi']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

dtree = DecisionTreeClassifier(criterion = 'entropy', random_state=2,max_depth=5)
dtree = dtree.fit(X_train, y_train)
from sklearn.tree import DecisionTreeClassifier 
classifier = DecisionTreeClassifier(criterion = 'entropy', random_state=0)
classifier.fit(X_train, y_train)
y_pred = dtree.predict(X_test)

y_pred = classifier.predict(X_test)
from sklearn.metrics import confusion_matrix
cm1 = confusion_matrix(y_test, y_pred)
print(cm1)


print(dtree.predict([[30,87000]]))



fig = plt.figure(1,figsize=(15,10))
tree.plot_tree(dtree,filled=True)
plt.title("Entropy")
plt.show()


data = tree.export_graphviz(dtree, out_file=None, feature_names=features)
graph = pydotplus.graph_from_dot_data(data)
graph.write_png('mydecisiontree.png')


plt.figure(2,figsize=(15,10))
plt.title("Entropy")
img=pltimg.imread('mydecisiontree.png')
imgplot = plt.imshow(img)
plt.show()

#%%

dtree1 = DecisionTreeClassifier(criterion = 'gini', random_state=2,max_depth=6)
dtree1 = dtree1.fit(X_train, y_train)

y_pred1 = dtree1.predict(X_test)


from sklearn.metrics import confusion_matrix
cm2 = confusion_matrix(y_test, y_pred1)
print(cm2)


print(dtree1.predict([[30,87000]]))



fig = plt.figure(3,figsize=(15,10))
tree.plot_tree(dtree1,filled=True)
plt.title("Gini")
plt.show()


data1 = tree.export_graphviz(dtree1, out_file=None, feature_names=features)
graph1 = pydotplus.graph_from_dot_data(data1)
graph1.write_png('mydecisiontree1.png')


plt.figure(4,figsize=(15,10))
plt.title("Gini")
img1=pltimg.imread('mydecisiontree1.png')
imgplot = plt.imshow(img1)
plt.show()

import time
sure=time.time()-start_time#bitiş zamanında çıkartıyoruz.
print(sure)
