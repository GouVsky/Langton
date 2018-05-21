from ant import Ant
from game import Game
from window import Window
from checkerboard import Checkerboard


window = Window("Langton Ant")


width = 150
height = 150

checkerboard = Checkerboard(window, window.width, window.height, 'white')

checkerboard.create_board(width, height)

ant = Ant(width / 2, height / 2, 'black')


game = Game(ant, checkerboard)

for i in range (0, 12000):
	
	game.run()
	
	window.update()

window.display()
