import art, random, os, util
os.system("")

def print_red(skk): print("\033[91m{}\033[00m" .format(skk))
def print_green(skk): print("\033[92m {}\033[00m" .format(skk))
def print_yellow(skk): print("\033[93m {}\033[00m" .format(skk))

CARDS_SCORES = {"A": 11, "K": 10, "Q": 10, "J": 10, "10": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}

CARDS_COLORS = ['♣', '♠', '♦', '♥']

def deal_card():
    dealed_card = []
    card = random.choice(list(CARDS_SCORES))
    dealed_card.append(CARDS_COLORS[random.randint(0,3)] + card)
    return dealed_card

def calculate_score(dealed_cards): 
    sum = 0
    ace = False
    for card in dealed_cards:
        card_sum = CARDS_SCORES.get(card[1:])
        if card_sum == 11: #ace
            ace = True
        sum += card_sum
    if sum == 21:
        return 0 #blackjack
    if sum > 21:
        if ace == True:
            sum -= 10
    return sum

def get_card(card):  #"♥Q"
    suit = card[0]
    value = card[1:]  # 1: for '10'
    return (
        ' ___ \n'
        '|{} |\n'
        '| {}|\n'
        '|_{}|\n'
    ).format(
        format(value, '<2'),
        format(suit, '<2'),
        format(value, '>2')
    ).splitlines()

def display_cards(cards):
    for lines in zip(*map(get_card, cards)):
        print(*lines)

def draw_a_card():
    while True:
        user_answer = input("\n\n---> Do you want to draw another card? Y/N ").upper()
        if user_answer == "Y":
            return True
        elif user_answer == "N":
            return False
        else:
            print("Wrong answer. Please write Y for yes and N for no.")
            continue

def print_all(hidden_cards, user_cards, user_sum):
    print_yellow("\nDEALER HAND:")
    display_cards(hidden_cards)
    print_yellow("\n\nYOUR HAND:")
    display_cards(user_cards)
    if user_sum == 0:
        user_sum = 21
    print_green(f"\nYour score: {user_sum}")

def check_closer_to_blackjack(user_sum, computer_sum):
    user_diffrence = 21 - user_sum
    computer_diffrence = 21 - computer_sum
    if user_diffrence > computer_diffrence:
        art.print_loose(computer_sum)  #computer wins
    else:
        art.print_win()
        print_green(f'Dealer have {computer_sum} points.')

def dealer_draw(computer_sum):
    if computer_sum < 17:
        return True
    else:
        return False

def print_results(user_sum, computer_sum):
    if user_sum == 0 or user_sum == 21:
        art.print_win()
        art.print_blackjack()
        return False
    elif user_sum > 21:
        art.print_loose(computer_sum)
        if computer_sum == 0 or computer_sum == 21:
            print_red('Dealer win this game.')
            art.print_blackjack()
    elif computer_sum > 21:
        art.print_win()
        return False

def restart_game():
    while True:
        user_answer = input("\n\n---> Do you want to play again? Y/N ").upper()
        if user_answer == "Y":
            return True
        elif user_answer == "N":
            return False
        else:
            print("Wrong answer. Please write Y for yes and N for no.")
            continue
    

def main():
    user_cards = deal_card() + deal_card()  #['♦J', '♥6']
    user_sum = calculate_score(user_cards)
    computer_cards = deal_card() + deal_card()
    computer_sum = calculate_score(computer_cards)
    hidden_cards = computer_cards[:]
    hidden_cards[0] = "##"
    while True:
        util.clear_screen()
        print_all(hidden_cards, user_cards, user_sum)
        if print_results(user_sum, computer_sum) == False:
            if restart_game() == True:
                continue
            else:
                break
        else:
            while True:
                if draw_a_card() == True:
                    util.clear_screen()
                    user_cards += deal_card()
                    user_sum = calculate_score(user_cards)
                    print_all(hidden_cards, user_cards, user_sum)
                    if print_results(user_sum, computer_sum) == False:
                        if restart_game() == True:
                            main()
                        else:
                            break
                    if dealer_draw(computer_sum) == True:
                        input('\nPlease ENTER to go on . . .')
                        util.clear_screen()
                        print_green('\nDealer draw a card.')
                        computer_cards += deal_card()
                        computer_sum = calculate_score(computer_cards)
                        hidden_cards = computer_cards[:]
                        hidden_cards[0] = "##"
                    else:
                        util.clear_screen()
                        print_green("\nDealer don't draw a card.")
                    print_all(hidden_cards, user_cards, user_sum)
                else:
                    check_closer_to_blackjack(user_sum, computer_sum)
                    if restart_game() == True:
                        main()
                    else:
                        break

if __name__ == "__main__":
    main()