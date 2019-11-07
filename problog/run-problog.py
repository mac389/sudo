import os 

from problog.program import PrologString
from problog.core import ProbLog
from problog import get_evaluatable

kb = open(os.path.join('..','knowledge_base.pl'),'r').read()
axioms = open(os.path.join('..','amalgamated.axiomata'),'r').read()

p = PrologString(kb + '\n'+ axioms + """\n
person(1).
adult(1).
male(1).
caucasian(1).
outpatient(1).
evidence(receive(X,buprenorphine_naloxone),false).
query(detoxification(1,opioid,_)).
trace(query(use(1,_))).
""")

print get_evaluatable().create_from(p).evaluate()
