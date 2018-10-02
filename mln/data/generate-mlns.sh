mlnLearningTool DOES NOT WORK IN SCRIPTS

for var in find ./*/*.mln; do
	db=${var%/*.mln}/test.db
	results=${var%/*.mln}/trained.mln
	echo $var
	python ../../../ProbCog/src/main/python/mlnLearningTool.py -i $var -o $results -t $db --run
done