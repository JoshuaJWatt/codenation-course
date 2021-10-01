
#dummy world
world = [[0,0,0,1,1],
		[0,0,0,0,1],
		[0,0,0,1,1],
		[0,1,0,1,1],
		[0,0,1,1,1]]

newcolumn = [0,1,1,1,1]

def showWorld(world):
	for i in world:
		print(i)

def worldLeft(world, newcolumn):
	for i in world:
		for j in range(len(i)):
			if j == 0:
				continue
			else:
				i[j-1] = i[j]
				if j == len(i)-1:
					i[j] = newcolumn[0]
					newcolumn.pop(0)
	return(world)

def worldRight(world, newcolumn):
	for i in world:
		for j in range(len(i)-1, -1, -1):
			if j == len(i):
				continue
			else:
				i[j] = i[j-1]
				if j == 0:
					i[j] = newcolumn[0]
					newcolumn.pop(0)
	return(world)

def worldUp(world, newcolumn):
	

world = worldRight(world, newcolumn)
showWorld(world)