
var_secret = "8"

while (True):
    var_guess = input("Please tell us your number")

    if var_secret == var_guess:
        print("congratulation, it is number 8")
        break
    else:
        print("Sorry, but number is wrong")
