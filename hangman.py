from typing import List
import random

print("H A N G M A N")


def show_menu():
    _choice = input('Type "play" to play the game, "exit" to quit:')
    while not (_choice == 'play' or _choice == 'exit'):
        _choice = input('Type "play" to play the game, "exit" to quit:')
    return _choice


choice = show_menu()
while choice != 'exit':
    print()

    lives = 8

    words: List[str] = ['python', 'java', 'kotlin', 'javascript']
    word = list(random.choice(words))
    letters = set(word)
    guess = ['-' for letter in word]
    typed_letters = set()

    while lives > 0:
        print("".join(guess))
        if guess == word:
            print('You survived!')
            break
        w = input('Input a letter:')
        if w in typed_letters:
            print('You already typed this letter\n')
            continue
        if len(w) != 1:
            print('You should print a single letter\n')
            continue
        if not (w.islower()):
            print('It is not an ASCII lowercase letter\n')
            continue
        typed_letters.add(w)
        if w in letters:
            for j in range(len(guess)):
                guess[j] = w if word[j] == w else guess[j]
        else:
            lives -= 1
            print('No such letter in the word')
        if lives > 0:
            print()
        else:
            print('You are hanged!')

    choice = show_menu()
