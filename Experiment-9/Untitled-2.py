from sklearn import datasets, model_selection, naive_bayes, neighbors, svm

breast_cancer_wisconsin = datasets.load_breast_cancer()
x_train, x_test, y_train, y_test = model_selection.train_test_split(
    breast_cancer_wisconsin.data, breast_cancer_wisconsin.target, test_size=0.25)
gaussian = naive_bayes.GaussianNB()
bernoulli = naive_bayes.BernoulliNB()
complement = naive_bayes.ComplementNB()
# categorical = naive_bayes.CategoricalNB()
multinomial = naive_bayes.MultinomialNB()
linear = svm.LinearSVC()
k = neighbors.KNeighborsClassifier()
gaussian.fit(x_train, y_train)
bernoulli.fit(x_train, y_train)
complement.fit(x_train, y_train)
# categorical.fit(x_train, y_train)
multinomial.fit(x_train, y_train)
linear.fit(x_train, y_train)
k.fit(x_train, y_train)
print('The accuracy of GaussianNB is:', gaussian.score(x_test, y_test))
print('The accuracy of BernoulliNB is:', bernoulli.score(x_test, y_test))
print('The accuracy of ComplementNB is:', complement.score(x_test, y_test))
# print('The accuracy of CategoricalNB is:', categorical.score(x_test,y_test))
print('The accuracy of MultinomialNB is:', multinomial.score(x_test, y_test))
print('The accuracy of LinearSVC is:', linear.score(x_test, y_test))
print('The accuracy of KNeighborsClassifier is:', k.score(x_test, y_test))
