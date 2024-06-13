import time
class GuessGame():
    def game(answer, test=False):
        # default values
        GuessGame.steps = 0
        GuessGame.guess = 1
        GuessGame.record = 0
        GuessGame.default_high = 10
        GuessGame.low = 1
        GuessGame.high = GuessGame.default_high
        while True:  # game loop breaks when the answer is correct
            # if the answer isnt correct but still within the search range
            if answer != GuessGame.guess and GuessGame.high >= answer:
                # guess = halfway point in range
                GuessGame.guess = GuessGame.low + (GuessGame.high - GuessGame.low) // 2
                if answer > GuessGame.guess:  # if answer is greater than guess, increase low by 1
                    GuessGame.low = GuessGame.guess + 1
                elif answer < GuessGame.guess:  # if answer is less than guess, decrease high by 1
                    GuessGame.high = GuessGame.guess - 1
                GuessGame.steps += 1  # steps keeps track of how many guesses the comp takes
                print(f'guess: {GuessGame.guess}')  # print guess
            # if answer is greater than high & != to guess, increase search range by increasing high
            elif GuessGame.high < answer and answer != GuessGame.guess:
                GuessGame.low *= 2
                GuessGame.high *= 2
                print('Expanding search range')
            # if answer == guess, print guess and steps it took to get there
            else:
                if GuessGame.record < GuessGame.steps:
                    GuessGame.record = GuessGame.steps
                print(f'I guess {GuessGame.guess}! It took me '
                f'{GuessGame.steps} guesses to get it correct!')
                if test: # if testing mode is requested
                    answer += 1  # go to next number to attempt guessing
                    print(f'Increasing answer by 1 to test next number. Next test is for {answer}. '
                          f'Most guesses needed: {GuessGame.record}')
                    # time.sleep(0.1)
                    GuessGame.low = 1  # reset default values
                    GuessGame.high = GuessGame.default_high
                    GuessGame.steps = 0  # reset guess attempts for next session
                    continue
                else:  # if testing mode is not requested, stop the loop
                    break

GuessGame.game(int(input(f'Give me a number to guess: ')), True)
time.sleep(60)