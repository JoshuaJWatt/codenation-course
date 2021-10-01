# A1 - 

films = ["The Godfather", "The Shawshank Redemption", "Schindler's List", "Raging Bull"]

def filmCheck(list):
	for i in films:
		if i == "Ghostbusters":
			print("yey it's ghostbusters")
		else:
			print("boo, I want ghostbusters")
	return()



# A2 - check whether all the numbers between 1 and 20 are prime.

# The cheat way:
primes = [2, 3, 5, 7, 11, 13, 17, 19]

for i in range(21):
	if i in primes:
		print(i, "is a prime")

# The proper way:
def checkprime(prrange = [1,20]):
	for i in range(prrange[0], prrange[1]+1):
		isprime = 1
		for j in range(2, i):
			if i % j == 0:
				isprime = 0
		if isprime == 1:
			print(i, "is prime")

checkprime()



