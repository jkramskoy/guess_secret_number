import random

secret = random.randint(1.10)
attempts = 0 #popitki
best_score = 0
with open("score.txt","r") as score_file:
  best_score = int(score_file.read())
  print("Current HighScore = {0}".format(best_score))

while True:
  guess = int(input("Please enter guess: \n"))
  attempts += 1  # attempts = attempts + 1
  if guess == secret:
    print("You got it!")
    if attempts < best_score:
      with open("score.txt","w") as score_file:
        score_file.write(str(attempts))
        break
  elif guess < secret:
    print("Guess higher")
  elif guess > secret:
    print("Guess lower")

print("Got it in {0} attempts".format(attempts))

