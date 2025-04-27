# adjectiv1 = input("Write an adjective: ")


def adjectiv_input():
    adjectiv = input("Write an adjective: ")
    return adjectiv


def noun_input():
    noun = input("Write a noun: ")
    return noun


def verb_input():
    verb = input("Write a verb, finish with ing: ")
    return verb


adjectiv1 = adjectiv_input()
adjectiv2 = adjectiv_input()
noun1 = noun_input()
verb1 = verb_input()
noun2 = noun_input()
adjectiv3 = adjectiv_input()
verb2 = verb_input()
verb3 = verb_input()
verb4 = verb_input()

print(f"I was walking in a {adjectiv1} forest.")
print(f"I was drinking a very {adjectiv2} {noun1}.")
print(f"After my drink was finished i started {verb1}.")
print(f"Right then I saw a {noun2}.")
print(f"The {noun2} was very {adjectiv3} and started {verb2}.")
print(f"That made me feel like {verb3}.")
print(f"So naturally the {noun2} started {verb4}.")
