
print("Hello,this is a  a program that converts units. More specifically, kilometers into miles.")

while (True):
  number_of_kilometers = float(input("Please enter number of kilometers to convert it to miles"))
  miles = number_of_kilometers * 0.621371
  print("It will be", miles, "miles")
  question = input("Do you want to do another conversion?Please use Y or N for your answer")
  if question == "Y":
      continue
  elif question == "N":
      print("Goodbye")
      break
  else:
      print("Wrong selection")





















