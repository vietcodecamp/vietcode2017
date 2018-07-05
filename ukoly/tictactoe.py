import sys  # umoznuje napsat print bez dalsiho radku


def checkVictory(tictactoe):
    if (tictactoe[0][0] == tictactoe[0][1] == tictactoe[0][2] == "X") or (
        tictactoe[1][0] == tictactoe[1][1] == tictactoe[1][2] == "X") or (
        tictactoe[0][0] == tictactoe[1][0] == tictactoe[2][0] == "X") or (
        tictactoe[0][1] == tictactoe[1][1] == tictactoe[2][1] == "X") or (
        tictactoe[2][0] == tictactoe[2][1] == tictactoe[2][2] == "X") or (
        tictactoe[0][2] == tictactoe[1][2] == tictactoe[2][2] == "X") or (
        tictactoe[0][2] == tictactoe[1][1] == tictactoe[2][0] == "X") or (
        tictactoe[0][0] == tictactoe[1][1] == tictactoe[2][2] == "X"):
        print("VYHRAL X")
        sys.exit()
    if (tictactoe[0][0] == tictactoe[0][1] == tictactoe[0][2] == "O") or (
        tictactoe[1][0] == tictactoe[1][1] == tictactoe[1][2] == "O") or (
        tictactoe[2][0] == tictactoe[2][1] == tictactoe[2][2] == "O") or (
        tictactoe[0][0] == tictactoe[1][0] == tictactoe[2][0] == "O") or (
        tictactoe[0][1] == tictactoe[1][1] == tictactoe[2][1] == "O") or (
        tictactoe[0][2] == tictactoe[1][2] == tictactoe[2][2] == "O") or (
        tictactoe[0][0] == tictactoe[1][1] == tictactoe[2][2] == "O") or (
        tictactoe[0][2] == tictactoe[1][1] == tictactoe[2][0] == "O"):
        print("VYHRAL O")
        sys.exit()
    if (tictactoe[0][0] != " ") and (
        tictactoe[0][1] != " ") and (
        tictactoe[0][2] != " ") and (
        tictactoe[1][0] != " ") and (
        tictactoe[1][1] != " ") and (
        tictactoe[1][2] != " ") and (
        tictactoe[2][0] != " ") and (
        tictactoe[2][1] != " ") and (
        tictactoe[2][2] != " "):
        print("REMIZA")
        sys.exit()
    return False


def vykresliHru():
    global tictactoe  # abych k tomu mela pristup
    for radek in tictactoe:
        for sloupec in radek:
            sys.stdout.write(sloupec + " | ")
        print()


def nextTurn():
    global playerNext
    global tictactoe
    print('Hraje hrac ' + str(playerNext))
    x = int(input('Zadej radek: '))
    y = int(input('Zadej sloupec: '))

    if x >= 4 or y >= 4 or 0 > x or 0 > y:
        print("Neplatne rozmezi. Zkus to znovu.")
    else:
        if tictactoe[x - 1][y - 1] == "X" or tictactoe[x - 1][y - 1] == "O":  # pokud je policko X nebo O
            print("Obsazeno. Zkus to znovu.")
        else:
            if playerNext == 1:  # zaskrtne policko urcitemu hraci
                tictactoe[x - 1][y - 1] = 'X'
                playerNext = 2
            elif playerNext == 2:
                tictactoe[x - 1][y - 1] = 'O'
                playerNext = 1


vyherce = 0
tictactoe = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
vykresliHru()
playerNext = 1

while vyherce == 0:
    nextTurn()
    vykresliHru()
    checkVictory(tictactoe)