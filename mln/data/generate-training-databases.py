import os, json, math, random

from tqdm import tqdm
'''
TODO:
  
   Add ability to take command line arguments to specify a selection of studies to use
'''

from pprint import pprint 
n_patients = 100

for filename in tqdm(os.listdir(os.getcwd()), 'Making words.'):
	if os.path.isdir(os.path.join(os.getcwd(),filename)):
		predicate_filename = os.path.join(os.getcwd(),filename,'%s.predicates'%filename)
		axioms = [x.strip() for x in open(predicate_filename,'r').read().splitlines() if x]
		n_axioms_per_patient = max(3,int(math.floor(0.6*len(axioms))))
		
		db = []
		for i in xrange(n_patients):
			tmp = random.sample(axioms,n_axioms_per_patient)
			#Assume default argument is "person" in all predicates. 
			#I should eventually remove this harcoded solution.

			for axiom in tmp:
				if 'person' in axiom:
					axiom.replace('person','patient_%d'%i)
				if 'specify_domain.json' in os.listdir(os.path.join(os.getcwd(),filename)):
					other_variables = json.load(open(os.path.join(os.getcwd(),filename,'specify_domain.json'),'r'))					
					for other_variable in other_variables:
						if other_variable in axiom:
							axiom.replace(other_variable,random.choice(other_variables[other_variable]))
			
			#tmp = [axiom.replace('person','patient_%d'%i) for axiom in tmp]



			#10% of the time randomly negate something
			if random.random() < 0.10:
				idx = random.choice(xrange(n_axioms_per_patient))
				tmp[idx] = '!' + tmp[idx]
			
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

		with open(os.path.join(os.getcwd(),filename,'train.db'),'w') as fout:
			for patient in train:
				for predicate in patient:
					print>>fout,predicate
				print>>fout,'\n'

		#Prepare test db by leaving one out
		#And then can ask about other inferences, capture all data

		test_labels = {}
		with open(os.path.join(os.getcwd(),filename,'test.db'),'w') as fout:
			for patient in test:

				idx_to_leave_out = random.choice(xrange(len(patient)))
				predicate = patient[idx_to_leave_out].replace(')',' ').replace('(',' ').split()[0]
				#function is, effectively, prefix notation

				test_labels['patient_%d'%idx_to_leave_out] = predicate
				patient[idx_to_leave_out] = '//'+ patient[idx_to_leave_out]

				for predicate in patient:
					print>>fout,predicate
				print>>fout,'\n'

		json.dump(test_labels,open(os.path.join(os.getcwd(),filename,'test_labels.json'),'w'))