def greetingQuestion():
    name = input("What's your name?")
    print("Nice to meet you " + name + "!")
    questionR = input("What do you want to learn?")
    print("Well, " + name + "we will try to figure out the answer together!")


def checkQuestion(arg):
    if input [-1] != "?":
        print(“I’m sorry, I can only answer questions.”)

def answerQuestion():
    possibleAnswers = ['It is certain',
                       'It is decidedly so',
                       'Without a doubt',
                       'Yes definitely',
                       'You may rely on it',
                       'As I see it, yes',
                       'Most likely',
                       'Outlook good',
                       'Yes',
                       'Signs point to yes',
                       'Reply hazy try again',
                       'Ask again later',
                       'Better not tell you now',
                       'Cannot predict now',
                       'Concentrate and ask again',
                       'Don\'t count on it',
                       'My reply is no',
                       'My sources say no',
                       'Outlook not so good',
                       'Very doubtful']
    print(random.choice(possibleAnswers))
