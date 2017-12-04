from sklearn.metrics import r2_score
from RandomForest import randForestTrain, forest_predict
from linRegressor import linRegressorTrain, linear_predict
from bayesRegressor import naiveRegressorTrain, naive_predict
from knnRegressor import knnRegressorTrain, knn_predict
import sys
from sklearn.feature_selection import SelectPercentile, f_regression
from sklearn.model_selection import cross_val_predict
from sklearn import linear_model
import matplotlib.pyplot as plt
from scipy.sparse import csr_matrix, load_npz, vstack
import pickle
import numpy as np
import random

def selectFeatures(test, target, percent):
    selector = SelectPercentile(f_regression, percentile=percent)
    data = selector.fit_transform(test, target)
    selected_features = selector.get_support(indices=True)
    return data, selected_features

# cross-validate
def csr_l2normalize(mat, copy=False, **kargs):
    r""" Normalize the rows of a CSR matrix by their L-2 norm. 
    If copy is True, returns a copy of the normalized matrix.
    """
    if copy is True:
        mat = mat.copy()
    nrows = mat.shape[0]
    nnz = mat.nnz
    ind, val, ptr = mat.indices, mat.data, mat.indptr
    # normalize
    for i in range(nrows):
        rsum = 0.0    
        for j in range(ptr[i], ptr[i+1]):
            rsum += val[j]**2
        if rsum == 0.0:
            continue  # do not normalize empty rows
        rsum = 1.0/np.sqrt(rsum)
        for j in range(ptr[i], ptr[i+1]):
            val[j] *= rsum
            
    if copy is True:
        return mat

def plotResults(predicted, measured):
    fig, ax = plt.subplots()
    ax.scatter(measured, predicted, edgecolors=(0, 0, 0))
    ax.plot([min(measured), max(measured)], [min(predicted), max(predicted)], 'k--', lw=4)
    ax.set_xlabel('Measured')
    ax.set_ylabel('Predicted')
    plt.show()

# main
input_path = sys.argv[1]
print "Hi there!\nWe will process the following file:"
print input_path

options = ("\nPlease select model to use:\n" 
        + "1. Linear Regression\n"
        + "2. Random Forest\n"
        + "3. Naive Bayes - very time inefficient\n"
        + "4. K Nearest Neighbors\n"
        + "\nEnter number: ")
chosen_model  = input(options)
is_training = input("Are you training models or predicting?\n"
        + "1 for training\n2 for predicting\n")
X = load_npz(input_path).tocsr()
print "Extracting features and normalizing data."
csr_l2normalize(X)


file = open('classes.txt', 'r')
y = []
for line in file:
    y.append(int(line.replace("\n", '')))
file.close()

if chosen_model == 1:
    train, selected_features  = selectFeatures(X, y, 20)
elif chosen_model == 2:
    train, selected_features  = selectFeatures(X, y, 15)
elif chosen_model == 3:
    train, selected_features  = selectFeatures(X, y, 1)
elif chosen_model == 4:
    train, selected_features  = selectFeatures(X, y, 30)

if is_training == 1:
    if chosen_model == 1:
        linRegressorTrain(train, y, save=True, cv=False)
    elif chosen_model == 2:
        randForestTrain(train, y, save=True, cv=True)
    elif chosen_model == 3:
        naiveRegressorTrain(train, y, save=True, cv=False)
    elif chosen_model == 4:
        knnRegressorTrain(train, y, save=True, cv=False)
    print "Done."
else:
    random_test = csr_matrix((0, train.shape[1]))
    random_clas = []


    while len(random_clas) < 100:
        test = random.randint(0, train.shape[0])
        if y[test] < 20000:
            random_test = vstack(([random_test, train.getrow(test)[0]]))
            random_clas.append(y[test])

    if chosen_model == 1:
        predicted =  linear_predict(random_test, plot=False)
        plotResults(predicted, random_clas)
    elif chosen_model == 2:
        predicted = forest_predict(random_test, plot=False)
        plotResults(predicted, random_clas)
    elif chosen_model == 3:
        predicted = naive_predict(random_test, plot=False)
        plotResults(predicted, random_clas)
    elif chosen_model == 4:
        predicted = knn_predict(random_test, plot=False)
        plotResults(predicted, random_clas)

    r2 = r2_score(random_clas, predicted)
    print "R^2 of the sample: ", r2

