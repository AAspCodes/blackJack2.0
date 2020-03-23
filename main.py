from deck import Deck
from user_input import get_int

class Main:
	def __init__(self):
		number_of_players, number_of_decks = self.get_number_of_players() 

		Deck.ready_deck(number_of_decks)

		print(Deck.get_number_of_cards())

	@staticmethod
	def get_number_of_players():
		message = "Enter the number of players. [1-6]:  "
		number_of_players = get_int(1,6,message)
		number_of_decks = number_of_players * 2
		return number_of_players, number_of_decks


if __name__ == "__main__":
	Main()
