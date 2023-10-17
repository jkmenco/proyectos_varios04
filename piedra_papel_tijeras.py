import random
# rock paper scissors
def play():
    user_choise = input("'r' para Piedra, 'p' para Papel, 's' para Tijeras" )
    computer_choise = random.choice(['r', 'p', 's'])
    if user_choise == computer_choise:
        return 'Empate!'
    
    # r > s, s > p, p > r
    if is_win(user_choise, computer_choise):
        return 'Tú ganas!'
    

    return 'Tú pierdes!'
    
def is_win(player, opponent):
    # return true si el jugador gana
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    

print(play())