import sys

def reducer():
	count_total = 0
	old_key = None

	for line in sys.stdin:
		data = line.strip().split()

		if len(data) != 1:
		    continue

		this_key = data[0]

		if old_key and old_key != this_key:
			count_total += 1

		old_key = this_key
	
	if old_key:
		count_total += 1
	
	print("Total No of unique listeners: ", count_total)

if __name__ == '__main__':
    reducer()