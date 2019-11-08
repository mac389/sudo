import os 

from problog.program import PrologString
from problog.core import ProbLog
from problog import get_evaluatable

#from awesome_print import ap 
from pprint import pprint

kb = open(os.path.join('..','knowledge_base.pl'),'r').read()
axioms = open(os.path.join('.','amalgamated.axiomata'),'r').read()

p = PrologString(kb + '\n'+ axioms + """\n	
person(1).
dependent(1,opioids).
evidence(outpatient(1),false).
evidence(adult(1),true).
evidence(male(1),true).
receive(1,buprenorphine_naloxone).
query(detoxification(1,opioid,success)).
query(sample(1,urine,opioids,_,_)).
""")

#How to indicate source?

#ap(get_evaluatable().create_from(p).evaluate())
pprint(get_evaluatable().create_from(p).evaluate())
'''
   Don't debug away all InconsistentError messages, Only those that involve reasoning
   over the results of more than one study. 
'''


'''
List of competency questions:
1. 
	Query: What are the chances of successful opioid detoxification? 
	Expected answer: 
	  -- Inpatient, clonidine => 22%
	  -- Inpatient, suboxone => 77%
	  -- Outpatient, clonidine => 5%
	  -- Outpatient, buprenorphine 29%



'''