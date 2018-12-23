import os, csv, re 

from pprint import pprint 


pattern = re.compile(r'(\D+)\((\D+)\)')

MLN_PATH = os.path.join('..','data')


mln_filenames = [os.path.join(MLN_PATH,name,filename) 
					for name in os.listdir(MLN_PATH)  if os.path.isdir(os.path.join(MLN_PATH,name))
					for filename in os.listdir(os.path.join(MLN_PATH,name))
					if filename.endswith('.predicates') and 'wts' not in filename]


with open(os.path.join('..','data','amalgamated.predicates.tsv'),'w') as fout:
	#print>>fout,"\t".join(["Name","Type","Source"])
	for filename in mln_filenames: 
		study_number,_ = os.path.splitext(os.path.basename(filename))


		for item in open(filename,'r').read().splitlines():

			x = pattern.findall(item)
			if x:
				argument, predicate = x[0]
				print>>fout, '\t' + argument + '\t' + predicate
					