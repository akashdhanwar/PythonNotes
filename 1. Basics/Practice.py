results = []
def stringMaker(string):
    if(string.startswith(("How","Why","What"))):
        return "%s?" % string
    else:
        return "%s." % string

while True:
    inputData = input("Say something: ")
    if inputData == "/end":
        break
    else:
        results.append(stringMaker(inputData.capitalize()))
        continue

print(" ".join(results))

# OUTPUT
# Say something: hello how are you
# Say something: how is the weather
# Say something: /end
# Hello how are you. How is the weather?