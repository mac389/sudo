import csv, os 

from tqdm import tqdm 
from pprint import pprint

filename = os.path.join('..','jamia-axiomata.csv')
contents = list(csv.DictReader(open(filename,'r'),delimiter='\t',skipinitialspace=True))

PATH = os.path.join('..','problog','could-create-mln-file')

translation_table = {item['original']:item['converted'] for item in contents}

for name in tqdm(os.listdir(PATH),'Formatting axiomata'):
	if os.path.isdir(os.path.join(PATH,name)):
		axioms = open(os.path.join(PATH,name,'abstract.logic'),'r').read()
		for string in contents:
			for string in translation_table:
				if string in axioms:
					axioms = axioms.replace(string,translation_table[string])
		with open(os.path.join(PATH,name,'formatted.logic'), 'w') as out:
			out.write(axioms)
