import random
print("Welcome to HiLo, the game where you guess a random number , and we tell you if you got it too high or too low.")
print("There are 3 levels, having increasing difficulty. If you get them all right, you will have a bonus level where you will have 1 guess to get the right winning number.")
print("This is level 1. Follow the instructions carefully, and use only numbers during the entire program")
print("Pick a number, and remember, for each wrong answer the winning number goes down by 1, and you lose if the winning number equals 0.")
def printN(n):
	S=int(input())
	if n==1 and S!=1:
		print("Sorry, you lose. The winning number was 1. Better luck next time.")
		exit()
	if S>10:
		print("You put in too big of a number to play. Put in another number.")
		printN(n)
	if S<0:
		print("You put in too small of a number to play. Put in another number.")
		printN(n)
	if S<n:
		print("Your guess was too low, try again")
		printN(n-1)
	if S>n:
		print("Your guess was too high, try again")
		printN(n-1)
	if S==n:
		print("Your guess was correct! Congratulations!!!")
		return
printN(random.randint(1,10))
print("Do you want to play again on a harder level? Type 1 for yes or 2 for no to answer.")
def choose(C):
	Y=1
	N=2
	if (C != Y and C != N):
		print("You put in a character that can not choose to play the game's next level.")
		print("Do you want to play again on a harder level? Type 1 for yes or 2 for no to answer.")
		choose(int(input()))
	if C==Y:
		print("This level is the same as the last level, except instead of choosing from numbers between 1 and 10,") 
		print("you will choose between the numbers 1 and 100. You lose if the winning number becomes 0 or less than 0.")
		print("Pick a number, and remember, each wrong answer lowers the winning number by 3")
		def printM(m):
			B=int(input())
			if m==1 and B!=1:
				print("Sorry, you lose. The winning number was 1. Better luck next time.")
				exit()
			if B>100:
				print("You put in too big of a number to play. Put in another number.")
				printM(m)
			if B<0:
				print("You put in too small of a number to play. Put in another number.")
				printM(m)
			if B<m:
				print("Your guess was too low, try again")
				printM(m-3)
			if B>m:
				print("Your guess was too high, try again")
				printM(m-3)
			if B==m:
				print("Your guess was correct! Congratulations!!!")
				return	
	if C==N:
		print("Oh well, we hope you enjoyed this game. Play again soon.")
		exit()
	if C == Y:
		printM(random.randint(1,100))
choose(int(input()))
print("Do you want to play the last level? Type 1 for yes or 2 for no to answer.")
def chooseAgain(V):
	Y=1
	N=2
	if (V != Y and V != N):
		print("You put in a number that can not choose to play the game's next level.")
		print("Do you want to play again on a harder level? Type 1 for yes or 2 for no to answer.")
		chooseAgain(int(input()))
	if V==Y:
		print("This level is the same as the last level, except instead of choosing from numbers between 1 and 100,") 
		print("you will choose between the numbers 1 and 1000. You lose if the winning number becomes 0 or less than 0.")
		print("Pick a number, and remember, each wrong answer lowers the winning number by 25")
		def printX(x):
			C=int(input())
			if x==1 and C!=1:
				print("Sorry, you lose. The winning number was 1. Better luck next time.")
				exit()
			if C>1000:
				print("You put in too big of a number to play. Put in another number.")
				printX(x)
			if C<0:
				print("You put in too small of a number to play. Put in another number.")
				printX(x)
			if C==x:
				print("Your guess was correct! Congratulations!!! You won the entire game of HiLo!!!")
				return	
			if C<x:
				print("Your guess was too low, try again")
				printX(x-25)
			if C>x:
				print("Your guess was too high, try again")
				printX(x-25)
	if V==N:
		print("Oh well, we hope you enjoyed this game. Play again soon.")
		exit()
	if V == Y:
		printX(random.randint(1,1000))
chooseAgain(int(input()))
print("Do you want to play the Bonus Level? Type 1 for yes or 2 for no to answer.")
def chooseBonus(A):
	Y=1
	N=2
	if (A != Y and A != N):
		print("You put in a number that can not choose to play the game's next level.")
		print("Do you want to play again on a harder level? Type 1 for yes or 2 for no to answer.")
		chooseAgain(int(input()))
	if A==Y:
		print("This level is the same as the last level, except instead of choosing from numbers between 1 and 100,") 
		print("you will choose between the numbers 1 and 100. You lose if you can not guess the right winning number in 1 try")
		print("Pick a number, and remember, if you guess wrong, the game is over and you lose.")
		def printO(O):
			H=int(input())
			if O != H:
				print("Sorry, you lose. The winning number was " + str(O) + ". Better luck next time.")
				exit()
			if H>100:
				print("You put in too big of a number to play. Put in another number.")
				printO(O)
			if H<0:
				print("You put in too small of a number to play. Put in another number.")
				printO(O)
			if H==O:
				print("Your guess was correct! Congratulations!!! You won the entire game of HiLo!!!")
				exit()	
	if A==N:
		print("Oh well, we hope you enjoyed this game. Play again soon.")
		exit()
	if A == Y:
		printO(random.randint(1,100))
chooseBonus(int(input()))
