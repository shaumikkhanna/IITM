def ConfusionMatrix(y_hat,y):
	TN = 0
	FP = 0
	FN = 0
	TP = 0
	for actual, predicted in zip(y, y_hat):
		if actual == 1:
			if predicted == 1:
				TP += 1
			else:
				FN += 1
		else:
			if predicted == 1:
				FP += 1
			else:
				TN += 1

	return np.array([
			[TN, FP],
			[FN, TP]
		])