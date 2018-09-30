import os, json, math, random

from pprint import pprint 

n_patients = 10 

axioms = [x.strip() for x in open('1005.predicates','r').read().splitlines() if x]
n_axioms_per_patient = int(math.floor(0.6*len(axioms)))
db = []

for i in xrange(n_patients):
	tmp = [random.sample(axioms,n_axioms_per_patient)]
	#Assume default argument is "person" in all predicates. 
	#I should eventually remove this harcoded solution.
	tmp = [axiom.replace('person','patient_%d'%i) for axiom in axioms]


	#10% of the time randomly negate something
	if random.random() < 0.10:
		idx = random.choice(xrange(n_axioms_per_patient))
		tmp[i] = '!' + tmp[i]
	
	#Logic clean-up
	#Don't think it's needed for these axioms

	db += [{'payload':tmp,'random_number':random.random()}]

test = []
train = []

for item in db:
	if random.random() >= 0.5:
		test += [item['payload']]
	else:
		train += [item['payload']]
random.shuffle(db)

with open('train.db','w') as fout:
	for patient in train:
		for predicate in patient:
			print>>fout,predicate
		print>>fout,'\n'

#Prepare test db by leaving one out
#And then can ask about other inferences, capture all data

test_labels = {}
with open('test.db','w') as fout:
	for patient in test:

		idx_to_leave_out = random.choice(xrange(len(patient)))
		patient_no = patient[idx_to_leave_out].replace(')',' ').replace('(',' ').split()[-1]

		test_labels[patient_no] = patient[idx_to_leave_out]
		patient[idx_to_leave_out] = '//'+ patient[idx_to_leave_out]

		for predicate in patient:
			print>>fout,predicate
		print>>fout,'\n'

json.dump(test_labels,open('./test_labels.json','w'))