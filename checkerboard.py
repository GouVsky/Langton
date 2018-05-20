from Tkinter import *


class Checkerboard(Canvas):
	
	def __init__(self, window, board_width, board_height):
		
		Canvas.__init__(self, window, width=board_width, height=board_height, background='white')
		
		self.width = board_width
		self.height = board_height
		
		self.pack();
				
	
	def create_board(self, number_squares_row, number_squares_column):
		
		squares_width = self.width / number_squares_row
		squares_height = self.height / number_squares_column
		
		
		# Alternating black and white squares.
		
		for i in range (0, number_squares_row + 1, 2):

			for j in range (0, number_squares_column + 1):
				
				x1 = i * squares_width
				y1 = j * squares_height
				
				x2 = x1 + squares_width
				y2 = y1 + squares_height
				
				
				# Alternating black and white squares on columns.

				if (j % 2 == 0):
					
					x1 += squares_width
					x2 += squares_width
				
				self.create_rectangle(x1, y1, x2, y2, fill='black')
