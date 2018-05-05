To execute the assignment:

cd into the directory

run the command in the terminal:
	cat <filename>.txt | python <mapper>.py | sort | python <reducer>.py 

for example, to run the question 1:

cat input.txt | python mapper1.py | sort | python reducer1.py

To write the results to a file

cat input.txt | python mapper1.py | sort | python reducer1.py > output.txt