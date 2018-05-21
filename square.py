class Square:
	
	id = -1
	
	def __init__(self, x, y, width, height, color):
			
		Square.id += 1
		
		self.id	= Square.id
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.color = color
