import pygame, math


class Conect4:
	def __init__(self):
		pygame.init()

		self.board = [
		[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0]
		]


		self.height, self.width = 700, 700
		self.title = 'Conect4'


	def screen(self):
		pygame.display.set_caption(self.title)
		s = pygame.display.set_mode((self.width, self.height))
		return s


	def game_loop(self):
		self.scr = self.screen()
		run = True
		player = 1

		while run:

			mouse_x, mouse_y = pygame.mouse.get_pos()

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False

				if event.type == pygame.MOUSEBUTTONDOWN:
					if pygame.mouse.get_pressed()[0] == 1:
						pos = self.down_circle(mouse_x)
						if player == 1 and pos != -1:
							self.board[pos][int(mouse_x // 100)] = 1
							player = 2
						elif player == 2 and pos != -1:
							self.board[pos][int(mouse_x // 100)] = 2
							player = 1
			
			self.scr.fill(self.colors('black'))

			self.draw_board(0, 0, 50)
			self.draw_player(50 + int(mouse_x // 100 * 100), 50, 50, player)
			self.end_game(player)

			self.update()
			self.fps(30)

		self.exit_game()



	def draw_board(self, start_x, start_y, r):
		x = start_x + r
		y = start_y + r + (abs((len(self.board) * r) - (len(self.board[0]) * r)) * 2)
		for i in range(len(self.board)):
			for j in range(len(self.board[i])):
				if self.board[i][j] == 1:
					pygame.draw.circle(self.scr, self.colors('red'), (x, y), r)
					#pygame.draw.circle(self.scr, self.colors('black'), (x, y), r, 1)
				elif self.board[i][j] == 2:
					pygame.draw.circle(self.scr, self.colors('blue'), (x, y), r)
					#pygame.draw.circle(self.scr, self.colors('black'), (x, y), r, 1)
				else:
					pygame.draw.circle(self.scr, self.colors('white'), (x, y), r)
					#pygame.draw.circle(self.scr, self.colors('black'), (x, y), r, 1)
				x += r * 2
			y += r * 2
			x = start_x + r


	def draw_player(self, x, y, r, p):
		if p == 1:		
			pygame.draw.circle(self.scr, self.colors('red'), (x, y), r)
		elif p == 2:
			pygame.draw.circle(self.scr, self.colors('blue'), (x, y), r)


	def down_circle(self, mx):
		c = int(mx // 100)
		for i in range(len(self.board)):
			if self.board[i][c] != 0:
				return i - 1
		return 5


	def end_game(self, player):
		pass


	def colors(self, c):
		color = {
		'black':(0, 0, 0),
		'white':(255, 255, 255),
		'red':(255, 0, 0),
		'blue':(0, 0, 255)
		}
		return color[c]


	def update(self):
		pygame.display.update()


	def fps(self, value):
		clock = pygame.time.Clock()
		return clock.tick(value)


	def exit_game(self):
		pygame.quit()



game = Conect4()
game.game_loop()
