import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import OneHotEncoder, PolynomialFeatures
from sklearn.linear_model import Ridge

def A2_A0273348X(N):
    #Load the Iris dataset
    iris = load_iris()
    X = iris.data  # Features
    y = iris.target  # Labels

    # Split the dataset into training (20%) and testing (80%) sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.8, random_state=42)

    # One-hot encode the target output for both training and testing sets
    encoder = OneHotEncoder(sparse=False)
    y_train_encoded = encoder.fit_transform(y_train.reshape(-1, 1))
    y_test_encoded = encoder.transform(y_test.reshape(-1, 1))

    # Initialize variables for storing results
    train_correct_counts = []
    test_correct_counts = []

    # Loop over polynomial orders from 1 to 10
    for order in range(1, 11):
        # Generate polynomial features
        poly = PolynomialFeatures(degree=order)
        X_train_poly = poly.fit_transform(X_train)
        X_test_poly = poly.transform(X_test)
        
        # Determine which form of ridge regression to use
        if X_train_poly.shape[0] <= X_train_poly.shape[1]:
            # Use dual form of ridge regression
            ridge = Ridge(alpha=0.0001, solver='sag')  # Adjust solver if needed
        else:
            # Use normal ridge regression
            ridge = Ridge(alpha=0.0001)

        # Fit the model to the training data
        ridge.fit(X_train_poly, y_train_encoded)

        # Predict and calculate the number of correct classifications for the training set
        y_train_pred = ridge.predict(X_train_poly)
        y_train_pred_class = np.argmax(y_train_pred, axis=1)
        train_correct = np.sum(y_train_pred_class == y_train)
        train_correct_counts.append(train_correct)

        # Predict and calculate the number of correct classifications for the testing set
        y_test_pred = ridge.predict(X_test_poly)
        y_test_pred_class = np.argmax(y_test_pred, axis=1)
        test_correct = np.sum(y_test_pred_class == y_test)
        test_correct_counts.append(test_correct)

        # Print results for this polynomial order
        print(f"Order {order}:")
        print(f"  Training set correct classifications: {train_correct} / {len(y_train)}")
        print(f"  Testing set correct classifications: {test_correct} / {len(y_test)}")


    # your code goes here
    pass
    # return in this order
    return X_train, y_train, X_test, y_test, Ytr, Yts, Ptrain_list, Ptest_list, w_list, error_train_array, error_test_array
