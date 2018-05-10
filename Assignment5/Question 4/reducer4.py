import sys

def reducer():
	dept_name = None
	total_employee = None
	old_key = None
	for line in sys.stdin:
		data = line.strip().split("\t")
		this_key = data[0]

		if old_key and old_key != this_key:
			print(dept_name+"\t"+total_employee)

		old_key = this_key
		if data[1] == '-':
			total_employee = data[2]
		elif data[2] == '-':
			dept_name = data[1]
	
	if old_key != None:
		print(dept_name+"\t"+total_employee)


if __name__ == '__main__':
    reducer()