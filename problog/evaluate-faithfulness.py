import os, json 

from problog.program import PrologString
from problog.core import ProbLog
from problog import get_evaluatable

#from awesome_print import ap 
from pprint import pprint

kb = open(os.path.join('..','knowledge_base.pl'),'r').read()
axioms = open(os.path.join('.','amalgamated.axiomata'),'r').read()

schema = json.load(open(os.path.join('.','test-schemata.json')))

for test in schema:

	p = PrologString(kb + '\n' + axioms + """\n	
	:- use_module(library(lists)).
		
	"""+'\n'+test['input'])
	
	res = get_evaluatable().create_from(p).evaluate()
	pprint(res)
