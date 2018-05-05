import sys

def mapper():
	for line in sys.stdin:
		data = line.strip().split('|')
		user = data[0]
		print(user)

if __name__ == '__main__':
	mapper()