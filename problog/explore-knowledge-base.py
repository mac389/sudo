import os 
from pprint import pprint 

import pandas as pd
import networkx as nx 
import matplotlib.pyplot as plt

df = pd.read_csv(os.path.join('.','axiomata-for-uml-analysis.csv'), delimiter='\t')

'''
targets = df[['target','label']].copy(deep=True)
targets.drop_duplicates(subset='target',inplace=True)
targets['group'] = 'CTN'
targets['coloring'] = 'black'
targets.rename(columns={'target':'node'}, inplace=True)

sources = df[['source','label']].copy(deep=True)
sources.drop_duplicates(subset='source', inplace=True)
sources['group'] = 'KB'
sources['coloring'] = 'red'
sources.rename(columns={'sources':'node'}, inplace= True)

nodes = {**targets.to_dict(orient='index'), **sources.to_dict(orient='index')}
'''
g = nx.from_pandas_edgelist(df)


#nx.set_node_attributes(g,pd.Series(df.target, index=df.group).to_dict(),'group')
#nx.draw(g, node_color=[nodes[idx]['coloring'] for idx in g])
#plt.show()
