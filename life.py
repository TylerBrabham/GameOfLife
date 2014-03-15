
from random import randint

from time import sleep

class Life(object):

	def __init__(self, m, n):
		self.num_rows = m
		self.num_cols = n
		self.game_board = [[randint(0,1) for j in range(n)] for i in range(m)]
		self.current_time = 0

	def __str__(self):
		out_string = ''

		string_map = {0:'0', 1:'*'}

		for i, row in enumerate(self.game_board):
			row_str = [string_map[elm] for elm in row]
			out_string += ''.join(row_str)

			out_string += '\n'

		return out_string

	def run_game(self, time_steps):
		self.render_state()

		while self.current_time<time_steps:
			sleep(.1)

			self.update_state()
			self.render_state()

	def update_state(self):
		old_board = self.game_board
		new_board = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]

		for i in range(self.num_rows):
			for j in range(self.num_cols):

				num_neighbors = self.calculate_neighbors(i,j)

				if old_board[i][j]==1:
					if num_neighbors<2:
						new_board[i][j] = 0

					elif num_neighbors<4:
						new_board[i][j] = 1

					else:
						new_board[i][j] = 0

				else:
					if num_neighbors==3:
						new_board[i][j] = 1

		self.game_board = new_board
		self.current_time += 1

	def calculate_neighbors(self,i,j):
		m = self.num_rows
		n = self.num_cols

		num_neighbors = 0

		for k in range(i-1,i+2):
			if k<0 or k>m-1:
				continue

			for l in range(j-1,j+2):
				if k==i and l==j:
					continue

				if l<0 or l>n-1:
					continue

				num_neighbors += self.game_board[k][l]

		return num_neighbors

	def render_state(self):
		print self


def main():
	test_board = Life(40,100)

	test_board.game_board[1][1] = 1

	test_board.run_game(1000)

if __name__=="__main__":
	main()