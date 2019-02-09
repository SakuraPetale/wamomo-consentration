from card import Card
from player import Player

Trump = Card()
player = Player()

Trump.stack_init()

while(Trump.check_fin() == False):
    Trump.show_deck()
    while(True):
        print("select 1st card")
        selecting_position = int(input())
        selected = Trump.select_card(selecting_position)
        if (selected == False):
            print("error")
            continue
        else:
            card1 = Trump.deck[selecting_position]
            break

    while(True):
        print("select 2nd card")
        selecting_position = int(input())
        selected = Trump.select_card(selecting_position)
        if (selected == False):
            print("error")
            continue
        else:
            card2 = Trump.deck[selecting_position]
            break

    is_pair = Trump.check_pair(card1, card2)
    if (is_pair == True):
        player.point += 1
