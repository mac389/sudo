import os 
from pprint import pprint 

kb = open(os.path.join('..','knowledge_base.pl'),'r').read()
axioms = open(os.path.join('.','amalgamated.axiomata'),'r').read()

text = kb + '\n' + axioms

pprint(text.split('\n\n'))