#varible with your secret number
#user input for their number
#if secret number == user input print congrads
#else print wrong number


var_secret = "8"

while (True):
    var_guess = input("Please tell us your number")

    if var_secret == var_guess:
        print("congratulation, it is number 8")
    else:
        print("Sorry, but number is wrong")
