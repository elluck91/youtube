# youtube analytics

run: $ python model.py main_data.npz

Instruction:
Select Model:
1. Linear Regression
2. Random Forest
3. Naive Bayes
4. KNN

Select operation:
1. Train model
2. Predict

For the purpose of demonstration, selecting 2. Predict will do the following:
1. Randomly select 100 samples from the dataset
2. Predict their viewCount based on the selected algorithm
3. Report R^2
4. Show plot
