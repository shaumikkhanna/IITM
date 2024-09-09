import numpy as np


def sigmoid(x, w, b):
	return 1/(1+np.exp(-(w*x+b)))


def derivative(xs, ys, w, b):
	total_w = 0
	total_b = 0

	for x, y in zip(xs, ys):
		y_hat = sigmoid(x, w, b)
		total_w += (y_hat-y)*y_hat*(1-y_hat)*x
		total_b += (y_hat-y)*y_hat*(1-y_hat)

	return total_w, total_b


def loss(xs, ys, w, b):
	total = 0
	for x, y in zip(xs, ys):
		total += (sigmoid(x, w, b)-y)**2

	return 0.5*total



xs = [-2,2]
ys = [0.18,0.81]
# xs = [-6,-4,-2,0,2,4,6]
# ys = [0.01,0.04,0.18,0.5,0.81,0.95,0.98]


w = 0
b = 0
prev_loss = loss(xs, ys, w, b)
for _ in range(70):
	del_w, del_b = derivative(xs, ys, w, b)

	new_loss = loss(xs, ys, w, b)
	print(new_loss-prev_loss)
	prev_loss = new_loss

	w = w - 0.1*del_w
	b = b - 0.1*del_b



print(w, b)


