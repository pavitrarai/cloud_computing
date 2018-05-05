import sys

def reducer():
	count_total = 0
	global_max = 0
	global_min = None
	max_friend_user = None;
	min_friend_user = None;

	for line in sys.stdin:
		data = line.strip().split("\t")

		if len(data) != 2:
		    continue

		this_key, friends_count = data
		friends_count = int(friends_count)
		if friends_count == 0:
			print("{} has no friends".format(this_key))

		if not global_min:
			global_min = friends_count
			min_friend_user = this_key

		if friends_count < global_min:
			global_min = friends_count
			min_friend_user = this_key

		if friends_count > global_max:
			global_max = friends_count
			max_friend_user = this_key


	print("{} has maximum no of friends, {} friends".format(max_friend_user,global_max))
	print("{} has minimum no of friends, {} friends".format(min_friend_user,global_min))

if __name__ == '__main__':
    reducer()