import numpy as np
import pandas as pd
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.model_selection import train_test_split

# NOTE: Make sure that the outcome column is labeled 'target' in the data file
tpot_data = pd.read_csv('PATH/TO/DATA/FILE', sep='COLUMN_SEPARATOR', dtype=np.float64)
features = tpot_data.drop('target', axis=1)
training_features, testing_features, training_target, testing_target = \
            train_test_split(features, tpot_data['target'], random_state=23)

# Average CV score on the training set was: 0.9974908845827983
exported_pipeline = ExtraTreesClassifier(bootstrap=True, criterion="entropy", max_features=0.9, min_samples_leaf=1, min_samples_split=19, n_estimators=100)
# Fix random state in exported estimator
if hasattr(exported_pipeline, 'random_state'):
    setattr(exported_pipeline, 'random_state', 23)

exported_pipeline.fit(training_features, training_target)
results = exported_pipeline.predict(testing_features)
