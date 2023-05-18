HW_SOURCE_FILE = 'hw03.py'

#############
# Questions #
#############

def num_sevens(x):
	"""Returns the number of times 7 appears as a digit of x.

	>>> num_sevens(3)
	0
	>>> num_sevens(7)
	1
	>>> num_sevens(7777777)
	7
	>>> num_sevens(2637)
	1
	>>> num_sevens(76370)
	2
	>>> num_sevens(12345)
	0
	"""
	"*** YOUR CODE HERE ***"
	if x < 10:
		if x == 7:
			return 1
		return 0
	all_but_last, last = x // 10, x % 10
	if last == 7:
		count = 1
	else:
		count = 0
	return num_sevens(all_but_last) + count

def pingpong(n):
	"""Return the nth element of the ping-pong sequence.

	>>> pingpong(7)
	7
	>>> pingpong(8)
	6
	>>> pingpong(15)
	1
	>>> pingpong(21)
	-1
	>>> pingpong(22)
	0
	>>> pingpong(30)
	6
	>>> pingpong(68)
	2
	>>> pingpong(69)
	1
	>>> pingpong(70)
	0
	>>> pingpong(71)
	1
	>>> pingpong(72)
	0
	>>> pingpong(100)
	2
	"""
	"*** YOUR CODE HERE ***"
	# k = 1
	# value = 0
	# count_direction = 1
	# while k <= n:
		# value = value + 1*count_direction
		# if num_sevens(k) or (k % 7) ==0:
			# print("DEBUG: swtich ", k)
			# count_direction = count_direction * -1
		# k = k + 1
	# return value
	def helper(n ,i,count,direction):
		if i == n:
			return count
		if num_sevens(i) or (i % 7) ==0:
			direction = direction * -1
		return helper(n, i + 1, count + direction, direction)
	return helper(n,1,1,1)

def count_change(total):
	"""Return the number of ways to make change for total.

	>>> count_change(7)
	6
	>>> count_change(10)
	14
	>>> count_change(20)
	60
	>>> count_change(100)
	9828
	"""
	# def bullshit():
	
		# return bullshit()
	
	# return bullshit()
	"*** YOUR CODE HERE ***"
	# def bullshit():
	
		# return bullshit()
	
	# return bullshit()
	def largest_factor_of_two(number, factor):
		if number//factor == 1:
			return factor
		return largest_factor_of_two(number, factor*2)
	
	def c(n, m):
			"""Count the ways to partition n using parts up to m."""
			if n == 0:
				return 1
			elif n < 0:
				return 0
			elif m == 1/2:
				return 0
			else:
				return c(n-m, m) + c(n, m/2)
	return c(total,largest_factor_of_two(total, 1))

	
def missing_digits(n):
	"""Given a number a that is in sorted, increasing order,
	return the number of missing digits in n. A missing digit is
	a number between the first and last digit of a that is not in n.
	>>> missing_digits(1248) # 3, 5, 6, 7
	4
	>>> missing_digits(1122) # No missing numbers
	0
	>>> missing_digits(123456) # No missing numbers
	0
	>>> missing_digits(3558) # 4, 6, 7
	3
	>>> missing_digits(4) # No missing numbers between 4 and 4
	0
	"""
	"*** YOUR CODE HERE ***"
	def split(n):
		"""Split a positive integer into all but its last digit and its last digit."""
		return n // 10, n % 10

	def mdh(but_last,last, num_missing):
		if but_last == 0:
			return num_missing
		new_but_last, new_last = split(but_last)
		print("DEBUG: New_Last Last",new_last, last )
		
		if (new_last != last -1) and (new_last != last):
			num_missing = num_missing + 1
			return mdh(but_last, last -1, num_missing)
		
		return mdh(new_but_last, new_last, num_missing)
	ABL,L= split(n)
	return mdh(ABL,L,0)
def split(n):
	"""Split a positive integer into all but its last digit and its last digit."""
	return n // 10, n % 10
def mdh(but_last,last, num_missing):
	if but_last == 0:
		return num_missing
	new_but_last, new_last = split(but_last)
	print("DEBUG: New_Last Last",new_last, last )
	
	if (new_last != last -1) and (new_last != last):
		num_missing = num_missing + 1
		return mdh(but_last, last -1, num_missing)
	
	return mdh(new_but_last, new_last, num_missing)
	


###################
# Extra Questions #
###################

def print_move(origin, destination):
	"""Print instructions to move a disk."""
	print("Move the top disk from rod", origin, "to rod", destination)

def move_stack(n, start, end):
	"""Print the moves required to move n disks on the start pole to the end
	pole without violating the rules of Towers of Hanoi.

	n -- number of disks
	start -- a pole position, either 1, 2, or 3
	end -- a pole position, either 1, 2, or 3

	There are exactly three poles, and start and end must be different. Assume
	that the start pole has at least n disks of increasing size, and the end
	pole is either empty or has a top disk larger than the top n start disks.

	>>> move_stack(1, 1, 3)
	Move the top disk from rod 1 to rod 3
	>>> move_stack(2, 1, 3)
	Move the top disk from rod 1 to rod 2
	Move the top disk from rod 1 to rod 3
	Move the top disk from rod 2 to rod 3
	>>> move_stack(3, 1, 3)
	Move the top disk from rod 1 to rod 3
	Move the top disk from rod 1 to rod 2
	Move the top disk from rod 3 to rod 2
	Move the top disk from rod 1 to rod 3
	Move the top disk from rod 2 to rod 1
	Move the top disk from rod 2 to rod 3
	Move the top disk from rod 1 to rod 3
	"""
	assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
	"*** YOUR CODE HERE ***"

from operator import sub, mul

def make_anonymous_factorial():
	"""Return the value of an expression that computes factorial.

	>>> make_anonymous_factorial()(5)
	120
	>>> from construct_check import check
	>>> # ban any assignments or recursion
	>>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
	True
	"""
	return 'YOUR_EXPRESSION_HERE'