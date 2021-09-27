import random as r

# print("hello world")

# print(len("hello world"))

# print("hello".upper())

# print(r.random())

# print(r.uniform(1,10))

# print(r.randint(1,2))

space = ' '
bar =  '|'
equ = '='

road = space + bar + space + bar + space

for i in range(1, 11):
	for i in range(1, 4):
		print(space, bar, space, bar, space)
	print(equ*9)
for i in range(1, 4):
		print(space, bar, space, bar, space)



# OR


space = '  '
bar =  '|'
equ = '='

road = space + bar + space + bar + space

for i in range(1, 11):
	for i in range(1, 4):
		print(road)
	print(equ*8)
for i in range(1, 4):
		print(road)


# OR, as a function

def roadprinter(length =  10):
	space = '  '
	bar =  '|'
	equ = '='

	road = space + bar + space + bar + space

	for i in range(1, length):
		for i in range(1, 4):
			print(road)
		print(equ*8)
	for i in range(1, 4):
			print(road)