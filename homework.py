happy_mood = "It is great to see you happy!"
nervous_mood = "Take a deep breath 3 times."
sad_mood = "Sorry to hear that."
excited_mood = "That sound AMAZING."
relaxed_mood = "Mellow out bro!"
error = "Soory I don't recognise your mood"

while (True):
    user_mood = input("please tell me your mood. (Option:happy,nervous,sad,exited,relaxed)")

    if user_mood == "happy":
        print(happy_mood)
    elif user_mood == "sad":
        print(sad_mood)
    elif user_mood == "nervous":
        print(nervous_mood)
    elif user_mood == "excited":
        print(excited_mood)
    elif user_mood == "relaxed":
        print(relaxed_mood)
    else:
        print(error)


