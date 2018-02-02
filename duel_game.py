import Tkinter as tk 
import random

LARGE_FONT = ("Verdana", 16)

class DuelGame(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		container = tk.Frame(self)

		container.pack(side="top", fill="both", expand=True)

		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.frames = {}

		for F in (StartPage, Game):

			frame = F(container, self)

			self.frames[F] = frame

			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame(StartPage)

	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

class StartPage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Duel Game", font=LARGE_FONT)
		label.pack(pady=100, padx=100) #suboptimal, should use grid

		start_button = tk.Button(self, text="Start", 
			command=lambda:controller.show_frame(Game))
		start_button.pack()
		exit_button = tk.Button(self, text="Exit", command=self.exit)
		exit_button.pack()

	def exit(self):
		self.quit()

class Game(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Teh ReAl Du3l G4m3", font=LARGE_FONT)
		label.pack(pady=100, padx=100) #suboptimal, should use grid

		step_button = tk.Button(self, text="Step", command=self.step)
		step_button.pack()
		shoot_button = tk.Button(self, text="Shoot", command=self.shoot)
		shoot_button.pack()
		reset_button = tk.Button(self, text="Reset", command=self.reset)
		reset_button.pack()
		end_button = tk.Button(self, text="I'm bored...", 
			command=lambda:controller.show_frame(StartPage))
		end_button.pack()
		self.d = 20
		self.n = self.d

	def step(self):
		if self.d > 0:
			self.d -= 1
		else:
			print "Invalid move"
		print "You are now", self.d, "steps away."

	def shoot(self, p=1):
		p=lambda n, d: (.9/n)*(n-d)+.1
		if random.random() < p(self.n, self.d):
			print True
			print "Game ends!"
		else:
			print False

	def reset(self):
		pass

app = DuelGame()
app.mainloop()