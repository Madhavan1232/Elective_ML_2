import pandas as pd
import numpy as np
import os , sys
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

df = pd.read_csv(os.path.join(sys.path[0] , input()))
print(f"Shape of dataset: {df.shape}")

train_data , test_data = train_test_split(df , test_size = 0.2 , random_state = 42)

print(f"Size of training dataset:  {train_data.shape}")
print(f"Size of test dataset:  {test_data.shape}")

xtrain , xtest , ytrain , ytest = train_test_split(
    df.drop(columns = 'not.fully.paid') , df['not.fully.paid'] , test_size = 0.2 , random_state = 42) 

print(f"\nShapes:")
print(f"X_train: {xtrain.shape} Y_train: {ytrain.shape}")
print(f"X_test: {xtest.shape} Y_test: {ytest.shape}")