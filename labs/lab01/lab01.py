"""Lab 1: Expressions and Control Structures"""

def both_positive(a, b):
	"""Returns True if both a and b are positive.

	>>> both_positive(-1, 1)
	False
	>>> both_positive(1, 1)
	True
	"""
	return a > 0  and b > 0 # You can replace this line!

def sum_digits(x):
	"""Sum all the digits of x.

	>>> sum_digits(10) # 1 + 0 = 1
	1
	>>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
	12
	>>> sum_digits(1234567890)
	45
	>>> a = sum_digits(123) # make sure that you are using return rather than print
	>>> a
	6
	"""
	keepgoing = 1
	y = 1
	while keepgoing:
		print("DEBUG: keepgoing start of loop: ",keepgoing)
		highest_pow_10 = y/10
		keepgoing = x//y
		# print(y)
		y = y * 10
	print("DEBUG: highest_pow_10: ", highest_pow_10)
	keepgoing = 1
	sum = 0
	while keepgoing:
		sum = sum + x//highest_pow_10
		print("DEBUG: sum: ",sum)
		x = x -(x//highest_pow_10)*highest_pow_10
		highest_pow_10= highest_pow_10/10
		print("DEBUG: x: ",x)
		keepgoing = x
	return int(sum)
	
	
	"*** YOUR CODE HERE ***"

def falling(n, k):
	"""Compute the falling factorial of n to depth k.

	>>> falling(6, 3)  # 6 * 5 * 4
	120
	>>> falling(4, 3)  # 4 * 3 * 2
	24
	>>> falling(4, 1)  # 4
	4
	>>> falling(4, 0)
	1
	"""
	"*** YOUR CODE HERE ***"

def double_eights(n):
	"""Return true if n has two eights in a row.
	>>> double_eights(8)
	False
	>>> double_eights(88)
	True
	>>> double_eights(2882)
	True
	>>> double_eights(880088)
	True
	>>> double_eights(12345)
	False
	>>> double_eights(80808080)
	False
	"""
	"*** YOUR CODE HERE ***"