import sys

def reducer():
    count_total = 0
    old_key = None
    
    for line in sys.stdin:
        data = line.strip().split("\t")

        if len(data) != 2:
            continue

        this_key, this_count = data

        if old_key and old_key != this_key:
            print("{}\t{}".format(old_key, count_total))
            count_total = 0

        old_key = this_key
        count_total += int(this_count)

    if old_key != None:
        print("{}\t{}".format(old_key, count_total))

if __name__ == '__main__':
    reducer()