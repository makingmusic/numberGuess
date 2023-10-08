# user makes a guess.
# computer searches for that number in the provided range using a simple binary search
# shares number of attempts and expected number of attempts (log2(n))

import random
import math

# Step 1: Ask the users' name and any other basic info (e.g. min and max range etc.)
print("minRange ?")
minGuess = int(input())
saveMinGuess = int(minGuess)
print("maxRange ?")
maxGuess = int(input())
saveMaxGuess = int(maxGuess)

print("Pick a Number ")
secretNumber = int(input())

hasComputerGuessedCorrectly = False
numberofAttempts = 0

while not hasComputerGuessedCorrectly:
      computerGuess = round((minGuess + maxGuess) / 2)
      numberofAttempts = numberofAttempts + 1
      print("Searching in  [", minGuess, "..", maxGuess, "]")
      if secretNumber < computerGuess:
            maxGuess = computerGuess
      if secretNumber > computerGuess:
            minGuess = computerGuess
      if computerGuess == secretNumber:
            hasComputerGuessedCorrectly = True
            break
# end of while loop
x = (saveMaxGuess - saveMinGuess + 1)
logx = round(math.log(x, 2), 2)
print("Found in ", numberofAttempts, " attempts. Expected: log_2(", x, ") = ", logx)
