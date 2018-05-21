from Tkinter import *

from square import Square


class Checkerboard(Canvas):
	
	def __init__(self, window, board_width, board_height, background_color):
		
		Canvas.__init__(self, window, width=board_width, height=board_height, background=background_color)
		
		self.width = board_width
		self.height = board_height
		self.background_color = background_color
		
		# In fact a list of lists.
		self.squares = []
		
		self.pack();
				
				
	
	def create_board(self, number_squares_row, number_squares_column):
		
		squares_width = self.width / number_squares_row
		squares_height = self.height / number_squares_column
		
		for i in range (0, number_squares_row):

			squares_by_row = []

			x1 = i * squares_width

			for j in range (0, number_squares_column):
				
				y1 = j * squares_height
								
				squares_by_row.append(Square(x1, y1, squares_width, squares_height, self.background_color))
			
			self.squares.append(squares_by_row)
	
	
	
	def fill_square(self, row, column, color):
		
		square = self.squares[row][column]
		
		x1 = square.x
		y1 = square.y
		x2 = x1 + square.width
		y2 = y1 + square.height
		
		square.color = color
		
		self.create_rectangle(x1, y1, x2, y2, fill=color, outline=color)
