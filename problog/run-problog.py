import os 

from problog.program import PrologString
from problog.core import ProbLog
from problog import get_evaluatable

#from awesome_print import ap 
from pprint import pprint

kb = open(os.path.join('..','knowledge_base.pl'),'r').read()
axioms = open(os.path.join('.','amalgamated.axiomata'),'r').read()

p = PrologString(kb + '\n'+ axioms + """\n	
:- use_module(library(lists)).

person(1).
property(1,dependence,opioids).
receive(1,standard_care).
receive(1,motivational_interviewing).
property(1,location,outpatient).
query(remain(1,in_therapy,_)).
""")

#How to indicate source?

#ap(get_evaluatable().create_from(p).evaluate())
res = get_evaluatable().create_from(p).evaluate()
pprint(res)

'''
List of competency questions (stored in */{CTN}/test.pl):
1. 
	Query: What are the chances of successful opioid detoxification? 
	Expected answer: 
	  -- Inpatient, clonidine => 22% (calculated 38)
	  -- Inpatient, suboxone => 77%  (calculated 81.6)
	  -- Outpatient, clonidine => 5%  (calculated 24)
	  -- Outpatient, suboxone 29%.  (calculated 43)

(-1) (Starting from end)


	Query: 

'''