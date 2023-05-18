import multiprocessing

def paths(m, n):
	"""Return the number of paths from one corner of an
	M by N grid to the opposite corner.

	>>> paths(2, 2)
	2
	>>> paths(5, 7)
	210
	>>> paths(117, 1)
	1
	>>> paths(1, 157)
	1
	"""
	"*** YOUR CODE HERE ***"
	if m==1 or n == 1:
		return 1
	return paths(n-1, m) + paths(n, m-1) 

if __name__ == '__main__':
	jobs = []
	for i in range(16):
		p = multiprocessing.Process(target=paths, args=(15,15))
		jobs.append(p)
		p.start()
		# print(jobs)
		print(p)