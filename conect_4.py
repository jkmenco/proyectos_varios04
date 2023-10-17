def create_board():
    # Función para crear el tablero
    board = [['-' for i in range(7)] for j in range(6)]
    return board

def print_board(board):
    # Función para imprimir el tablero
    for row in board:
        print('|', end='')
        for col in row:
            print(col + '|', end='')
        print()
    print('---------------')

def make_move(player, col, board):
    # Función para hacer una jugada
    row = 5
    while row >= 0:
        if board[row][col] == '-':
            board[row][col] = player
            return True
        row -= 1
    return False

def check_win(player, board):
    # Función para comprobar si un jugador ha ganado
    # Comprobación de filas
    for row in range(6):
        for col in range(4):
            if board[row][col] == player and board[row][col+1] == player and board[row][col+2] == player and board[row][col+3] == player:
                return True
    # Comprobación de columnas
    for row in range(3):
        for col in range(7):
            if board[row][col] == player and board[row+1][col] == player and board[row+2][col] == player and board[row+3][col] == player:
                return True
    # Comprobación de diagonales
    for row in range(3):
        for col in range(4):
            if board[row][col] == player and board[row+1][col+1] == player and board[row+2][col+2] == player and board[row+3][col+3] == player:
                return True
    for row in range(3, 6):
        for col in range(4):
            if board[row][col] == player and board[row-1][col+1] == player and board[row-2][col+2] == player and board[row-3][col+3] == player:
                return True
    return False

def main():
    # Función principal del juego
    board = create_board()
    player = 'X'
    while True:
        print_board(board)
        col = int(input("Jugador {} ({}), ingresa el número de la columna donde quieres jugar: ".format(player, 'X' if player == 'X' else 'O')))
        if make_move(player, col, board):
            if check_win(player, board):
                print_board(board)
                print("¡Felicidades, jugador {} ({})! ¡Has ganado!".format(player, 'X' if player == 'X' else 'O'))
                break
            if player == 'X':
                player = 'O'
            else:
                player = 'X'
        else:
            print("La columna está llena, intenta en otra.")
            continue

if __name__ == '__main__':
    main()
