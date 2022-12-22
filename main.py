import art, random

CARDS_SCORES = {"A": 11, "K": 10, "Q": 10, "J": 10, "10": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}

CARDS_COLORS = ['♣', '♠', '♦', '♥']


def deal_cards():
    dealed_cards = []
    card_one = random.choice(list(CARDS_SCORES))
    card_two = random.choice(list(CARDS_SCORES))
    dealed_cards.append(CARDS_COLORS[random.randint(0,3)] + card_one)
    dealed_cards.append(CARDS_COLORS[random.randint(0,3)] + card_two)
    return dealed_cards


#cards = ['♦J', '♥6']

def calculate_score(dealed_cards): 
    first_card = CARDS_SCORES.get(dealed_cards[0][1])
    second_card = CARDS_SCORES.get(dealed_cards[1][1])
    sum = first_card + second_card
    if sum == 21:
        return 0  #blackjack
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



def main():
    user_cards = deal_cards()  #['♦J', '♥6']
    computer_cards = deal_cards()
    hidden_cards = computer_cards[:]
    hidden_cards[0] = "##"
    print("\nDEALER HAND:")
    display_cards(hidden_cards)
    print("\n\nYOUR HAND:")
    display_cards(user_cards)


    # if user_sum == 0:
    #     print("Blackjack. You win")
    # elif computer_sum == 0:
    #     print("You loose. Dealer have blackjack.")

if __name__ == "__main__":
    main()