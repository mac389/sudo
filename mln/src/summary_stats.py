import os, json, itertools

import numpy as np 
MLN_PATH = os.path.join('..','data')


def parse(filename):
	text = open(filename).read().splitlines()
	return text

flags = ['//','log']

def count_axioms(lst):
	return sum(1 for item in lst if not any([flag in item for flag in flags]))


axioms = {}
for directory in os.listdir(MLN_PATH):
	if os.path.isdir(os.path.join(MLN_PATH,directory)):
		for file in os.listdir(os.path.join(MLN_PATH,directory)):
			if file.endswith('.mln') and not file.startswith('w'):
				#All files with computed formula weights start with w
				parsed = parse(os.path.join(MLN_PATH,directory,file))
				axioms[file.split('.')[0]] = count_axioms(parsed)

'''
print sum(axioms.values())/float(len(axioms))
print np.median(axioms.values())
print np.std(axioms.values())

print np.percentile(axioms.values(),25)
print np.percentile(axioms.values(),75)

print 0.5*(np.percentile(axioms.values(),75)-np.percentile(axioms.values(),25))
'''

json.dump(axioms,open(os.path.join('..','data','axiom_count.json'),'w'))

