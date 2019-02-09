import random

class Card:

    SUIT_SPADE = 'S'
    SUIT_CLUB = 'C'
    SUIT_DIA = 'D'
    SUIT_HEART = 'H'

    SUIT_LIST = [SUIT_SPADE, SUIT_CLUB, SUIT_DIA, SUIT_HEART]
    FACE_LIST = ['A'] + list(map(str, range(2,11))) + ['J', 'Q', 'K']

    deck = []
    cnt_pair = 0

    # 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10| 11| 12
    # 13| 14| 15| 16| 17| 18| 19| 20| 21| 22| 23| 24| 25
    # 26| 27| 28| 29| 30| 31| 32| 33| 34| 35| 36| 37| 38
    # 39| 40| 41| 42| 43| 44| 45| 46| 47| 48| 49| 50| 51

    # card state
    #       0: down
    #       1: up
    #       2: None
    def __init__(self, rank=None, suit=None, state=0):
        if (rank == None):
            self.rank = random.randint(1, 13)
        else:
            self.rank = rank

        if (suit == None):
            self.suit = random.choice(Card.SUIT_LIST)
        else:
            self.suit = suit
        self.state = state

    def get_face(self):
        return Card.FACE_LIST[self.rank]

    def stack_init(self):
        for n in range(1,14):
            for m in Card.SUIT_LIST:
                Card.deck.append(Card(rank=n, suit=m, state=0))
        # random.shuffle(Card.deck)

    def show_deck(self):
        for k in range(4):
            for i in range(13):
                print(Card.deck[i + k * 13].rank, end="")
                print("|", end="")
                #print("(", end="")
                #print(i + k *13 ,end="")
                #print(")", end="")
            print("\n")

    def check_card_state(self, card):
        return card.state

    def select_card(self, position):
        if (Card.deck[position].state == 2 or Card.deck[position].state == 1):
            return False
        else:
            Card.deck[position].state = 1
            return True

    def check_pair(self, card1, card2):
        if (card1.state == 1 and card2.state == 1 and card1.rank == card2.rank):
            card1.state = 2
            card2.state = 2
            Card.cnt_pair += 1
            return True
        else:
            if (card1.state == 2 or card2.state == 2):
                return False
            else:
                card1.state = 0
                card2.state = 0
                return False

    def check_fin(self):
        if (Card.cnt_pair == 26):
            return True
        else:
            return False

    # not needed
    def draw_card(self, num=1):
        cards = Card.deck[0:num]
        Card.deck = Card.deck[num:]
        return cards
