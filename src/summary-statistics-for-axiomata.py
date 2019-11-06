import csv, os, re

import numpy as np 

from pprint import pprint 
from ast import literal_eval

filename = os.path.join('..','jamia-axiomata.csv')
pattern = re.compile(r'([_a-zA-z\\]+)\(([a-zA-z0-9,\s+\\]+)\)')
contents = list(csv.DictReader(open(filename,'r'),delimiter='\t',skipinitialspace=True))

axiomata = [item['converted'] for item in contents if item['flag']=='done']

predicates = []
arguments = []
argument_counts = []
for axiom in axiomata:
	x = pattern.findall(axiom)
	if x:
		predicate,argument = x[0]
		args = argument.split(',')
		predicates +=["%s/%d"%(predicate,len(args))]
		arguments += args
	else:
		not_parseable += [axiom]

'''
print(len(predicates),len(set(predicates)))
print(len(arguments),len(set(arguments)))
'''

