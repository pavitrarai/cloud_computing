import sys

def mapper():
	for line in sys.stdin:
		data = line.strip().split('|')
		track = data[1]
		radio = data[3]
		print(track+"\t"+radio)

if __name__ == '__main__':
	mapper()