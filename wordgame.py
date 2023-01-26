import time
import random
print("Welcome to the intresting word game.")
name=input("Enter your name: ")
a = name[0]
print("To start the game, first type a word in the initial letter of your name")
print("The second time, you have to type the word that a character suggests to you.")
print("Don't type space in word, then game will end.")
print("One word allowed only one time, Don’t type words repeatedly.")  
score = 0
lett_list = []
lett_list1 = []
time.sleep(3)
num=int(input("How many words you want to play? Enter the number here: "))
i = 0
while i < num:
    lett=input("Enter the word: ")
    if lett[0] == a and " " not in lett and lett not in lett_list1:
        x=random.randint(0, len(lett)-1)
        print("Your word is: " + lett + ", and your suggest letter is: " , lett[x])
        a = lett[x]
        i += 1
        score = score + len(lett)
        lett_list.append(lett + ", suggest letter is: " + lett[x]+"\n")
        lett_list1.append(lett)
    else:
        break

print("thank you " + name + ", you are welcome.")
print("Your score is: ", score)
f = open("game.txt", "w")
f.write("Hello " + name + ", your scor is: %d.\n" %(score))
f.write("Your words are listed below:\n")
for i in lett_list:
    f.write(i)
f.close()
print("Wow!, your word details are saved in file called game.txt")
time.sleep(8)

