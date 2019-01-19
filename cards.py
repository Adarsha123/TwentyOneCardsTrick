import random


class Cards:
    def __init__(self):
        pass

    def check(self, card_num):
        if card_num == 1:
            self.card = "Ace"
        elif card_num == 11:
            self.card = "Jack"
        elif card_num == 12:
            self.card = "Queen"
        elif card_num == 13:
            self.card = "King"
        elif 2 <= card_num <= 10:
            self.card = str(card_num)
        else:
            self.card = "RankError"
        return self.card

    def deck(self):
        deck = []
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        for s in suits:
            for n in range(1, 14):
                a = Cards.check(self, n)
                deck.append(a + " of " + s)
        return deck



