#!/usr/bin/env python3

"""
Sie befinden sich in einem 3D Labyrinth und wollen auf schnellstem Weg nach Hause.
Das Labyrinth besteht aus einheitlichen Quadern aus Stein oder Luft.
Sie benötigen 1 Minute, um einen Schritt nach Norden, Süden, Westen, Osten, Oben oder Unten zu gehen.
Diagonale Fortbewegung ist nicht möglich. Ausserdem ist das Labyrinth an allen Seiten von Steinen umgeben.

Ist es möglich zu entkommen, und falls ja, wie lange sind Sie mindestens unterwegs?
"""
from collections import deque


class Position(object):
    def __init__(self, level=None, row=None, column=None):
        self.level = level
        self.row = row
        self.column = column

    def set_coordinates(self, level, row, column):
        self.level = level
        self.row = row
        self.column = column

    def __str__(self):
        return f"l:{self.level}r:{self.row}c:{self.column}"

    def __repr__(self):
        return f"Position(level={self.level}, row={self.row}, column={self.column})"

    def __eq__(self, other):
        return self.level == other.level and self.row == other.row and self.column == other.column


class Labyrinth(object):
    def __init__(self, start, end, body):
        self.start_position = start
        self.end_position = end
        self.body = body

    def __is_valid_position(self, position):
        if not 0 <= position.level < len(self.body):
            return False
        if not 0 <= position.row < len(self.body[0]):
            return False
        if not 0 <= position.column < len(self.body[0][0]):
            return False
        return True

    def __is_not_stone(self, position):
        level, row, col = position.level, position.row, position.column
        return self.body[level][row][col] != "#"


    def solve(self):
        """BFS Loesung (O(level*rows*columns))"""
        minutes = 0
        visited = set()
        queue = deque()
        queue.append((self.start_position, minutes))

        while queue:
            current_position, minutes = queue.popleft()
            visited.add(str(current_position))

            if current_position == self.end_position:
                return minutes, True

            for direction in [(0, 0, -1), (0, 0, 1), (0, -1, 0), (0, 1, 0), (-1, 0, 0), (1, 0, 0)]:
                level = current_position.level + direction[0]
                row = current_position.row + direction[1]
                col = current_position.column + direction[2]
                next_position = Position(level, row, col)

                if self.__is_valid_position(next_position) and self.__is_not_stone(next_position):
                    if str(next_position) not in visited:
                        queue.append((next_position, minutes + 1))

        return -1, False


def read_level(rows):
    return [list(input()) for _ in range(rows)]


def find_endpoint(labyrinth_levels, endpoint_char):
    fake_coordinate = -1 * ord(endpoint_char)
    position = Position(fake_coordinate, fake_coordinate, fake_coordinate)

    for l_idx, level in enumerate(labyrinth_levels):
        for r_idx, row in enumerate(level):
            for c_idx, col in enumerate(row):
                if col.upper() == endpoint_char.upper():
                    position.set_coordinates(l_idx, r_idx, c_idx)
                    return position
    return position


def main():
    labyrinths = []
    levels, rows, _ = map(int, input().split())

    while levels != 0: # 0 levels => no labyrinth
        labyrinth_levels = []
        for _ in range(levels):
            labyrinth_levels.append(read_level(rows))
            input()
        start = find_endpoint(labyrinth_levels, 'S')
        end = find_endpoint(labyrinth_levels, 'E')
        labyrinths.append(Labyrinth(start, end, labyrinth_levels))

        levels, rows, _ = map(int, input().split())

    for lab in labyrinths:
        steps, solved = lab.solve()
        if solved:
            print(f"Entkommen in {steps} Minute(n)!")
        else:
            print("Gefangen :-(")


if __name__ == "__main__":
    main()
