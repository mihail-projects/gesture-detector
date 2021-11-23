from flaml import AutoML
import pandas as pd
import pickle
from pycaret.classification import *


dataset = pd.read_csv('recordings/data.csv')


"""data = dataset.sample(frac=0.9, random_state=786)
data_unseen = dataset.drop(data.index)

data.reset_index(drop=True, inplace=True)
data_unseen.reset_index(drop=True, inplace=True)

print('Data for Modeling: ' + str(data.shape))
print('Unseen Data For Predictions: ' + str(data_unseen.shape))

exp_mclf101 = setup(data = data, target = 'label', session_id=123) 

best = compare_models()"""


# Initialize an AutoML instance
automl = AutoML()

# Specify automl goal and constraint
automl_settings = {
    "time_budget": 3600,  # in seconds
    "task": 'classification',
    "log_file_name": "log.log",
}

# Train with labeled input data
automl.fit(dataframe=dataset, label='label', **automl_settings)

# Predict
print('\nPrediction:' )
print(automl.predict(dataset))

# Export the best model
print('\nBest model:')
print(automl.model)

with open('model.pkl', 'wb') as model:
    pickle.dump(automl, model, pickle.HIGHEST_PROTOCOL)
    print('\nModel exported')