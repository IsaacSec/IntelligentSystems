from matplotlib import cm
from sklearn import datasets, linear_model
import warnings
import pandas
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np

warnings.filterwarnings(action="ignore", module="scipy", message="^internal gelsd")

wine = datasets.load_wine()
X = wine.data
y = wine.target
print("Name of the classes ", wine.target_names)
print("Features: ", wine.feature_names)
print("Dataset length: ", len(X))


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2, random_state=42)

print("Train length: ", len(X_train))
print("Test length: ", len(X_test))

wine_dataframe = pandas.DataFrame(X_train, columns=wine.feature_names)
cmap = cm.get_cmap('Accent')
pandas.plotting.scatter_matrix(wine_dataframe, c=y_train, figsize=(15, 15), marker='o', hist_kwds={'bins': 20}, s=60,
                               alpha=.8, cmap=cmap)
plt.show()

logistic = linear_model.LogisticRegression(C=1)
logistic.fit(X_train, y_train)
print("Training set score 1: {:.3f}".format(logistic.score(X_train, y_train)))

print("Test set score 1 : {:.3f}".format(logistic.score(X_test, y_test)))

logistic = linear_model.LogisticRegression(C=10)
logistic.fit(X_train, y_train)
print("Training set score 2: {:.3f}".format(logistic.score(X_train, y_train)))

print("Test set score 2: {:.3f}".format(logistic.score(X_test, y_test)))

logistic = linear_model.LogisticRegression(C=.001)
logistic.fit(X_train, y_train)
print("Training set score 3: {:.3f}".format(logistic.score(X_train, y_train)))

print("Test set score 3: {:.3f}".format(logistic.score(X_test, y_test)))


prediction = logistic.predict(X_test)
print("Prediction - test: ", abs(y_test - prediction))
print("Test: ", y_test)
print("Prediction: ", prediction)




