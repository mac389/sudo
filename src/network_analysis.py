import os, json, itertools

import networkx as nx
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 

from tqdm import tqdm 

db = {}
PROBLOG_PATH = os.path.join('..','problog','could-create-mln-file')

for name in os.listdir(PROBLOG_PATH):
	if os.path.isdir(os.path.join(PROBLOG_PATH,name)):
		db[name] = json.load(open(os.path.join(PROBLOG_PATH,name,'roster.json')))


df = pd.DataFrame(0,index=db.keys(), columns=db.keys())

for one,two in itertools.combinations(db.keys(),2):
	#Jaccard Similarity
	one_text = db[one]['predicates'] + db[one]['atoms']
	two_text = db[two]['predicates'] + db[two]['atoms']

	js = len(set(one_text) & set(two_text))/float(len(set(one_text) | set(two_text)))
	
	df.loc[one,two] = js
	df.loc[two,one] = js

G=nx.from_pandas_adjacency(df)
nx.draw(G)
plt.show()