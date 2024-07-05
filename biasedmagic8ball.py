"""Biased Magic 8 Ball - this Magic 8 Ball is cynical when it comes to love and only answers negatively in those cases."""

import random


pos_answers = ["It is certain.",
               "It is decidedly so.",
               "Without a doubt.",
               "Yes definitely.",
               "You may rely on it.",
               "As I see it, yes.",
               "Most likely.",
               "Outlook good.",
               "Yes.",
               "Signs point to yes."]

mid_answers = ["Reply hazy, try again.",
               "Ask again later.",
               "Better not tell you now.",
               "Cannot predict now.",
               "Concentrate and ask again."]

neg_answers = ["Don't count on it.",
               "My reply is no.",
               "My sources say no.",
               "Outlook not so good.",
               "Very doubtful."]


love_words = ["love",
              "boyfriend",
              "girlfriend",
              "partner",
              "like",
              "relationship",
              "romance",
              "couple",
              "soulmates",
              "marry",
              "spouse",
              "husband",
              "wife"]


def biased_magic_8_ball():
    while True:
        user_input = input("Hello! I am the (biased) Magic 8 Ball! "
                           "Do you have a question for me?"
                           " Please enter Y or N: ")
        if user_input.upper() == "Y":
            user_question = input(
                "Ask me your question and I will tell you your fortune: ")
            if user_question in love_words:
                love_answers = mid_answers + neg_answers
                print(love_answers[random.randint(0, len(love_answers)-1)])
                break
            else:
                all_answers = pos_answers + mid_answers + neg_answers
                print(all_answers[random.randint(0, len(all_answers)-1)])
                break
        elif user_input.upper() == "N":
            print("Until next time, dear stranger.")
            break
        else:
            print("Please enter a valid input.")


biased_magic_8_ball()
