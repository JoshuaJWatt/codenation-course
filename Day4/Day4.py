# A1 - Here's an example of a function that includes a parameter.
# Parameters are responsible for functions being able to work on
# different data inputs. Edit the snippet below to include two or
# more parameters and a running order count updated when the
# function is called:

# order_count = 0

# def take_order(*toppings):
# 	global order_count
# 	print("Pizza with {}, {} and, {}".format(*toppings))
# 	order_count += 1
# 	print(order_count)
# 	return

# take_order("pineapple", "cheese", "more cheese")

# A2 - Cash machine time. Let’s create one that :
# Takes an input of pin number and amount
# Prints dispensing cash if the pin number is correct and there’s
# enough money to withdraw
# Displays the new bank balance

# gPin = 0000
# gAmnt = 578

# def cashMachine():
# 	global gPin
# 	global gAmnt
# 	pin = int(input("gib pin number: "))
# 	amnt = int(input("how much?: "))
# 	if pin != gPin or amnt > gAmnt:
# 		print("no.")
# 	else:
# 		gAmnt -= amnt
# 		print("k. your new balance is: {}".format(gAmnt))
# 	return()

# cashMachine();

# Make a function that outputs the product of several numbers

# def prod(*args):
# 	out = 1
# 	for i in args:
# 		out = out * i
# 	return(out)

# print(prod(1,2,3,4))

# Make a list of your top 3 favourite songs and print it

# top3 = ["Nemo - Nightwish", "Just Like Heaven - The Cure", "Camel Cigarette - Beggar"]

# top3.append("Lip Up Fatty - Bad Manners")

# print(top3)


# A1 - Create a list of your favourite website (3 of them), and
# then add another two once you’ve created the list.
# Then remove the last website.

# sites = ["JoshuaWatt.com", "github.com/JoshuaJWatt", "w3schools.com/python"]
# sites.extend(["dotabuff.com/players/98475971", "docs.python.org"])
# sites.pop()

# print(sites)

# Bonus - longest alternating substring
# Given a string of digits, return the longest substring with alternating
# odd/even or even/odd digits. If two or more substrings have the same 
# length, return the substring that occurs first.

def longestSubstring(string_):
	substrings = []
	currentsubstring = []
	previ = None # We make this a bool, where 1 is odd, 0 is even.
	for i in string_:
		# The case in which we don't alternate:
		if int(i) % 2 == previ:
			# currentsubstring.append(i)
			substrings.append(currentsubstring)
			currentsubstring = [i]
			previ = int(i) % 2
		# The case in which they do alternate
		elif int(i) % 2 != previ:
			currentsubstring.append(i)
			previ = int(i) % 2
	if len(substrings) == 0:
		return("There are no alternating substrings")#
	else:
		lenlist = []
		for i in substrings:
			lenlist.append(len(i))
		longestlen = max(lenlist)
		# if lenlist.count(longestlen)== 1:
		# 	return max(substrings)
		# else:
		outindex = lenlist.index(longestlen)
		# Turning our list back into a string
		outlist = substrings[outindex]
		out = "".join(outlist)
		return(out)

in_ = input("Gimme a string of numbers: ")
print("The first, longest alternating substring is: ", longestSubstring(in_))

