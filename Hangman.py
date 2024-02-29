from random import choice


endGame = False

lives = 6

word_list = ["ardvark", "baboon", "camel"]

chosen_word = choice(word_list)

blank = list("_" * len(chosen_word))

while( not endGame):
    Guess = input("Guess a letter: ").lower()
    
    if Guess in blank:
        print(f'You\'ve guessed {Guess} earlier.')

    for i in range(len(chosen_word)):
        if Guess == chosen_word[i]:
            blank[i] = Guess
    print(blank)
    if '_' not in blank:
        endGame = True
        print('You win.')

    elif Guess not in chosen_word:
        lives -= 1
        print(f'\nWrong. {Guess} is not a character in the word\n')
        print(f'You have {lives} lives left')
        print(blank)

        if lives == 0:
            endGame = True
            print('You lose. Game Over!')
