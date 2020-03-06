import os, json, itertools

import networkx as nx
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 

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
weights = np.log([G[u][v]['weight'] for u,v in G.edges()])


nx.draw(G, pos=nx.nx_agraph.pygraphviz_layout(G, prog='neato'), with_labels=True, node_size=1000, 
		face_color='w', linewidths=1.5, edge_color=weights, edge_cmap=plt.cm.bone_r)
plt.savefig(os.path.join('../social-network.png'),dpi=600,bbox_inches='tight')



'''
sns.heatmap(df)
plt.show()
'''
'''
pos = nx.get_node_attributes(G,'posxy')
print(pos)
### Output for tikz-network

#Edges
df = pd.DataFrame([[5*pos[key][0],5*pos[key][1],True] for key in db.keys()],
		columns=['x','y','IdAsLabel'], index=db.keys())

df.to_csv('../vertices.csv', index_label='id')
'''