import Tkinter as tk

class Window:
	
	def __init__(self):
		
		self.x = 0
		self.y = 0
		self.width = 500
		self.height = 500
		
		
	def center(self, window):
		
		# We center the window.
		
		self.x = window.winfo_screenwidth() / 2 - self.width / 2
		self.y = window.winfo_screenheight() / 2 - self.height / 2
				
		
	def display(self):
		
		window = tk.Tk()		
				
		window.geometry("%dx%d+%d+%d" % (self.width, self.height, self.x, self.y))
		window.title("Langton Ant")
		window.resizable(False, False)
		
		self.center(window)
		
		window.mainloop();
