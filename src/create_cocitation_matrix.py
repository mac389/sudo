import pymongo, json, sys, random

import pandas as pd 
import numpy as np 

from pymongo import MongoClient
from pprint import pprint 
from collections import defaultdict
from itertools import combinations
from pprint import pprint 
from tqdm import tqdm 


#This will not work if the author information is scattered across multiple databases. 
#In that case add an additional line to iterate over collection_names()
def get_all_pmids(author_name,db):
	return list(set([item['Article Identifiers']['pubmed'] 
			for item in db.find({"Full Name":author_name}) if 'pubmed' in item['Article Identifiers']]))

def count_common_papers(author_one,author_two,db):
	return len(set(get_all_pmids(author_one,db)) & set(get_all_pmids(author_two,db)))


def main(client,db_name,collection_name, author_list=None):
	db = client[db_name][collection_name]

	interaction_dictionary = defaultdict(list)

	if author_list:
		if '.xls' in author_list:
			df = pd.read_excel(open(author_list,'rb'))
			#Will need to specxify format here, if different from Head/Neck
			df.columns = ['Author Name']

			author_names = df['Author Name'].values
			interaction_matrix = np.zeros((author_names.shape[0],author_names.shape[0]),dtype=int)
			#Specifying int saves space

		elif author_list.endswith('.txt'):
			author_names = open(author_list,'rb').read().splitlines()
			interaction_matrix = np.zeros((len(author_names),len(author_names)), dtype=int)
			#Specifying int saves space

	else:
		author_names = list(set([item['Full Name'] for item in db.find({},{"Full Name":1})]))
		#author_names = random.sample(author_names,200)
		interaction_matrix = np.zeros((len(author_names),len(author_names)), dtype=int)
		#Specifying int saves space


	for i,j in tqdm(zip(*np.triu_indices(len(author_names))), 'Computing Co-Author Counts'):
		interaction_matrix[i,j] = count_common_papers(author_names[i],author_names[j],db)
		interaction_dictionary[author_names[i]] += [(author_names[j],interaction_matrix[i,j])]


	#Add Transpose
	interaction_matrix += interaction_matrix.T

	#Double counted diagonal when adding transpose
	#Simpler than juggling indices from upper to lower triangles
	interaction_matrix[np.diag_indices_from(interaction_matrix)] /= 2

	df_aa = pd.DataFrame(data=interaction_matrix,index=author_names,columns=author_names)
	df_aa.to_csv('./data/author-author-matrix-full.csv', encoding='utf-8')

	json.dump(interaction_dictionary,open('./data/interaction_dictionary-full.json','wb'))

	print 'Finished'