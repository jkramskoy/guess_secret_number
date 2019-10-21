import random
import json
import datetime


# Play the game
def play_game(level):
    secret_num = random.randint(1, 30)
    attempts = 0
    wrong_guesses = []
    name = input("please enter your name: ")

    while True:
        user_input = int(input("Guess the secret number(between1 and 30)"))
        attempts += 1
        print(level)
        if user_input == secret_num :
            print("you did a great job.It's number{0}".format(str(secret_num)))
            print("attempts needed:{0}".format(str(attempts)))
            cur_attempt = {"attempts": attempts, "date": str(datetime.datetime.now()), "name": name,
                           "wrong_guesses": wrong_guesses}
            print(str(cur_attempt["attempts"]) + " attempts, date: " + cur_attempt.get("date"))

            score_list.append(cur_attempt)
            with open("guessing-save.txt", "w") as score_file:
                score_file.write(json.dumps(score_list))
            break
        elif level == "easy" and user_input > secret_num:
            wrong_guesses.append(user_input)
            print("try smaller")
        elif level == "easy" and user_input < secret_num:
            wrong_guesses.append(user_input)
            print("try bigger")
        else:
            wrong_guesses.append(user_input)
            print("wrong number")
            
# Get a list of all scores
def get_score_list () :
 with open("guessing-save.txt","r") as score_file:
    score_list = json.loads(score_file.read())
    return score_list


# sort the list of dicts per attempts.Get top 3 scores
def get_top_scores(score_list):
 return sorted(score_list, key=lambda k: k['attempts'])[:3]
score_list = get_score_list()
score_list = get_top_scores(score_list)
print("top score: {0}".format(str(score_list)))

#run the game:

while True:
    selection = input("Would you like to A) play a new game, B) see the best scores, or C) quit?")

    if selection == "A":
        level = input("Please choose your level (easy/hard): ")
        play_game(level)
    elif selection == "B":
        for score_dict in get_top_scores(score_list):
            print(str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("date"))
    else:
        break










