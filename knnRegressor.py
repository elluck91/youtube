import pickle
from sklearn.model_selection import cross_val_predict
from sklearn.neighbors import KNeighborsRegressor
import matplotlib.pyplot as plt

def knnRegressorTrain(test, target, save=True, cv=True):
    print "Beginning to train the KNN Model."
    if save == False:
        with open('knnModel.pickle', 'rb') as handle:
            model = pickle.load(handle)
        
        predicted = cross_val_predict(model, test, target, cv=10)
        print model.score(test, target)
    else:
        model = KNeighborsRegressor()
        knn = model.fit(test, target)
        print "Saving the model."
        with open('naiveModel.pickle', 'wb') as handle:
            pickle.dump(knn, handle, protocol=pickle.HIGHEST_PROTOCOL) 
    if cv == True:
        print "Cross-validating."
        predicted = cross_val_predict(knn, test, target, cv=10)
        print knn.score(test, target)

        print "Plotting."
        fig, ax = plt.subplots()
        ax.scatter(y, predicted, edgecolors=(0, 0, 0))
        ax.plot([min(target), max(target)], [min(target), max(target)], 'k--', lw=4)
        ax.set_xlabel('Measured')
        ax.set_ylabel('Predicted')
        plt.show()

def knn_predict(X, plot=True):
    print "Loading Linear Regression Model."
    regr = loadModel()

    predicted = []

    print "Running prediction."
    for i in range(X.shape[0]):
        predicted.append(regr.predict(X.getrow(i)[0]))

    if plot==True:
        print "Plotting."
        fig, ax = plt.subplots()
        ax.scatter(range(X.shape[0]), predicted, edgecolors=(0, 0, 0))
        ax.plot([min(predicted), max(predicted)], [min(predicted), max(predicted)], 'k--', lw=4)
        ax.set_xlabel('Object id')
        ax.set_ylabel('Predicted')
        plt.show()

    return predicted


def cross_val(X, y, plot=True):
    regr = loadModel()
    predicted = cross_val_predict(regr, X, y, cv=10)
    print "R^2 on the training set: ", model.score(test, target)

    if plot == True:
        print "Plotting:"
        fig, ax = plt.subplots()
        ax.scatter(y, predicted, edgecolors=(0, 0, 0))
        ax.plot([min(y), max(y)], [min(y), max(y)], 'k--', lw=4)
        ax.set_xlabel('Measured')
        ax.set_ylabel('Predicted')
        plt.show()

def loadModel():
    with open('naiveModel.pickle', 'rb') as handle:
        regr = pickle.load(handle)
    return regr


