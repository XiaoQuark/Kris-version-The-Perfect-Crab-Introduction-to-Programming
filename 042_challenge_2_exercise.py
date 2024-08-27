# Video alternative: https://vimeo.com/954334009/67af9910fc#t=1054

# So far you've spent a lot of time writing new programs.

# This is great for learning the fundamentals of code, but
# actually isn't very realistic. Most software engineers
# spend their time modifying and maintaining existing
# programs, not writing entirely new ones.

# Below is the same program as in the example. Your
# challenge is to implement some improvements:

# V 1. Right now users can place their tiles over the other
#    user's tiles. Prevent this.

# V 2. Right now if the game reaches a draw with no more free
#    spaces, the game doesn't end. Make it end at that
#    point.

# V 3. If you want a real challenge, try to rework this
#    program to support a 5x5 board rather than a 3x3 board.

# V 4. If you're still not satisfied, try to rework this
#    program to take a parameter `board_size` and play a
#    game with a board of that size.

# This is getting really challenging now — and is entirely
# optional. Don't forget about your assessment!

def play_game(num):
  board = [["."] * num for row in range(num)]
  player = "X"
  while not is_game_over(board, num):
    print(print_board(board))
    print("It's " + player + "'s turn.")
    # `input` asks the user to type in a string
    # We then need to convert it to a number using `int`
    row = int(input(f"Enter a row between 0 and {num - 1}: "))
    column = int(input(f"Enter a column between 0 and {num - 1}: "))
    # check_move(board, row, column)
    if board[row][column] != ".":
      print("This position is already full. Try again!")
    else:
      board = make_move(board, row, column, player)
      if player == "X":
        player = "O"
      else:
        player = "X"  
  print(print_board(board))
  print("Game over!")

def print_board(board):
  formatted_rows = []
  for row in board:
    formatted_rows.append(" ".join(row))
  grid = "\n".join(formatted_rows)
  return grid

def make_move(board, row, column, player):
  board[row][column] = player
  return board

# This function will extract three cells from the board
def get_cells(board, *coords):
  return [board[row][col] for row, col in coords]

# This function will check if the group is fully placed
# with player marks, no empty spaces.
def is_group_complete(board, *coords):
  cells = get_cells(board, *coords)
  return "." not in cells

# This function will check if the group is all the same
# player mark: X X X or O O O
def are_all_cells_the_same(board, *coords):
  cells = get_cells(board, *coords)
  # all()checks all values in iterable are true
  return all(cell == cells[0] for cell in cells)

# We'll make a list of groups to check:

# groups_to_check = [
#   # Rows
#   [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)],
#   [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4)],
#   [(2, 0), (2, 1), (2, 2), (2, 3), (2, 4)],
#   [(3, 0), (3, 1), (3, 2), (3, 3), (3, 4)],
#   [(4, 0), (4, 1), (4, 2), (4, 3), (4, 4)],
#   # Columns
#   [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)],
#   [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1)],
#   [(0, 2), (1, 2), (2, 2), (3, 2), (4, 2)],
#   [(0, 3), (1, 3), (2, 3), (3, 3), (4, 3)],
#   [(0, 4), (1, 4), (2, 4), (3, 4), (4, 4)],
#   # Diagonals
#   [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)],
#   [(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)]
# ]

def create_groups_to_check(num):
  groups_to_check = []
  # for loop: i = index, num=grid size
  for i in range(num):
    # create row: list of tuples (non mutable list)
    # i will increase at next loop
    # for loop increases j every time we add (i, j) to row
    # until it reaches value of num
    row = [(i, j) for j in range(num)]
    #  append row list to groups list
    groups_to_check.append(row)

  # same thing as before, but i increases and j stays th same
  for j in range(num):
    column = [(i, j) for i in range(num)]
    groups_to_check.append(column)

  # positive diagonal quite simple to understand
  diagonal_1 = [(i, i) for i in range(num)]
  groups_to_check.append(diagonal_1)

  # negative diagonal: x coordinate increases with loop
  # y coordinate equals num - 1 - current value of x coordinate
  # example: num = 4
  # i == 0 -> (0, 4 - 1 - 0) -> (0, 3)
  # i == 1 -> (1, 4 - 1 - 1) -> (1, 2)
  # i == 2 -> (2, 4 - 1 - 2) -> (2, 1)
  # i == 3 -> (3, 4 - 1 - 3) -> (3, 0)
  # remmeber: range(num) num is not included in range
  diagonal_2 = [(j, num - 1 - j) for j in range(num)]
  groups_to_check.append(diagonal_2)
  return groups_to_check


def is_game_over(board, num):
  groups_to_check = create_groups_to_check(num)
  # We go through our groups
  for group in groups_to_check:
    # If any of them are empty, they're clearly not a
    # winning row, so we skip them.
    # * similar to spread operator in JS
    if is_group_complete(board, *group):
      if are_all_cells_the_same(board, *group):
        return True # We found a winning row!
        # Note that return also stops the function
  # all checks that ". is not in any row that are part of board"
  if all("." not in row for row in board):

    print("It's a draw!")
    return True 
  return False # If we get here, we didn't find a winning row

# And test it out:

print("Game time!")
play_game(3)
