import datetime

now = datetime.datetime.now()
print(now)
x = now.strftime("%H")
t = int(x)
if t < 12:
	print("Hello visiter, good morning!")
elif t < 16:
	print("Hello visiter, good afternoon!")
elif t <= 24:
	print("Hello visiter, good evening!")