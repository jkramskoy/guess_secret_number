import random
import json
import datetime


score_list = []
secret_num = random.randint (1,30)
attempts = 0

with open("save.txt","r") as score_file:
    score_list = json.loads(score_file.read())
    print("top score: {0}".format(str(score_list)))

name = input("please enter your name: ")


while True:
    user_input = int (input ("Guess the secret number(between1 and 30)"))
    attempts += 1

    if user_input == secret_num:
        print("you did a great job.It's number{0}".format(str(secret_num)))
        print("attempts needed:{0}".format(str(attempts)))
        cur_attempt = {"attempts":attempts, "date":str (datetime.datetime.now()), "name": name}
        print(str(cur_attempt["attempts"]) + " attempts, date: " + cur_attempt.get("date"))

        score_list.append(cur_attempt)
        with open("save.txt","w") as score_file:
              score_file.write(json.dumps(score_list))


        break
    elif user_input > secret_num:
        print("try smaller")
    elif user_input < secret_num:
        print("try bigger")



