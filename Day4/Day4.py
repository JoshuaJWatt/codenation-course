# A1 - Here's an example of a function that includes a parameter.
# Parameters are responsible for functions being able to work on
# different data inputs. Edit the snippet below to include two or
# more parameters and a running order count updated when the
# function is called:

order_count = 0

def take_order(*toppings):
	global order_count
	print("Pizza with {}, {} and, {}".format(*toppings))
	order_count += 1
	print(order_count)
	return

take_order("pineapple", "cheese", "more cheese")

# A2 - Cash machine time. Let’s create one that :
# Takes an input of pin number and amount
# Prints dispensing cash if the pin number is correct and there’s
# enough money to withdraw
# Displays the new bank balance

gPin = 0000
gAmnt = 578

def cashMachine():
	global gPin
	global gAmnt
	pin = int(input("gib pin number: "))
	amnt = int(input("how much?: "))
	if pin != gPin or amnt > gAmnt:
		print("no.")
	else:
		gAmnt -= amnt
		print("k. your new balance is: {}".format(gAmnt))
	return()

cashMachine();