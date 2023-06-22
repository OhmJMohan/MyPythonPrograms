list=["apple \n", "like \n", "king \n", "love \n"]
f = open("d:\Mohan.txt", "w")
f.write("Your words are:\n")
for x in list:
	f.write(x)
f.close()

