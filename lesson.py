secret = 22
guess = 0
while guess != secret:
     guess = int(input("guess number between 1-100: "))

     if secret == guess:
       print ("your guess is right")
     else:
       print ("you are wrong")
print("progress end")


num1 = int(input("first number "))
num2 = int(input("second number "))
operation = input(('pick from - add/sub/mul/div'))

if operation == "add":
    print((num1 +num2))
elif operation == "sub":
    print((num1 - num2))
elif operation == "mul":
    print((num1 * num2))
elif operation == "div":
    print((num1 / num2))










