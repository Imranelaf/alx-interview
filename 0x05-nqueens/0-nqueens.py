#!/usr/bin/python3

'''
This is a Python program that solves the N-Queens problem using backtracking.
The N-Queens problem is the problem of placing N chess queens on an N×N
chessboard so that no two queens attack each other.
'''

import sys


def solve_queens_problem(board_size):
    '''
    This function solves the N-Queens problem using backtracking.

    Parameters:
        board_size (int): The size of the board.

    Returns:
        list: A list of solutions. Each solution is a list of integers
        representing the column position of each queen in the corresponding
    '''

    def is_valid_position(pos, occupied_pos):
        '''
        This function checks if a position is valid for a queen.

        Parameters:
            pos (int): The position to check.
            occupied_pos (list): A list of integers representing the column
            position of each queen.

        Returns:
            bool: True if the position is valid, False otherwise.
        '''
        for index in range(len(occupied_pos)):
            if (
                occupied_pos[index] == pos or
                occupied_pos[index] - index == pos - len(occupied_pos) or
                occupied_pos[index] + index == pos + len(occupied_pos)
            ):
                return False
        return True

    def place_queens(board_size, index, occupied_pos, solutions):
        '''
        This function recursively places queens on the board.

        Parameters:
            board_size (int): The size of the board.
            index (int): The index of the current row.
            occupied_pos (list): A list of integers representing the column
            position of each queen.
            solutions (list): A list of solutions.

        Returns:
            None
        '''
        if index == board_size:
            solutions.append(occupied_pos[:])
            return

        for i in range(board_size):
            if is_valid_position(i, occupied_pos):
                occupied_pos.append(i)
                place_queens(board_size, index + 1, occupied_pos, solutions)
                occupied_pos.pop()

    sol_lst = []
    place_queens(board_size, 0, [], sol_lst)
    return sol_lst


def main():
    '''
    This is the main function.

    Parameters:
        None
    '''
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        brd_sze = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if brd_sze < 4:
        print("N must be at least 4")
        sys.exit(1)

    slts_list = solve_queens_problem(brd_sze)
    for sol in slts_list:
        print([[i, sol[i]] for i in range(len(sol))])


if __name__ == "__main__":
    main()
