import time
from spellchecker import SpellChecker

spell = SpellChecker()
userInput = input("Type the text here: \n")
startTime = time.time()
if userInput == "":
    print(f"The text you entered: {userInput}")

measuredTime = time.time() - startTime

wordList = userInput.split()
misspelledWords = len(list(spell.unknown(wordList)))
print(f"The number of your misspelled words is:  {misspelledWords}")

print(f"The time it took you to type the text is: {measuredTime}")


