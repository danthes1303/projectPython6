import random
import art
import words



chosen_word = random.choice(words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(art.logo)
print("Welcome to the HangManGame.")
# print(f'The solution is {chosen_word}.')


display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:


    guess = input("Try to guess a letter: ").lower()


    if guess in display:
        print(f"You've already guessed letter {guess}. Try something else.")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter


    if guess not in chosen_word:
        lives -= 1
        print(f"Your guess is wrong. Lives remaining {lives}")
        if lives == 0:
            end_of_game = True
            print(f"hidden word: {chosen_word}")
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")


    print(art.stages[lives])