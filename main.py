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

print(deal_cards())


#print(cards.get('two')[random.randint(0,4)])

def calculate_score(cards): 
    first_card = CARDS_SCORES.get(cards[0])
    second_card = CARDS_SCORES.get(cards[1])
    sum = first_card + second_card
    if sum == 21:
        return 0  #blackjack
    return sum



# def main():
#     user_cards = deal_cards()  #['ace','jack']
#     computer_cards = deal_cards()
#     print(art.CARDS.get(user_cards[0])[random.randint(0,3)],art.CARDS.get(user_cards[1])[random.randint(0,3)])
#     # print(art.CARDS.get(user_cards[0])[random.randint(0,3)], end =' ')
#     # print(art.CARDS.get(user_cards[1])[random.randint(0,3)])


#     user_sum = calculate_score(user_cards)
#     computer_sum = calculate_score(computer_cards)
#     # if user_sum == 0:
#     #     print("Blackjack. You win")
#     # elif computer_sum == 0:
#     #     print("You loose. Dealer have blackjack.")

# if __name__ == "__main__":
#     main()