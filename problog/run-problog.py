import os 

from problog.program import PrologString
from problog.core import ProbLog
from problog import get_evaluatable

#from awesome_print import ap 
from pprint import pprint

kb = open(os.path.join('..','knowledge_base.pl'),'r').read()
axioms = open(os.path.join('.','amalgamated.axiomata'),'r').read()

p = PrologString(kb + '\n'+ axioms + """\n	

person(1,male).
dependent(1,opioids).
use(1,cocaine,before).
receive(1,buprenorphine_naloxone).
receive(1,motivational_enhancement).
receive(1,standard_care).
hispanic(1).
taper(1,buprenorphine,n7_days).

evidence(outpatient(1),true).
evidence(hispanic(1),true).

query(detoxification(1,opioid,success)).
query(remain(X,in_therapy,_)).
query(use(1,_,_)).
query(taper(1,_,_)).
query(sample(1,urine,opioids,_,_)).
""")

#How to indicate source?

#ap(get_evaluatable().create_from(p).evaluate())
res = get_evaluatable().create_from(p).evaluate()
pprint(res)

'''
   Don't debug away all InconsistentError messages, Only those that involve reasoning
   over the results of more than one study. 
'''


'''
List of competency questions (stored in */{CTN}/test.pl):
1. 
	Query: What are the chances of successful opioid detoxification? 
	Expected answer: 
	  -- Inpatient, clonidine => 22% (calculated 38)
	  -- Inpatient, suboxone => 77%  (calculated 81.6)
	  -- Outpatient, clonidine => 5%  (calculated 24)
	  -- Outpatient, suboxone 29%.  (calculated 43)

2. 
	Query: 

'''