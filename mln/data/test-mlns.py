
import os, json, math, random
from tqdm import tqdm

#must run source env.sh first
'''
TODO:
  
   Add ability to take command line arguments to specify a selection of studies to use
'''

from MLN import *
from pprint import pprint 
n_patients = 100

for folder in tqdm(os.listdir(os.getcwd()), 'Evaluating'):
	if os.path.isdir(os.path.join(os.getcwd(),folder)):
		#print folder
		LOCAL_PATH = os.path.join(os.getcwd(),folder)
		
		mln_filename = os.path.join(LOCAL_PATH,'wts.%s.mln'%folder)
		mrf_filename = os.path.join(LOCAL_PATH,"test.db")

		patient_labels = json.load(open(os.path.join(LOCAL_PATH,'test_labels.json'),'r'))

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

		json.dump(results,open(os.path.join(LOCAL_PATH,"predicted_labels.json"),'w'))
