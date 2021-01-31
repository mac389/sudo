import os, json 

import numpy as np 

from problog.program import PrologString
from problog.core import ProbLog
from problog import get_evaluatable

#from awesome_print import ap 
from pprint import pprint
from tqdm import tqdm 

kb = open(os.path.join('..','knowledge_base.pl'),'r').read()
axioms = open(os.path.join('.','amalgamated.axiomata'),'r').read()

schema = json.load(open(os.path.join('.','test-schemata.json')))

annotated_unit_test = []

'''
for i,line in enumerate((kb + '\n' + axioms + """\n	
	:- use_module(library(lists)).
		
	"""+'\n').split('\n')):
	print(f'{str(i)}: {line}')
'''
for j,test in enumerate(tqdm(schema, 'Conducting Unit Test')):

	input_strings = kb + '\n' + axioms + """\n	
	:- use_module(library(lists)).
		
	"""+'\n'+test['input']
	p = PrologString(input_strings)
	
	predicted = np.nan

	try:
		res = get_evaluatable().create_from(p).evaluate()
		_, predicted = list(res.items()).pop()

	except Exception as e:
		print(e, predicted, f'axiom no. {str(j)}')
		print(test['input'])
	
	cargo = {**test,  **{'calculated-output':predicted}}

	#Probably need unambiguous identifier for each axiom. 
	
	annotated_unit_test += [cargo]

json.dump(annotated_unit_test, open(os.path.join('.','schemata-consistency-test-results.json'),'w'))