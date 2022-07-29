
#!/bin/bash

#importing random for generating random number
import random
comp_guess=random.randint(1,100)


times_you_had_did=0
#Using try except to not getting error
try:
    print("guess number between 1 to 100")
	while True:
		times_you_had_did=times_you_had_did+1
		guess=int(input("Enter your guessing number\n>>> "))
		print(".................")
		if(guess==comp_guess):
			print("Congratulations you guessed right number!")
			break
		if(guess>comp_guess):
			print("guess lower number")
			continue
		if(guess<comp_guess):
			print("guess higher number")
			continue

except:
	print("..................")
	print("error")
	print("you have done something wrong")
	exit()

f=open("highscore.txt")
highscore=int(f.read())
f.close()


if(times_you_had_did<highscore):
	f=open("highscore.txt", "w")
	f.write(str(times_you_had_did))
	f.close()
