import time
class BinarySearch():
    def game(answer, test=False):
        # default values
        BinarySearch.steps = 0
        BinarySearch.guess = 1
        BinarySearch.record = 0
        BinarySearch.default_high = 10
        BinarySearch.low = 1
        BinarySearch.high = BinarySearch.default_high
        while True:  # game loop breaks when the answer is correct
            # if the answer isnt correct but still within the search range
            if answer != BinarySearch.guess and BinarySearch.high >= answer:
                # guess = halfway point in range
                BinarySearch.guess = BinarySearch.low + (BinarySearch.high - BinarySearch.low) // 2
                if answer > BinarySearch.guess:  # if answer is greater than guess, increase low by 1
                    BinarySearch.low = BinarySearch.guess + 1
                elif answer < BinarySearch.guess:  # if answer is less than guess, decrease high by 1
                    BinarySearch.high = BinarySearch.guess - 1
                BinarySearch.steps += 1  # steps keeps track of how many guesses the comp takes
                print(f'guess: {BinarySearch.guess}')  # print guess
            # if answer is greater than high & != to guess, increase search range by increasing high
            elif BinarySearch.high < answer and answer != BinarySearch.guess:
                BinarySearch.low *= 2
                BinarySearch.high *= 2
                print('Expanding search range')
            # if answer == guess, print guess and steps it took to get there
            else:
                if BinarySearch.record < BinarySearch.steps:
                    BinarySearch.record = BinarySearch.steps
                print(f'I guess {BinarySearch.guess}! It took me '
                f'{BinarySearch.steps} guesses to get it correct!')
                if test: # if testing mode is requested
                    answer += 1  # go to next number to attempt guessing
                    print(f'Increasing answer by 1 to test next number. Next test is for {answer}. '
                          f'Most guesses needed: {BinarySearch.record}')
                    # time.sleep(0.1)
                    BinarySearch.low = 1  # reset default values
                    BinarySearch.high = BinarySearch.default_high
                    BinarySearch.steps = 0  # reset guess attempts for next session
                    continue
                else:  # if testing mode is not requested, stop the loop
                    break

BinarySearch.game(int(input(f'Give me a number to guess: ')), False)  # True to turn on testing mode
time.sleep(60)