def is_int(list):
	'''
	Takes in a list of elements of different types.
	Returns all the elements of the list of type int.
	'''
	output = [i for i in list if isinstance(i, int)]
	print output

def solve_eqn():
	'''
	Solves the equation y = x**2 + 1.
	Prints out list of integer solutions.
	'''
	output = [(x,y) for x in range(-5,6) for y in range (0,11) if y == (x**2 + 1)]
	print output


'''
x**2 + y**2 = r**2
'''

def solve_circle_eqn(a,b):
	'''
	Returns integer solutions [x,y] for a circle with radius of 5, and with center at (a,b).
	Arguments a and b are integers.
	'''
	output = [(x + a, y + b) for x in range(-5,6) for y in range (-5,6) if (x**2 + y**2 == 5**2)]
	print output