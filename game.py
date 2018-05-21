class Game:
	
	def __init__(self, ant, checkerboard):
		
		self.ant = ant
		self.checkerboard = checkerboard



	def run(self):
		
		x = self.ant.x
		y = self.ant.y
		
		square = self.checkerboard.squares[self.ant.x][self.ant.y]
		
		color = None
		
		if (square.color == 'white'):
			
			color = self.ant.color
			
			self.ant.rotate_right()
			
		elif (square.color == self.ant.color):
			
			color = 'white'
			
			self.ant.rotate_left()


		self.checkerboard.fill_square(self.ant.x, self.ant.y, color)

		self.ant.move()
