import random

# Write 'Rock Paper Scissors' to the console
print('Rock Paper Scissors')

# Create list of three elements: rock, paper, scissors
elements = ['rock', 'paper', 'scissors']

# Initialize scores
player1_score = 0
player2_score = 0

# Create a function to handle player inputs and display results
def players():
    global player1_score, player2_score

    # Ask Player 1 for input and validate it
    while True:
        player1 = input('Player 1, choose rock, paper, or scissors: ').lower()
        if player1 in elements:
            break
        print('Invalid input. Please choose rock, paper, or scissors.')
    
    # Player 2's random choice
    player2 = random.choice(elements)
    print('Player 1 chose:', player1)
    print('Player 2 chose:', player2)

    # Compare choices and determine the winner
    if player1 == player2:
        print('It is a tie')
    elif (player1 == 'rock' and player2 == 'scissors') or \
         (player1 == 'scissors' and player2 == 'paper') or \
         (player1 == 'paper' and player2 == 'rock'):
        print('Player 1 wins this round!')
        player1_score += 1
    else:
        print('Player 2 wins this round!')
        player2_score += 1

    # Ask to play again
    play_again = input('Do you want to play again? (yes or no): ').lower()
    if play_again == 'yes':
        players()
    elif play_again == 'no':
        print('Game ended')
        print('Final score:')
        print('Player 1:', player1_score)
        print('Player 2:', player2_score)
    else:
        print('Invalid input. Exiting game.')
        print('Final score:')
        print('Player 1:', player1_score)
        print('Player 2:', player2_score)

# Start the game
def start():
    print('Game started')
    print('Rules: Rock beats scissors, scissors beats paper, paper beats rock')
    players()

# Call the function to start the game
start()