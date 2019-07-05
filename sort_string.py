# Given lexicographical order
lex_order =  ["r" , "c", "t" , "a"]

string=''

for i in lex_order:
	string+=i

a=[]

print("Enter strings : ")

while True:
	# Enter input and enter blank to exit
	s=input()
	if s =='':
		break;
	else:
		a.append(s)


print("The sorted list of string are as follow: ")

print(sorted(a, key=lambda word: [string.index(c) for c in word]))