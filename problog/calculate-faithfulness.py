import os, json 

import numpy as np 
import pandas as pd 

from pprint import pprint 

pd.set_option('display.max_rows', None)


db = pd.read_json(os.path.join('.','schemata-consistency-test-results.json'))

print(db)

#how many nan? #13

#print(db['calculated-output'][db['calculated-output']>1])
print((db['calculated-output']-db['desired-output']).astype(float).sum())