from flaml import AutoML
import pandas
import pickle

dataset = pandas.read_csv('ML/data.csv')

automl = AutoML()
automl.fit(dataframe=dataset, label='label', task='classification', time_budget=3600, early_stop=True)

print('\nPrediction:\n' + automl.predict(dataset) )
print('\nBest model:\n' + automl.model)

with open('ML/model.pkl', 'wb') as model:
    pickle.dump(automl, model, pickle.HIGHEST_PROTOCOL)
    print('\nModel exported')