from gtn import guess_the_num
from rps import rps

while True:
	txt = """Mini Games!!!
		- Guess The Number (1)
		- Rock, Paper, Scissors (2)
		- Wordle (3)
		- Connect Four (4)
		- Tic Tac Toe (5)
	
	Select a game (press a number or 'q' to quit): """
	val = input(txt)
	
	if val == '1':
		guess_the_num(input)
	elif val == '2':
		rps()
	elif val == '3':
		pass
	elif val == '4':
		pass
	elif val == '5':
		pass 
	elif val == 'q': #so it doesnt need to be a variable, just input
		break
