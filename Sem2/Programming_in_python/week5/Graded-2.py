def user_score(read_count, reply_count, new_post_count):
	return 'Leader' if 1*read_count + 3*reply_count + 5*new_post_count > 50 else 'Basic'