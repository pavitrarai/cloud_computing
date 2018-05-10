import sys

def mapper():
	infile = sys.stdin
	table = None
	for line in infile:
		data = line.strip().split('\t')
		dept_id = None
		dept_name = '-'
		total_employee = '-' 
		if(data[1] == "DEPT_NAME"):
			table = 'A'
		elif(data[1] == "TOTAL_EMPLOYEE"):
			table = 'B'
		else:
			if(table == 'A'):
				dept_id = data[0]
				dept_name = data[1]
			elif(table == 'B'):
				dept_id = data[0]
				total_employee = data[1]
			print(dept_id+"\t"+dept_name+"\t"+total_employee)

if __name__ == '__main__':
	mapper()