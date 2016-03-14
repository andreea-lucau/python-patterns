"""Sample usage of the Commnad pattern.

This is a maze game and the commands are the moves that the player can execute.
"""
#!/usr/bin/env python
# pylint: disable=missing-docstring,too-few-public-methods
import os
import sys
import termios
import tty

LEFT = 67
RIGHT = 68
UP = 65
DOWN = 66
QUIT = 113

class Command(object):
    def __init__(self, labyrinth):
        self.labyrinth = labyrinth

    def execute(self):
        pass

    def __call__(self):
        self.execute()


class MoveLeft(Command):
    def execute(self):
        position = self.labyrinth.position
        if self.labyrinth.is_valid_move(position[0], position[1] + 1):
            self.labyrinth.update_position(position[0], position[1] + 1)


class MoveRight(Command):
    def execute(self):
        position = self.labyrinth.position
        if self.labyrinth.is_valid_move(position[0], position[1] - 1):
            self.labyrinth.update_position(position[0], position[1] - 1)


class MoveUp(Command):
    def execute(self):
        position = self.labyrinth.position
        if self.labyrinth.is_valid_move(position[0] - 1, position[1]):
            self.labyrinth.update_position(position[0] - 1, position[1])


class MoveDown(Command):
    def execute(self):
        position = self.labyrinth.position
        if self.labyrinth.is_valid_move(position[0] + 1, position[1]):
            self.labyrinth.update_position(position[0] + 1, position[1])


class Quit(Command):
    def execute(self):
        sys.exit()


class Labyrinth(object):

    def __init__(self, filename):
        self.cells = []
        for line in open(filename):
            cells_line = map(int, line.split())
            self.cells.append(cells_line)
        self.position = (len(self.cells) - 2, 0)
        self.end = (1, len(self.cells[0]) - 1)

    def is_valid_move(self, line, column):
        if line >= len(self.cells):
            return False

        if column >= len(self.cells[0]):
            return False

        if self.cells[line][column] == 1:
            return False

        return True

    def update_position(self, line, column):
        self.position = (line, column)

    def display(self):
        for i, line in enumerate(self.cells):
            for j, cell in enumerate(line):
                if (i, j) == self.position:
                    print '*',
                elif cell == 1:
                    print unichr(0x2585),
                else:
                    print ' ',
            print
        print "Left, right, up, down or 'q'"

    def is_solved(self):
        return self.position == self.end


def read_command():
    stdin_fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(stdin_fd)
    try:
        tty.setraw(sys.stdin.fileno())
        return sys.stdin.read(1)
    finally:
        termios.tcsetattr(stdin_fd, termios.TCSADRAIN, old_settings)


def play_game():
    labyrinth = Labyrinth("labyrinth.txt")

    commands = {
        LEFT: MoveLeft(labyrinth),
        RIGHT: MoveRight(labyrinth),
        UP: MoveUp(labyrinth),
        DOWN: MoveDown(labyrinth),
        QUIT: Quit(labyrinth)
    }

    while not labyrinth.is_solved():
        os.system('clear')
        labyrinth.display()
        input_command = read_command()
        command = commands.get(ord(input_command))
        if command:
            command()

    os.system('clear')
    labyrinth.display()

    print "Victory!!!!!! Press any key to exit"
    input_command = read_command()


if __name__ == "__main__":
    play_game()
