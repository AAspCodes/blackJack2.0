from black_jack_2.app.card import Card
from unittest import TestCase


class TestCard(TestCase):
	def runTest(self):
		self.test_eights()
		self.test_aces()


	def test_eights(self):
		
		
		card = Card("The Eight of Hearts", "Eight", 8)
		card2 = Card("The Eight of Hearts", "Eight", 8)

		self.assertEqual(card, card2)
		self.assertIsNot(card, card2)
		self.assertEqual(card.name, 'The Eight of Hearts')
		self.assertEqual(card.value, 8)
		self.assertEqual(card.card_type, "Eight")

		try:
			card.value = 2
		except Exception:
			self.assertTrue(True)
		else:
			self.assertFalse(False)

	def test_aces(self):
		
		card = Card('The Ace of Spades', 'Ace', 11)

		self.assertEqual(card.name, 'The Ace of Spades')
		self.assertEqual(card.value, 11)
		self.assertEqual(card.card_type, 'Ace')

		try:
			card.value = 1
		except Exception:
			self.assertFalse(False)
		else:
			self.assertTrue(True)
			self.assertEquals(card.value, 1)

		try:
			card.value = 11
		except Exception:
			self.assertTrue(True)
		else:
			self.assertFalse(False)
			

