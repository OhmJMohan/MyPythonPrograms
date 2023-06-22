print("hello user!, welcome to the new hand cricket game ")


import random 

over=int(input("how many over you want to play"))
ball=over*6
if ball> 6:
	print("dear playeryou have only 6 overs so please enter number till 6") 
run=0
count=0
while count<ball:
	try:
		r=random.randint(1, 6)
		user=int(input("enter the run"))
		count=count+1
		if user>6:
			count=count-1
			run=run-user
			print("முறையாக விலையாட வேண்டும்")
		elif user<0:
			count=count-1
			run=run-user
			print("dont play like this")
		elif user==r:
			print("you are gone, your total score is %d after %d overs%d balls" % (run,count//6,count%6))
			break
		elif ball==count:
			print(" your total score is %d after %d overs%d balls" % (run,count//6,count%6))
			break
		print(r)
		run=run+user
	except ValueError:
		print("plese enter number only")
import time
time.sleep(5)