from random import randint

computer = randint(1,100)

while True:
  try:
      guess = int(input("Guess a number between 1 to 100  : "))
    
      if guess > computer :
         print(f"{guess} is high")
      elif guess < computer : 
         print(f"{guess} is low")
      else:
         print("Congrajulations,You guessed the correct number")  
         break
        
  except ValueError:
         print("Enter a valid number")
         
         
        



