# chatbot steps
"""
steps:
1.take input / listen
2.process / decide
3.output / talk back

"""

greet_words = ["hi", "hey", "hlw", "hello", "assalamu", " alaikum", "yo"]
bye_words = ["bye", "tata", "see you", "by"]


def listen():
    return input("say something....:")


def decide(command):
    print("decide", command)
    broken_word = command.split(" ")
    print(broken_word)


def talkBack():
    pass


command = listen()
decide(command)
