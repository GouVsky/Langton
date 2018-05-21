from collections import deque

from square import Square


class Ant:
	
	def __init__(self, x, y, color):
		
		# x and y values are indexes of squares on the checkerboard, not their coordinates.
		
		self.x = x
		self.y = y
		
		self.color = color
		
		self.directions	= deque('top left bottom right'.split(' '))
		
		self.direction = self.directions[0]
		
		
		
	def rotate_left(self):
						
		self.directions.rotate(-1)
		
		self.direction = self.directions[0]
		
		
		
	
	def rotate_right(self):
		
		self.directions.rotate(1)
		
		self.direction = self.directions[0]



	def move(self):
				
		if (self.direction == 'top'):
			
			self.y += -1
			
		elif (self.direction == 'left'):
			
			self.x += -1
			
		elif (self.direction == 'bottom'):
			
			self.y += 1
			
		elif (self.direction == 'right'):
			
			self.x += 1
