import json, nltk, os 

from pprint import pprint 

db = json.load(open(os.path.join('..','data','text-of-abstracts.json'),'r'))

for trial in 