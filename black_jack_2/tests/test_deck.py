from black_jack_2.app.deck import Deck
from black_jack_2.app.card import Card
import unittest

class TestDeck(unittest.TestCase):

	def test_ready_deck(self):
		Deck.ready_deck(3)
		self.assertEqual(Deck.get_number_of_cards(), 156)

	def test_draw(self):
		Deck.ready_deck(1)
		c = Deck.draw()
		self.assertIsInstance(c,Card)
		self.assertEqual(Deck.get_number_of_cards(),51)


