import random

while True:
   
   choice = input("Roll the dice? (y/n)")

   if choice.lower() == "y" :
      dice1 = random.randint(1,6)
      dice2 = random.randint(1,6)
      print(f"({dice1},{dice2})")
      
   elif choice.lower() == "n":
       print("Thank You")

       break
   
   else:
      print("Invalid Selection")

      
