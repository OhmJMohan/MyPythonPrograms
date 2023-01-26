z=input("Enter your good name.")
print("Welcome {0}, for our python calculator".format(z))
while True:
	x=int(input("Enter your first number"))
	y=int(input("Enter your second number"))
	print("Addition for plus sign")
	print("Subract for Minus sign")
	print("Multiply for star sign")
	print("Divide for slash sign")
	w=input("Enter the symbol to do with two numbers, add, subract, multiply, or divede.")
	a=x+y
	b=x-y
	c=x*y
	d=x/y
	if w=="+":
		print("Your answer is: ",a)
	elif w=="-":
		print("Your answer is: ",b)
	elif w=="*":
		print("Your answer is: ",c)
	elif w=="/":
		print("Your answer is: ",d)
	else:
		print("no value")
	tex=input("Do you want to continue for calculating? Type Y or N")
	if tex=="n":
		break
	else:
		print("thank you")

print("Welcome {0}, see you again.".format(z))
end=input("Press enter to continue")
 

