import csv, os 

filename = os.path.join('..','jamia-axiomata.csv')
contents = list(csv.DictReader(open(filename,'r'),delimiter='\t',skipinitialspace=True))

PATH = os.path.join('..','problog','could-create-mln-file')

for name in os.listdir(PATH):
	if os.path.isdir(os.path.join(PATH,name)):
		axioms = open(os.path.join(PATH,name,'abstract.logic'),'r')
		
