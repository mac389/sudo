#run everything in python 
#instead of minLearnShort.sh BASH script

#must run source env.sh first

import os, json  

from tqdm import tqdm 
from MLN import *
from pprint import pprint 

folder =  os.path.relpath('.','..')

mln_filename = 'wts.%s.mln'%folder
mrf_filename = "test.db"

patient_labels = json.load(open('./test_labels.json','r'))

mln = MLN(mln_filename)
mrf = mln.groundMRF(mrf_filename)
results = {}

tasks = [("MC-SAT","PyMLNs")]

queries = [str(query+"("+patient+")") for patient, query in patient_labels.iteritems()]

probabilities = mrf.inferMCSAT(queries, verbose=False)

for (patient, query), probability in zip(patient_labels.iteritems(),probabilities):
		if patient not in results:
			results[patient] = {}

		results[patient][query] = float(probability)

json.dump(results,open("predicted_labels.json",'wb'))
