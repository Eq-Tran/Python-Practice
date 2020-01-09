#Rock-Paper-Scissors
# Ethan Tran 11/11/19

game = True

while game == True:

    p1 = input("Player 1 Choose Rock, Paper, or Scissors")
    p2 = input("Player 2 Choose Rock, Paper, or Scissors")

    if p1 == 'Rock' and p2 == 'Scissors':
        print('P1 Wins')
    elif p1== 'Scissors' and p2 == 'Rock':
        print('p2 wins')
    if p1 =='Scissors' and p2 == 'Paper':
        print('p1 wins')
    elif p1 == 'Paper' and p2 == 'Paper':
        print('p2 wins')
    if p1 == 'Paper' and p2 == 'Rock':
        print('p1 wins')
    elif p1 == 'Rock' and p2 == 'Paper':
        print('p2 wins')
    if p1 == p2:
        print('Tie')
        game = True
    choice = input('keep playing?')
    if choice == 'Y'.lower():
        game = True
    else:
        game = False
