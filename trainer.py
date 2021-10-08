from flaml import AutoML
import numpy as np
import os
import pandas as pd
import glob
import pickle
from sklearn import svm

# Initialize an AutoML instance
automl = AutoML()

# Specify automl goal and constraint
automl_settings = {
    "time_budget": 3600*1,  # in seconds
    "metric": 'auto',
    "task": 'classification',
    "log_file_name": "log.log",
}

all_files = glob.glob(os.path.join('recordings/*.csv'))
df_from_each_file = (pd.read_csv(f, header=None) for f in all_files)
data = pd.concat(df_from_each_file, ignore_index=True)

labels = []
for entry in os.scandir('recordings/'):
    if entry.is_file():
        labels.append(entry.name.partition('-')[0])
labels = np.array(labels)

"""clf = svm.SVC()
clf.fit(data, labels)

with open('model2.pkl', 'wb') as model:
    pickle.dump(clf, model, pickle.HIGHEST_PROTOCOL)"""

# Train with labeled input data
automl.fit(X_train=data, y_train=labels, **automl_settings)

# Predict
print("\nPrediction:")
print(automl.predict(data))

# Export the best model
print("\nBest model:")
print(automl.model)

with open('model.pkl', 'wb') as model:
    pickle.dump(automl, model, pickle.HIGHEST_PROTOCOL)