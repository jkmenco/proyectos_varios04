import random

def play_game(player_choice, computer_choice):
    if player_choice == computer_choice:
        print("¡Empate!")
    elif (player_choice == 1 and computer_choice == 3) or (player_choice == 2 and computer_choice == 1) or (player_choice == 3 and computer_choice == 2):
        print("¡Ganaste!")
    else:
        print("¡Perdiste!")

def game_present():
    print("\tJuguemos piedra, papel o tijera!")
    print()
    print("1. Piedra\n2. Papel\n3. Tijera")


def game_info(player_choice, computer_choice):
    if player_choice == 1:
        print("Elegiste Piedra!")
    elif player_choice == 2:
        print("Elegiste Papel!")
    else:
        print("Elegiste Tijera!")
        
    if computer_choice == 1:
        print("La computadora eligió Piedra!")
    elif computer_choice == 2:
        print("La computadora eligió Papel!")
    else:
        print("La computadora eligió Tijera!")
    
game_present()

def turn_players():
    options = [1, 2, 3]

    computer_choice = random.choice(options)

    player_choice = int(input("¿Piedra, papel o tijera? ---> "))
    return player_choice, computer_choice

player_choice, computer_choice = turn_players()

game_info(player_choice, computer_choice)

play_game(player_choice, computer_choice)

player_choice, computer_choice = turn_players()

game_info(player_choice, computer_choice)

play_game(player_choice, computer_choice)

player_choice, computer_choice = turn_players()

game_info(player_choice, computer_choice)

play_game(player_choice, computer_choice)