import sys

def mapper():
	for line in sys.stdin:
		data = line.strip().split('|')
		track = data[1]
		shared = data[2]
		print(track+"\t"+shared)

if __name__ == '__main__':
	mapper()