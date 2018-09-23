import os

MLN_PATH = os.path.join('..','mln','data')

for directory in os.listdir(MLN_PATH):
	print directory
	if os.path.isdir(directory):
		print directory