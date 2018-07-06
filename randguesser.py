from random import *

def get_guess():
  guess=raw_input("Your guess: ")
  return int(guess)

def rand_num():
  num=randint(0,100)
  count=0
  print"Guess a number between 1 and 100: "
  guess=get_guess() 
  while guess!=num:
      if guess>100 or guess<0:
	 print "Error! Your guess is out of range."
         guess=get_guess() 
         count+=1
      elif guess>num:
	 print "Too high!"
         guess=get_guess()
         count+=1
      else: 
         print"Too low!" 
         guess=get_guess()
         count +=1
  
  print "You guessed it in {} guesses! The number was {}!".format(count, num) 

if __name__=="__main__":
   rand_num()

