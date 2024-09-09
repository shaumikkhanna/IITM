import numpy as np
import pickle


with open('matrix.pkl', 'rb') as file:
    matrix = pickle.load(file)

with open('test_matrix.pkl', 'rb') as file:
    test_matrix = pickle.load(file)


x_train, y_train = matrix[:, :-1], matrix[:, -1]
x_test, y_test = test_matrix[:, :-1], test_matrix[:, -1]
# print(x_train.shape, y_train.shape, x_test.shape, y_test.shape)

# print(sum(y_train == 1))
# print(sum(y_train == -1))


from sklearn.linear_model import Perceptron

perceptron1 = Perceptron(random_state=42, eta0=1, max_iter=100, shuffle=True, fit_intercept=True, penalty=None)
perceptron2 = Perceptron(random_state=42, eta0=1, max_iter=100, shuffle=False, fit_intercept=True, penalty=None)

perceptron1.fit(x_train, y_train)
perceptron2.fit(x_train, y_train)


# from sklearn.metrics import confusion_matrix

# y_pred = perceptron1.predict(x_test)
# print(confusion_matrix(y_test, y_pred))


from sklearn.metrics import accuracy_score, precision_score, recall_score

y_pred_1 = perceptron1.predict(x_test)
old_accuracy = accuracy_score(y_test, y_pred_1)
old_precision = precision_score(y_test, y_pred_1)
old_recall = recall_score(y_test, y_pred_1)

print('With shuffling')
print("Accuracy:", old_accuracy)
print("Precision:", old_precision)
print("Recall:", old_recall)

print()

y_pred_2 = perceptron2.predict(x_test)
new_accuracy = accuracy_score(y_test, y_pred_2)
new_precision = precision_score(y_test, y_pred_2)
new_recall = recall_score(y_test, y_pred_2)

print('Without shuffling')
print("Accuracy:", new_accuracy)
print("Precision:", new_precision)
print("Recall:", new_recall)
