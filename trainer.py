from flaml import AutoML
import pandas as pd
import pickle

dataset = pd.read_csv('ML/data.csv')

# Initialize an AutoML instance
automl = AutoML()

# Specify automl goal and constraint
automl_settings = {
    "time_budget": 3600,  # in seconds
    "task": 'classification',
    "log_file_name": "ML/log.log",
}

# Train with labeled input data
automl.fit(dataframe=dataset, label='label', early_stop=True, **automl_settings)

# Predict
print('\nPrediction:' )
print(automl.predict(dataset))

# Export the best model
print('\nBest model:')
print(automl.model)

with open('ML/model.pkl', 'wb') as model:
    pickle.dump(automl, model, pickle.HIGHEST_PROTOCOL)
    print('\nModel exported')