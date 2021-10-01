import random as r;
import datetime as t;

#A1
names = ['James', 'Robert', 'John', 'Michael', 'William', 'David', 'Richard', 'Joseph'];
ages = range(19, 99);
colours = ['red', 'green', 'blue', 'indigo', 'violet'];

print("{} is {}, and their favourite colour is {}".format(names[r.randint(0, len(names)-1)], ages[r.randint(0,len(ages)-1)], colours[r.randint(0,len(colours)-1)]));


#A2
foods = ['cereal', 'sandwich', 'toast', 'salad', 'chips', 'curry', 'shawarma'];
br = r.choice(foods); di = r.choice(foods); te = r.choice(foods);
print("For breakfast I will eat {}, for dinner I will eat {}, and for tea I will eat {}".format(br, di, te));
br = r.choice(foods); di = r.choice(foods); te = r.choice(foods);
print("Tomorrow, for breakfast I will eat {}, for dinner I will eat {}, and for tea I will eat {}".format(br, di, te));


#A3
spaces = ['x', 'o', ' ','x','x',' ','o',' ',' ']

for i in range(0,11):
	if i % 2 == 1: print(" | | ")
	elif i % 4 == 0: print("-----")
	else:
		if i == 2: print("{}|{}|{}".format(spaces[0], spaces[1], spaces[2]))
		if i == 6: print("{}|{}|{}".format(spaces[3], spaces[4], spaces[5]))
		if i == 10: print("{}|{}|{}".format(spaces[6], spaces[7], spaces[8]))

#A5
birthday = t.datetime(1995, 9, 17)
today = t.datetime.now()

print(today-birthday)
