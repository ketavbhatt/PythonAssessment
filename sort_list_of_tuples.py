from ast import literal_eval

def sortTuple(l):
	# Sorting based on last element of tuple
	l=sorted(l,key = lambda x: x[-1])  
	return l


# Enter the list of tuples in the following form : (2,1),(3,4),(2,2)
l = literal_eval(input("Please enter the data: "))


print(sortTuple(l))


