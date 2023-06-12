import random
from images import black_jack
from os import system
def round(player):
    new_card = random.choice([11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10])
    player.append(new_card)
    return player
def check(pessoa, computador, jogador):
    soma_pessoa = sum(pessoa)
    soma_computador = sum(computador)
    if (11 in computador) and (10 in computador) and (len(computador) == 2):
        return "bloose"
    elif (11 in pessoa) and (10 in pessoa) and (len(pessoa) == 2):
        return "bwin"
    elif soma_pessoa > 21:
        if 11 in pessoa:
            indice = pessoa.index(11)
            pessoa[indice] = 1
            return check(pessoa, computador, jogador)
        else:
            return "loose"
    elif soma_computador > 21:
        if 11 in computador:
            indice = computador.index(11)
            computador[indice] = 1
            return check(pessoa, computador, jogador)
        else:
            return "win"
    else:
        if jogador == "y":
            print(f"Your cards: {pessoa}, current score: {soma_pessoa}")
            print(f"Computer's first card: {computador[0]} || {computador} / {sum(computador)}")
            resposta = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            return resposta
        else:
            if soma_computador > 16:
                if soma_computador > soma_pessoa:
                    return "loose"
                elif soma_computador < soma_pessoa:
                    return "win"
                else:
                    return "draw"
            else:
                return "n"   
#########################################    Main    ###########################################
start = input("Do you want to play a game of blackjack? Type 'yes' or 'no': ").lower()
while start == "yes":
    print(black_jack)
    answer2 = "y"
    computer = []
    person = []
    for i in range(2):
        person = round(person)
        computer = round(computer) 
    while True:
        answer2 = check(pessoa = person, computador = computer, jogador = answer2)
        #print(answer2)
        if answer2 == "y":
            person = round(person)
        elif answer2 == "n":
            computer = round(computer)
        else:
            print(f"Your final hand: {person}, final score: {sum(person)}")
            print(f"Computer's final hand: {computer}, final score: {sum(computer)}")
            if answer2 == "draw":
                print("It's a draw!")
            elif answer2 == "win":
                print("You win!")
            elif answer2 == "loose":
                print("You loose!")
            elif answer2 == "bwin":
                print("Blackjack!! You win!")
            elif answer2 == "bloose":
                print("Blackjack!! You loose!")
            else:
                print("Invalid answer! End of the game.")
            break
    start = input("Do you want to play a game of blackjack? Type 'yes' or 'no': ").lower()
    system("cls")