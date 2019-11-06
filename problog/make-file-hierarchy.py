import json, os

from pprint import pprint 

abstracts = json.load(open(os.path.join('..','data','text-of-abstracts.json'),'r'))

for abstract in abstracts:
	path = os.path.join('..','problog','ctn',abstract)
	if not os.path.exists(path):
		os.makedirs(path)

	with open(os.path.join(path,'abstract.txt'),'w') as fout:
		fout.write(abstracts[abstract])