import os 

from problog.program import PrologString
from problog.core import ProbLog
from problog import get_evaluatable

kb = open(os.path.join('..','knowledge_base.pl'),'r').read()
axioms = open(os.path.join('..','amalgamated.axiomata'),'r').read()

p = PrologString(kb + axioms + """\n
receive(1,initial_therapy).
receive(1,standard_intake_evaluation).
query(use(1,_)).
""")

print get_evaluatable().create_from(p).evaluate()
