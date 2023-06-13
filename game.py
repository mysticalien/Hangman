import random
print('H A N G M A N')
win = 0
lose = 0
flag = True
while flag:
    what_to_do = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
    if what_to_do not in ['play', 'results', 'exit']:
        continue
    elif what_to_do == 'play':
        words = ['python', 'java', 'swift', 'javascript']
        word = random.choice(words)
        start = '-' * (len(word))
        i = 8
        guessed_letters = set()
        while i > 0:
            if word == start:
                win += 1
                print('\n', f'You guessed the word {word}!', sep='')
                print('You survived!')
                break
            print('\n', start, sep='')
            answer = input('Input a letter: ')
            set_of_word = set(word)
            if len(answer) != 1 or type(answer) != str:
                print('Please, input a single letter.')
            elif not answer.isalpha() or not answer.islower():
                print('Please, enter a lowercase letter from the English alphabet.')
            elif answer in guessed_letters:
                print('You\'ve already guessed this letter.')
                continue
            elif answer in word:
                start_list = list(start)
                for index, letter in enumerate(word):
                    if letter == answer:
                      start_list[index] = answer
                start = ''.join(start_list)
            else:
                print('That letter doesn\'t appear in the word.')
                i -= 1
            guessed_letters.add(answer)
        if i == 0 and word != start:
            lose += 1
            print('/n', 'You lost!', sep='')
        continue
    elif what_to_do == 'results':
        print(f'You won: {win} times')
        print(f'You lost: {lose} times')
        continue
    elif what_to_do == 'exit':
        break