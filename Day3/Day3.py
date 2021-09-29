
def namecheck():
	name = input("Gib name: ")

	try: 
		int(name)
		print("That's not a name, it's a number")
	except ValueError:
		if name:
			print("Hello {}, how are you?".format(name))
		else:
			print("You did not give me your name!")
	return


# A1 - Create a variable called password.
# Check how many letters are in the password, if there
# are less than 8 print that the password is too short.
# Otherwise print the password.

input_ = input("password: ")

if len(input_) < 8:
	print("Too short")
else:
	print(input_)

# A2 - Create a variable called num.
# Check if the variable is divisible by 3 or 5. If it is print
# “This number is divisible by 3 or 5” to the console.
# Otherwise log “This number is not divisible by 3 or 5”

input_ = int(input("gimme a number: "))

if(input_ % 3 == 0 or input_ % 5 == 0):
	print("that's divisible by 5 or 3")
else:
	print("that's not divisible by 5 or 3")

# A3 - Create a variable called num.
# If num is divisible by 3 print “fizz”, if it’s divisible by 7
# print “buzz”, if it’s divisible by both 3 and 7 print “fizz
# buzz”. Otherwise print num.

# This is probably not the optimum fizz-buzz.

input_ = int(input("gimme a number: "))

if(input_ % 3 == 0 and input_ % 7 == 0):
	print("fizz buzz")
elif(input_ % 3 == 0):
	print("fizz")
elif(input_ % 7 == 0):
	print("buzz")
else:
	print(input_)

# A4 - Create a variable called word that takes a string.
# Create an if statement that checks if the last letter is
# the same as the first. If it is return true, otherwise
# return false.

input_ = input("gimme a word: ")

if(input_[0] == input_[len(input_)-1]):
	print("true")
else:
	print("false")

# A5 - Create a variable called time, a variable called
# place_of_work and a variable called town_of_home.
# Create an if statement that prints where someone is
# at times of the day. E.g. if the time is 7 I’m at home, at
# 8 I’m commuting, at 9 I’m at work

input_ = int(input("what hour is it?: "))
commuting = 8;
work = 9;

if input_ == commuting:
	print("The time is {}, I am commuting".format(input_))
elif input_ == work:
	print("The time is {}, I am at work".format(input_))
else:
	print("The time is {}, I am at home".format(input_))

# A6 - Create two variables called num1 and num2.
# Create an if statement that checks if the result of the
# sum is even. If it is, return a success message.

num1 = int(input("number 1: "))
num2 = int(input("number 2: "))

if((num1 + num2) % 2 == 0):
	print("this is a success message")

# A7 - Create a variable called num.
# Check if the number is a palindrome (looks the same
# forward as it does backwards e.g. 1001 or 20202).

input_ = input("gimme a number: ")
reverse = input_[::-1]

if(input_ == reverse):
	print("{} is a plaindrome".format(input_))