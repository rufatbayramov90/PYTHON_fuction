import random
word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
display = []
for letter in chosen_word:
    display += "_"
print(display)

guess = input("Guess a letter").lower()

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")