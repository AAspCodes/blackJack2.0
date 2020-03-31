from black_jack_2.app.hand import Hand
from black_jack_2.app.deck import Deck
import unittest

class TestHand(unittest.TestCase):
	
	def setUp(self):
		Deck.ready_deck(2)

	def test_hands(self):
		hand = Hand([Deck.draw(),Deck.draw()], bet=100)
		self.assertEqual(hand.num_of_cards, 2)
		self.assertEqual(hand.value, hand.cards[0].value + hand.cards[1].value)
		self.assertEqual(hand.bet, 100)



	def test_splitting(self):
		hand = self._find_splitable()
		self.assertTrue(hand.can_split)
		self.assertEqual(hand.num_of_cards,2)
		new_hand = hand.split()
		self.assertEqual(hand.num_of_cards,1)
		self.assertEqual(new_hand.num_of_cards,1)
		self.assertLess(hand.value, 12)
		self.assertLess(new_hand.value, 12)



	def _create_hand(self):
		Deck.ready_deck(2)
		return Hand([Deck.draw(),Deck.draw()])

	def _find_splitable(self):
		while True:
			hand = self._create_hand()
			if 6 < hand.num_of_cards:
				return False
			if hand.can_split:
				return hand

	# TODO add testing for ace value changeing, names, value, eq..
			

