import random

def get_input():
    playerMove = None
    while playerMove is None:
        candidate = input("Please input a move:").lower()
        if candidate in validMoves:
            playerMove = candidate
        else:
            print("Invalid move")
    return playerMove

def get_result(playerPicked, enemyPicked):
    matrix = [
        ["draw", "lose", "win"],
        ["win", "draw", "lose"],
        ["lose", "win", "draw"],
    ]
    return matrix[playerPicked][enemyPicked]

validMoves = ["rock", "paper", "scissors"]

enemyMoveIndex = random.randint(0,2)
enemyMove = validMoves[enemyMoveIndex]


playerMove = get_input()

playerMoveIndex = validMoves.index(playerMove)

print("Enemy picked: ", enemyMove)

result = matrix[playerMoveIndex][enemyMoveIndex]

print("you", result)










