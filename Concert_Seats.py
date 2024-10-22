def can_one_see_stage(seats, i, j):
	"""A number can "see" the front-stage if it is strictly greater than the number before it."""
	if j == 0:
		return True
	return seats[j][i] > seats [j-1][i]

def can_see_stage(seats):
	for j, row in enumerate(seats):
		for i in range(len(row)):
			if can_one_see_stage(seats, i, j):
				continue
			return False
	return True