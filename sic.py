z=input("Enter your good name.")
print("Welcome {0}, for our python simple intrest calculator".format(z))
while True:
	x=int(input("Enter the principle amount: "))
	y=int(input("Enter the number of months: "))
	w=float(input("Enter the rate of interest: ")) 
	v=x*y*w/100 
	print("Your one month interest:", x*1*w/100)
	print("Total interest amount for total months: ", v)
	print("Total amount that you get from party with principle: ", v+x)
	tex=input("Do you want to continue for calculating? Type Y or N")
	if tex=="n":
		break
	else:
		print("thank you")

print("Welcome {0}, see you again.".format(z))
end=input("Press enter to continue")
 

