from deck import Deck
from user_input import get_int, get_name
from player import Player
class Main:
	def __init__(self):
		number_of_players, number_of_decks = self.get_number_of_players() 
		Deck.ready_deck(number_of_decks)
		# create Dealer
		Dealer = Player("Dealer")
		# create players
		self.players = []
		for _ in range(number_of_players):
			self.players.append(Player(get_name("What is this player's name: ")))
		self.show_player_states()
		# get players money
		for player in self.players:
			player.money = get_int(100,1_000_000,
			 f"how much money does {player.name} have?\nmin: 100, max: 1 million: ")
		self.show_player_states()
		# generate hands
		
		


	@staticmethod
	def get_number_of_players():
		message = "Enter the number of players. [1-6]:  "
		number_of_players = get_int(1,6,message)
		number_of_decks = number_of_players * 2
		return number_of_players, number_of_decks

	def show_player_states(self):
		for player in self.players:
			print(player)


if __name__ == "__main__":
	Main()
