import sys

def mapper():
	for line in sys.stdin:
		data = line.strip().split('|')
		track = data[1]
		skipped = data[4]
		print(track+"\t"+skipped)

if __name__ == '__main__':
	mapper()