from sklearn.datasets import load_breast_cancer, fetch_california_housing
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import FunctionTransformer, PolynomialFeatures
from sklearn.feature_selection import SelectPercentile, mutual_info_regression
from sklearn.model_selection import train_test_split
from sklearn.dummy import dummy_classifier
import numpy as np
import pandas as pd


# data = load_breast_cancer()

# print(data.keys())
# print(data['DESCR'])

# d = data['data']
# print(np.corrcoef(d[:, 0], d[:, 2]))

# s = SimpleImputer()
# a = [[7, 16, 31], [np.nan, np.nan, 66], [12, 5, np.nan],[98, np.nan, 92]]
# print(s.fit_transform(a))

# f = FunctionTransformer(np.log10)
# a = [[1, 1], [2, 3],[10,100]]
# print(f.fit_transform(a))


# data = pd.read_csv(
# 	'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', 
# 	names=['sepal length', 'sepal width', 'petal length', 'petal width', 'label']
# 	)

# print(data)


data = fetch_california_housing()
data, labels = data['data'], data['target']

# new_data = SelectPercentile(mutual_info_regression, percentile=10).fit_transform(data, labels)
# print(new_data)

train_data, train_labels, test_data, test_labels = train_test_split(data, labels, test_size=0.2)
print(train_data.shape)
print(test_data.shape)
print(train_labels.shape)
print(test_labels.shape)








