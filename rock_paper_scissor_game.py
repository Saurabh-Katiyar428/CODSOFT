import random
# Choice function is displaying the choice of user and computer
def _choice(a):
   if(a=="r"):
      print("Your choice","rock")
      return "rock"
   elif(a=="p"):
      print("Your choice","paper")
      return "paper"
   elif(a=="s"):
      print("Your choice","scissors")
      return "scissors"
# Main function controlling actions
def function():
   choices=["rock","paper","scissors"]
   global sfu,sfc # Refrencing to global variables
   while True:
      x=input("Hi user enter your choice R->rock P->paper S->scissors:").lower()
      if x in ["r","p","s"]:# x means choice of user
         break
      print("Invalid input. Please try again!")
   y=random.choice(choices)
   user_choice=_choice(x)
   print("Computers choice:",y)
   if ((user_choice=="rock" and y=="scissors") or (user_choice=="scissors" and y=="paper") or (user_choice=="paper" and y=="rock")):
      sfu=sfu+1
      print("(((((......Congratulation you Won.......)))))")
   elif ((y=="rock" and user_choice=="scissors") or (y=="scissors" and user_choice=="paper") or (y=="paper" and user_choice=="rock")):
      sfc=sfc+1
      print("(((((......Oops you lost.......)))))")
   elif (user_choice==y):
      print("(((((.....Match tied.....)))))")
   print("Current scores->", "You:",sfu," Computer Score:",sfc)
def game():
   print("Welcome to rock/paper/scisssors/game...")
   function()
   while True:
      print("Press 1->To play again:")
      print("Press 2->To exit from the game:")
      ch=int(input('Enter your choice:'))
      if(ch==1):
         function()
      elif(ch==2):
         print("------Thank you---------")
         print("Final scores->", "You:",sfu," Computer Score:",sfc)
         break
      else:
         print("Invalid input!Please try again")
sfu=0 # sfu means score for user
sfc=0 # sfc means score for computer
game() # calling game