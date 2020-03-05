import os, json 


db  = {}

MLN_FOLDER = os.path.join('..','problog','could-create-mln-file')
for name in os.listdir(MLN_FOLDER):
	if os.path.isdir(os.path.join(MLN_FOLDER,name)):
		filename = os.path.join(MLN_FOLDER,name,'formatted.logic')
		x = open(filename).read()
		print(x.split('\n\n'))
