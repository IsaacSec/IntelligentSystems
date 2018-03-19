from matplotlib import cm
from sklearn import datasets, linear_model
import warnings
import pandas
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np

warnings.filterwarnings(action="ignore", module="scipy", message="^internal gelsd")

iris = datasets.load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.02, random_state=42)

iris_dataframe = pandas.DataFrame(X_train, columns=iris.feature_names)
cmap = cm.get_cmap('Accent')
pandas.scatter_matrix(iris_dataframe, c=y_train, figsize=(15, 15), marker='o', hist_kwds={'bins': 20}, s=60, alpha=.8,
                      cmap=cmap)
plt.show()

logistic = linear_model.LogisticRegression(C=1e5)
logistic.fit(X_train, y_train)
print("Training set score: {:.3f}".format(logistic.score(X_train, y_train)))

print("Test set score: {:.3f}".format(logistic.score(X_test, y_test)))


prediction = logistic.predict(X_test)
print(abs(y_test - prediction))

