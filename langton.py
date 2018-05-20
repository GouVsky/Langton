from window import Window

from checkerboard import Checkerboard


window = Window("Langton Ant")

checkerboard = Checkerboard(window, window.get_width(), window.get_height())

checkerboard.create_board(20, 20)

window.display()
