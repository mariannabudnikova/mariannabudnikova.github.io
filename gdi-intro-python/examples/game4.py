#!/usr/bin/python
"""
This is a simple text based game that displays a board and obtains input from
the command line.


In this stage, the following is already implemented:
    * Loads a text file as the playing board
    * Displays the board and obtains input in a loop until a user types `quit`
    * Displays the player on the board
    * Moves the player on the board when the user types input such as "up"
    * Prevents the player from walking through walls
    * Makes it so the player can pick up the item (Item looks like ^)

Implement the following:
    * Make it so the player can use the key to open the door.
"""
from __future__ import print_function


DEFAULT_BOARD = 'board.dat'
PLAYER_X_START = 5
PLAYER_Y_START = 5

NON_SOLIDS = ['^', '$', 'o', ' ', 'f']


def print_char(char):
    """Print only the given `char` without a newline"""
    print(char, end='')


def get_input():
    try:
        move = raw_input("Choose a direction (Type `quit` to quit): ")
    except NameError:
        # Python3
        move = input("Choose a direction (Type `quit` to quit): ")
    return move


def load_board(filename):
    """
    Given a filename of a text file, load the characters therein and return as
    a list of character lists. E.g.:

    A file containing:
        xox
        oxx
        oxo

    would return:
        [
            ['x', 'o', 'x'],
            ['o', 'x', 'x'],
            ['o', 'x', 'o'],
        ]
    """
    board_file = open(filename)
    board_tiles = []
    for line in board_file.readlines():
        board_tiles.append([char for char in line.strip()])
    board_file.close()
    return board_tiles


def get_tile(board, x, y):
    """
    Returns the character for a give, `x` and `y` position of the given `board`
    """
    return board[y][x]


def display(board, player_x, player_y, player_inventory):
    """
    Display the given `board` and the player at the position `player_x` and
    `player_y`
    """
    for y, row in enumerate(board):
        for x, tile in enumerate(row):
            if x == player_x and y == player_y:
                print_char('@')
            else:
                print_char(tile)
        print_char('\n')


def main():
    board = load_board(DEFAULT_BOARD)
    player_x = PLAYER_X_START
    player_y = PLAYER_Y_START
    player_inventory = []
    while True:
        display(board, player_x, player_y, player_inventory)
        print('Player inventory:')
        for item in player_inventory:
            print(item)
        move = get_input()
        if move == 'quit':
            return True
        if move == 'up':
            # FIXME: Add a check that allows the player to pass through a door
            # if they have a key.
            if get_tile(board, player_x, player_y - 1) in NON_SOLIDS:
                player_y -= 1
        if move == 'down':
            # FIXME: Add a check that allows the player to pass through a door
            # if they have a key.
            if get_tile(board, player_x, player_y + 1) in NON_SOLIDS:
                player_y += 1
        if move == 'left':
            if get_tile(board, player_x - 1, player_y) in NON_SOLIDS:
                player_x -= 1
        if move == 'right':
            if get_tile(board, player_x + 1, player_y) in NON_SOLIDS:
                player_x += 1
        current_tile = get_tile(board, player_x, player_y)
        if current_tile in ['^', 'f'] and current_tile not in player_inventory:
            board[player_y][player_x] = ' '
            player_inventory.append(current_tile)


if __name__ == '__main__':
    main()
