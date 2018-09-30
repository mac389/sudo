import json, os

import pandas as pd 

from pprint import pprint 

actual_test_labels = json.load(open('./test_labels.json','r'))
predicted_test_labels = json.load(open('./predicted_labels.json','r'))

df_actual_test_labels = pd.DataFrame.from_dict(actual_test_labels, orient='index')
df_actual_test_labels.columns=['Actual']

formatted_predicted_test_labels = {}

for patient in predicted_test_labels:
	predicate,probability = predicted_test_labels[patient].items()[0]
	if probability > 0.8:
		formatted_predicted_test_labels[patient] = predicate

df_formatted_predicted_test_labels = pd.DataFrame.from_dict(formatted_predicted_test_labels, orient='index')
df_formatted_predicted_test_labels.columns=['Predicted']

df = pd.concat([df_actual_test_labels, df_formatted_predicted_test_labels], axis=1)

acutal_pos_predicted_neg = (df['Actual'] == df['Predicted']).value_counts().to_dict()