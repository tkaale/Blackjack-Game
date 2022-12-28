import art, random
import sys
import os
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

#card = ['♦J']

def calculate_score(dealed_cards): 
    sum = 0
    ace = False
    for card in dealed_cards:
        card_sum = CARDS_SCORES.get(card[1])
        if card_sum == 11:
            ace = True
        sum += card_sum
    if sum == 21:
        return 0 #blackjack
    if sum > 21:
        if ace == True:
            sum -= 10
    return sum

print(calculate_score(['♠A', '♥Q', "♥Q"]))


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



def main():
    user_cards = deal_card() + deal_card()  #['♦J', '♥6']
    computer_cards = deal_card() + deal_card()
    hidden_cards = computer_cards[:]
    hidden_cards[0] = "##"
    print_yellow("\nDEALER HAND:")
    display_cards(hidden_cards)
    print_yellow("\n\nYOUR HAND:")
    display_cards(user_cards)


    # if user_sum == 0:
    #     print("Blackjack. You win")
    # elif computer_sum == 0:
    #     print("You loose. Dealer have blackjack.")

# if __name__ == "__main__":
#     main()