import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures, OneHotEncoder 

def A2_A0273348X(N):

    iris = load_iris() #150 samples
    X = iris.data #2D matrix (150,4), features => (sepal length, sepal width, petal length, petal width)
    y = iris.target #1D array (150,), targets => (0, 1, or 2)

    #split dataset into 20% training and 80% testing, N is the function parameter (for reproducibility)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.8, random_state=N)

    #Generate the target output using one-hot encoding for both the training set and the test set
    encoder = OneHotEncoder(sparse=False, sparse_output=False)

    #(number_of_training_samples,3)
    #identify and learn unique categories in y_train
    Ytr = encoder.fit_transform(y_train.reshape(-1, 1)) #reshape from 1D array to 2D column vector

    #(number_of_test_samples, 3)
    #only transform y_test using categories from y_train
    Yts = encoder.transform(y_test.reshape(-1, 1))

    #Polynomial features 
    Ptrain_list = [] #List of training polynomial matrices for orders 1 to 10
    Ptest_list = [] #List of test polynomial matrices for orders 1 to 10

    for degree in range(1, 11):
        polynomial = PolynomialFeatures(degree=degree)
        Ptrain_list.append(polynomial.fit_transform(X_train))
        Ptest_list.append(polynomial.transform(X_test))

    #Ridge Regression (L2 Regularisation) to prevent overfitting by shrinking the magnitude of coefficients
    regularisation_rate = 0.0001 #lambda 

    w_list = [] #List of estimated regression coefficients for orders 1 to 10
    error_train_array = [] #Training error counts for orders 1 to 10
    error_test_array = [] #Test error counts for orders 1 to 10

    for index in range(10):
        model = Ridge(alpha=regularisation_rate)
        model.fit(Ptrain_list[index], Ytr)

        #Regression coefficients(weights)
        w_list.append(model.coef_)

        #Uses respective polynomials created to predict outputs
        y_train_onehot = model.predict(Ptrain_list[index])
        y_test_onehot = model.predict(Ptest_list[index])

        #Converting one-hot encoded outputs to class labels (0, 1, and 2)
        y_train_classlabel = np.argmax(y_train_onehot, axis=1)
        y_test_classlabel = np.argmax(y_test_onehot, axis=1)

        #Find training and testing errors
        #Comparing predicted outputs with ground truths (Ytr and Yts)
        training_error = np.sum(y_train_classlabel != y_train)
        testing_error = np.sum(y_test_classlabel != y_test)

        #Append each error to their respective lists
        error_train_array.append(training_error)
        error_test_array.append(testing_error)

    #converting lists to numpy array of training error counts
    error_train_array = np.array(error_train_array)
    error_test_array = np.array(error_test_array)

    return X_train, y_train, X_test, y_test, Ytr, Yts, Ptrain_list, Ptest_list, w_list, error_train_array, error_test_array

