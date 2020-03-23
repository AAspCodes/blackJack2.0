from hand import Hand
from deck import Deck

def create_hand():
	Deck.ready_deck(2)
	hand = Hand()
	hand.add_card(Deck.get_random_card())
	hand.add_card(Deck.get_random_card())
	return hand

def find_splitable():
	while True:
		hand = create_hand()
		if 6 < hand.num_of_cards:
			break
		if hand.can_split:
			print("can split", hand)
			new_hand = hand.split()
			print("old_hand", hand)
			print("new hand", new_hand)
			return

			


find_splitable()
