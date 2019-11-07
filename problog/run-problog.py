import os 

from problog.program import PrologString
from problog.core import ProbLog
from problog import get_evaluatable


axioms = open(os.path.join('..','amalgamated.axiomata'),'r').read()
print axioms 


p = PrologString(axioms + """\n
person(1).
receive(1,initial_therapy)
receive(1,standard_intake_evaluation).
query(stay_in_therapy(1,n84_day)).
""")

print get_evaluatable().create_from(p).evaluate()
