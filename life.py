
from random import randint, random

from time import sleep

import sys

class Life(object):

	def __init__(self, m, n, seed=None):
		self.num_rows = m
		self.num_cols = n

		if seed=='glidergun':
			self.game_board = self.glider_board()
		elif seed=='checker':
			self.game_board = self.checker_board()
		else:
			self.game_board = [[randint(0,1) for j in range(n)] for i in range(m)]

		self.current_time = 0

	def __str__(self):
		out_string = ''

		string_map = {0:' ', 1:'O'}

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

				rand_val = random()
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

	def checker_board(self):
		n = self.num_cols
		m = self.num_rows

		board =  [[0 for j in range(n)] for i in range(m)]

		for i in range(0, m):
			if i%2==0:
				for j in range(0,n,2):
					board[i][j] = 1
			else:
				for j in range(1,n,2):
					board[i][j] = 1


		return board


	def glider_board(self):

		n = self.num_cols
		m = self.num_rows

		board =  [[0 for j in range(n)] for i in range(m)]

		#left block
		board[5][1] = 1
		board[5][2] = 1
		board[6][1] = 1
		board[6][2] = 1

		#middle circle
		board[3][13] = 1
		board[3][14] = 1
		board[4][12] = 1
		board[4][16] = 1

		board[5][11] = 1
		board[5][17] = 1
		board[6][11] = 1
		board[6][15] = 1
		board[6][17] = 1
		board[6][18] = 1
		board[7][11] = 1
		board[7][17] = 1

		board[8][12] = 1
		board[8][16] = 1
		board[9][13] = 1
		board[9][14] = 1

		#middle v
		board[1][25] = 1
		board[2][23] = 1
		board[2][25] = 1

		board[3][21] = 1
		board[3][22] = 1
		board[4][21] = 1
		board[4][22] = 1
		board[5][21] = 1
		board[5][22] = 1

		board[6][23] = 1
		board[6][25] = 1
		board[7][25] = 1

		#right block
		board[3][35] = 1
		board[3][36] = 1
		board[4][35] = 1
		board[4][36] = 1

		return board


def main(argv):
	# test_board = Life(40,100,'glidergun')
	# test_board.run_game(int(argv[1]))

	test_board = Life(int(argv[2]),int(argv[3]), seed=argv[4])
	test_board.run_game(int(argv[1]))


if __name__=="__main__":
	main(sys.argv)