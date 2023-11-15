import random

words = {
    "pies": "dog",
    "kot": "cat",
    "krowa": "cow",
    "kura": "hen",
    "kaczka": "duck",
    "świnia": "pig",
    "koń": "horse",
    "owca": "sheep",
    "kurczak": "chicken",
    "kogut": "rooster"
}

correct = 0

#TODO: Make the asked words unique
#TODO2: rearrange the logic so it can be asked for both languages
for i in range(5):
    word = random.choice(list(words.keys()))
    translation = input("What is the translation of the word " + word + "? ")
    if translation == words[word]:
        print("Correct!")
        correct+=1
    else:
        print("Wrong! The correct translation is: " + words[word])

print("You answered correctly " + str(correct) + " out of 5 questions.")
print("Your score is: " + str(correct/5*100) + "%.")