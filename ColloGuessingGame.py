player1 = 1
total = 0
# the list below will store all the values of player 1
player1guesses = []
total_list = []
# The player that chooses a number that will add up to the numbers below will win
mylist = [12, 23, 34, 45, 56, 67, 78, 89]
for item in mylist:
    print(f'\n\nPlayer 1 guessed {player1}')
    player2 = int(input('Player 2 guess : '))
    if 0 < player2 < 10:
        total1 = player1 + player2
        total = total1
        print(f'The sum of the two guesses is {total}')
        total_list.append(total)
        total_list_sum = sum(total_list)
        print(f'The total list : {total_list}')
        player1 = item - total_list_sum
        player1 = player1
        player1guesses.append(player1)
        print(f'The list of player 1 guesses {player1guesses}')
        print(f'Player 1 next guess is {player1}')
    else:
        exit()
