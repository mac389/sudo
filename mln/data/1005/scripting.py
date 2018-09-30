#run everything in python 
#instead of minLearnShort.sh BASH script

#must run source env.sh first

import os, json  

from MLN import *
from mlnQueryTool import MLNInfer
from pprint import pprint 

folder =  os.path.relpath('.','..')

mln = 'wts.%s.mln'%folder
mrf = "test.db"

patient_labels = json.load(open('./test_labels.json','r'))


for patient_label,patient_axioms in patient_labels.iteritems():
	query  = patient_axioms.replace('(',' ').replace(')',' ').split()[0] #Cheap way to get signature of function

#inference
inf = MLNInfer()
mlnFiles = mln
output_filename = "./results.txt"

results = {}

tasks = [("MC-SAT","PyMLNs")]

for method,engine in tasks:
	for patient_label,patient_axioms in patient_labels.iteritems():
		
		query, patient  = patient_axioms.replace('(',' ').replace(')',' ').split() #Cheap way to get signature of functions

		unformatted_results = inf.run(mln,mrf,method,str(query),engine,
			output_filename, saveResults=True, maxSteps=500, verbose=False)	

		for predicate_patient,probability in unformatted_results.iteritems():
			predicate, patient = predicate_patient.replace("("," ").replace(")"," ").split()

			if patient not in results:
				results[patient] = {}

			if predicate not in results[patient]:
				results[patient][predicate] = None

			results[patient][predicate] = float(probability)

json.dump(results,open("test_made_with_answer_key.json",'wb'))
