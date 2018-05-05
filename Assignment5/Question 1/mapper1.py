import sys
def mapper():
    for line in sys.stdin:
        data = line.strip().split()
        for word in data:
        	if(word != " "):
        		print("{}\t{}".format(word,1));

if __name__ == '__main__':
	mapper()