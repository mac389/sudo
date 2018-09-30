import os 

from pprint import pprint 

MLN_PATH = os.path.join('..','data')


mln_filenames = [os.path.join(MLN_PATH,name,filename) 
					for name in os.listdir(MLN_PATH)  if os.path.isdir(os.path.join(MLN_PATH,name))
					for filename in os.listdir(os.path.join(MLN_PATH,name))
					if filename.endswith('.predicates') and 'wts' not in filename]


with open(os.path.join('..','data','amalgamated.predicates'),'w') as fout:
	for filename in mln_filenames: 
		study_number,_ = os.path.splitext(os.path.basename(filename))

		print>>fout,'//Study No. %s'%study_number
		print>>fout,'\n'.join(open(filename,'r').read().splitlines())
		print>>fout,'\n'