from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_predict
import matplotlib.pyplot as plt
import pickle

def randForestTrain(X, y, save=True, cv=True):
    print "Beginning to train the Random Forest Model."
    if save == True:
        regr = RandomForestRegressor(random_state=0)
        regr.fit(X, y)
        print "Saving the model."
        with open('randomForest.pickle', 'wb') as handle:
            pickle.dump(regr, handle, protocol=pickle.HIGHEST_PROTOCOL) 
    else:
        regr = RandomForestRegressor(random_state=0)
        regr.fit(X, y)

    if cv == True:
        print "Cross-validating..."
        cross_val(X, y, plot=True)
    return regr

def forest_predict(X, plot=True):
    regr = loadModel()

    predicted = []

    for i in range(X.shape[0]):
            predicted.append(regr.predict(X.getrow(i)[0]))

    if plot==True:
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
    print "R^2 on the training set: ", regr.score(X, y)

    if plot == True:
        print "Plotting:"
        fig, ax = plt.subplots()
        ax.scatter(y, predicted, edgecolors=(0, 0, 0))
        ax.plot([min(y), max(y)], [min(y), max(y)], 'k--', lw=4)
        ax.set_xlabel('Measured')
        ax.set_ylabel('Predicted')
        plt.show()

def loadModel():
    with open('randomForest.pickle', 'rb') as handle:
        regr = pickle.load(handle)
    return regr
