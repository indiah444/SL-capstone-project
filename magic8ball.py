"""Standard Magic 8 Ball - ask a yes or no question it will give you an random answer."""

import random


answers = ["It is certain.",
           "It is decidedly so.",
           "Without a doubt.",
           "Yes definitely.",
           "You may rely on it.",
           "As I see it, yes.",
           "Most likely.",
           "Outlook good.",
           "Yes.",
           "Signs point to yes.",
           "Reply hazy, try again.",
           "Ask again later.",
           "Better not tell you now.",
           "Cannot predict now.",
           "Concentrate and ask again.",
           "Don't count on it.",
           "My reply is no.",
           "My sources say no.",
           "Outlook not so good.",
           "Very doubtful."]


def magic_8_ball():
    while True:
        user_input = input("Hello! I am the Magic 8 Ball! "
                           "Do you have a question for me?"
                           " Please enter Y or N: ")
        if user_input.upper() == "Y":
            input("Ask me your question and I will tell you your fortune: ")
            print(answers[random.randint(0, len(answers)-1)])
            break
        elif user_input.upper() == "N":
            print("Until next time, dear stranger.")
            break
        else:
            print("Please enter a valid input.")


magic_8_ball()
