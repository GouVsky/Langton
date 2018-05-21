from ant import Ant
from game import Game
from window import Window
from checkerboard import Checkerboard


window = Window("Langton Ant")


checkerboard = Checkerboard(window, window.width, window.height)

checkerboard.create_board(8, 8)

ant = Ant(3, 3, 'black')


game = Game(ant, checkerboard)

game.run()


window.display()
