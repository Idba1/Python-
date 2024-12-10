# chatbot steps
"""
steps:
1.take input / listen
2.process / decide
3.output / talk back

"""

greet_words = ["hi", "hey", "hlw", "hello", "assalamu", " alaikum", "yo"]
bye_words = ["bye", "tata", "see you", "by"]
bad_words = ["dog", "pocha"]


def listen():
    return input("say something....:")


def decide(command):
    command = command.lower()
    print("decide", command)
    broken_word = command.split(" ")
    print(broken_word)

    for word in broken_word:
        if word in greet_words:
            talkBack("Hi Human!")

        elif word in bye_words:
            talkBack("Tata Human!")

        elif word in bad_words:
            talkBack("You are a bad Human. Behave yourself!")


def talkBack(response):
    print(response)


while True:
    command = listen()
    decide(command)
