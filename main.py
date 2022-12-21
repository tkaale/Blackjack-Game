import art, random

CARDS_SCORES = {"ace": 11, "king": 10, "queen": 10, "jack": 10, "ten": 10, "nine": 9, "eight": 8, "seven": 7, "six": 6, "five": 5, "four": 4, "three": 3, "two": 2}

#print(cards_scores.get("ace"))  == [1,11]

def deal_cards():
    cards_list = []
    dealed_cards = []
    for card in CARDS_SCORES.keys():
        cards_list.append(card)
    dealed_cards.append(random.choice(cards_list))
    dealed_cards.append(random.choice(cards_list))
    return dealed_cards

#print(deal_cards())


def calculate_score(cards): 
    first_card = CARDS_SCORES.get(cards[0])
    second_card = CARDS_SCORES.get(cards[1])
    sum = first_card + second_card
    return sum
      
print(calculate_score(['ace','jack']))


# def main():
#     user_cards = deal_cards()  #['ace','jack']
#     computer_cards = deal_cards()

# if __name__ == "__main__":
#     main()