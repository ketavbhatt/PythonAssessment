# Initialize dictionary for names
d = {}

# Initializing counter
c = 1

print("Enter pair of name : ")

while True:
	# Input pair 
	names = input()

	if names=="":
		break
	
	else:
		# Spliting pair and adding it in a list
		n=names.split()

		# If name not present in dictionary add and assign counter
		if n[0] not in d and n[1] not in d:
			d[n[0]]=c
			d[n[1]]=c
			c+=1

		# If one of the name add the new name and assign value of the old name
		else:
			if n[0] not in d:
				d[n[0]]=d[n[1]]
			else:
				d[n[1]]=d[n[0]]




	

print("Total number of groups are : ",c-1)

pair = input("Enter the pair to check their association : ")

p = pair.split()

# To check if pair is associated
if d[p[0]] == d[p[1]]:
	print("Yes")

else:
	print("No")
	