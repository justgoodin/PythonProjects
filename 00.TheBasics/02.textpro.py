def sentence_maker(phrase):
    interrogatives = ("how", "what", "why")
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)


output = []

while True:
    userInput = input()
    if userInput == "end":
        break
    else:
        output.append(sentence_maker(userInput))

print("".join(output))
