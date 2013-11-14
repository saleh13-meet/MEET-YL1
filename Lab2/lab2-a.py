print "Please enter a number"

x = int(raw_input())

def divisors(n):

	for i in range(1,n+1):
		if (n%i==0):
			print i

divisors(x)
