import sys

def mapper():
	for line in sys.stdin:
		data = line.strip().split('->')
		user = data[0].strip()
		friends = len(data[1].split())
		print(user+"\t"+str(friends))

if __name__ == '__main__':
	mapper()