import os, json, math, random

from pprint import pprint 

n_patients = 3 

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

	tmp  = {'payload':tmp,'random_number':random.random()}

test = []
train = []

for item in db:
	if random.random() >= 0.5:
		test += item
	else:
		train += item

random.shuffle(db)

for key,value in [{"test":test},{"train":train}]:
	with open('%s.db'%key,'w') as fout:
		for item in value:
			for predicate in item:
				print>>fout,predicate
			print>>fout,'\n'