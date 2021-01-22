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
property(1,inject,fentanyl).
receive(1,therapeutic_alliance).
query(property(1,increase_attendance,counseling_and_education)).
""")
