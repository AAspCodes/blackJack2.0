from ..app.hand import Hand
from ..app.deck import Deck
from unittest import TestCase

class TestHand(TestCase):
	def runTest(self):


	def test_hands(self):
		print("Testing Hands", end=": ")
		print(_find_splitable())


	def _create_hand(self):
		Deck.ready_deck(2)
		hand = Hand()
		hand.add_card(Deck.draw())
		hand.add_card(Deck.draw())
		return hand

	def _find_splitable(self):
		while True:
			hand = _create_hand()
			if 6 < hand.num_of_cards:
				return False
			if hand.can_split:
				new_hand = hand.split()
				return hand.cards[0].card_type == new_hand.cards[0].card_type

	# TODO add testing for ace value changeing, names, value, eq..
			

