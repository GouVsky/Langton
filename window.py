from Tkinter import *


class Window(Tk):
	
	def __init__(self, title):
		
		Tk.__init__(self)
		
		self.x = 0
		self.y = 0
		self.width = 500
		self.height = 500
		self.window_title = title
		
		
	def center(self):
		
		# We center the window.
		
		self.x = self.winfo_screenwidth() / 2 - self.width / 2
		self.y = self.winfo_screenheight() / 2 - self.height / 2
				
		
	def display(self):
					
		self.center()
		
		self.geometry("%dx%d+%d+%d" % (self.width, self.height, self.x, self.y))
		self.title(self.window_title)
		self.resizable(False, False)
				
		self.mainloop();


	def get_width(self):
		
		return self.width
		
		
	def get_height(self):
		
		return self.height
