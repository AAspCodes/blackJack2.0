from black_jack_2.app.card import Card, CantSetValueException
import unittest


class TestCard(unittest.TestCase):

	def test_eights(self):
		
		card = Card("The Eight of Hearts", "Eight", 8)
		card2 = Card("The Eight of Hearts", "Eight", 8)

		self.assertEqual(card, card2)
		self.assertIsNot(card, card2)
		self.assertEqual(card.name, 'The Eight of Hearts')
		self.assertEqual(card.value, 8)
		self.assertEqual(card.card_type, "Eight")

		with self.assertRaises(CantSetValueException):
			card.value = 2
		
	def test_aces(self):
		
		card = Card('The Ace of Spades', 'Ace', 11)

		self.assertEqual(card.name, 'The Ace of Spades')
		self.assertEqual(card.value, 11)
		self.assertEqual(card.card_type, 'Ace')
		
		card.value = 1
		self.assertEqual(card.value, 1)

		with self.assertRaises(CantSetValueException):
			card.value = 11
			

