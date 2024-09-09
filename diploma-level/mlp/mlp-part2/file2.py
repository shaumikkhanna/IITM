from sklearn.datasets import fetch_openml
import numpy as np

data, labels = fetch_openml('mnist_784', return_X_y=True)

x_train, x_test = data[:10000], data[10000:12000]
y_train, y_test = labels[:10000], labels[10000:12000]

positive_class = np.array(x_train[y_train == '5'])
negative_class = np.array(x_train[y_train == '3'])
labels = np.array([1] * len(positive_class) + [-1] * len(negative_class)).reshape(-1, 1)

matrix = np.concatenate([positive_class, negative_class])
matrix = np.concatenate([matrix, labels], axis=1)


test_positive_class = np.array(x_test[y_test == '5'])
test_negative_class = np.array(x_test[y_test == '3'])
test_labels = np.array([1] * len(test_positive_class) + [-1] * len(test_negative_class)).reshape(-1, 1)

test_matrix = np.concatenate([test_positive_class, test_negative_class])
test_matrix = np.concatenate([test_matrix, test_labels], axis=1)


import pickle

with open('matrix.pkl', 'wb') as f:
    pickle.dump(matrix, f)

with open('test_matrix.pkl', 'wb') as f:
    pickle.dump(test_matrix, f)

