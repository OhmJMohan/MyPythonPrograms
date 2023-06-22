print("Welcome to check the number if odd or even")
num=int(input("Enter the number: "))
x = num % 2
if x == 0:
	print("Number {0}, is even number.".format (num)) 
else:
	print("Number {0}, is odd number.".format (num)) 

print("Thank you")