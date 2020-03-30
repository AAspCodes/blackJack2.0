from random import randint
from .card import Card
cards_file_path = "black_jack_2/assets/cards.txt"

class Deck:
	_cards = []
	_number_of_decks = 0

	@classmethod
	def draw(cls):
		return cls._cards.pop(randint(0,len(cls._cards)-1))

	@classmethod
	def get_number_of_cards(cls):
		return len(cls._cards)

	@classmethod
	def ready_deck(cls,number_of_decks):
		cls._number_of_decks = number_of_decks
		decks = []
		for _ in range(number_of_decks):
			decks.extend(cls._load_cards())
		cls._cards = decks
		
	@classmethod
	def _load_cards(cls):
		with open(cards_file_path, "r") as f:
			contents = f.read()
		contents = contents.split("\n")
		cards = []
		for line in contents:
			card_name, card_type, value = line.split(",")
			new_card = Card(card_name, card_type, int(value))
			cards.append(new_card)

		return cards
