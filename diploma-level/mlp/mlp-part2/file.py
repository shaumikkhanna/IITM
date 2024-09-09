from sklearn.datasets import fetch_california_housing

california = fetch_california_housing()
data = california.data
target = california.target


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(data, target, test_size=0.4, random_state=1)


from sklearn.preprocessing import StandardScaler
std_scalar = StandardScaler(with_mean=True, with_std=True)


x_train = std_scalar.fit_transform(x_train)
x_test = std_scalar.transform(x_test)


from sklearn.linear_model import Lasso
lasso_regressor = Lasso()


from sklearn.model_selection import GridSearchCV

param_grid = {
    'alpha': [0.5, 0.1, 0.05, 0.01, 0.005, 0.001],
    'fit_intercept': [True, False],
}

grid_search = GridSearchCV(estimator=lasso_regressor, param_grid=param_grid, cv=6)
grid_search.fit(x_train, y_train)

best_params = grid_search.best_params_
best_score = grid_search.best_score_

print("Best parameters:", best_params)
print("Best score:", best_score)


print(grid_search.score(x_test, y_test))