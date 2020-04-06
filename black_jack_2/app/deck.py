from random import randint
from .card import Card
import json
cards_file_path = "black_jack_2/assets/cards.json"

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

		data = json.loads(contents)
		cards = []
		for card in data:
			new_card = Card(card["name"], card["card_type"], int(card["value"]))
			cards.append(new_card)

		return cards
