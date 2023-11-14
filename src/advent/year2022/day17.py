WIDTH = 7
BAR_SHAPE = [(0, 0), (1, 0), (2, 0), (3, 0)]
L_SHAPE = [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]
CROSS_SHAPE = [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)]
I_SHAPE = [(0, 0), (0, 1), (0, 2), (0, 3)]
SQUARE_SHAPE = [(0, 0), (1, 0), (0, 1), (1, 1)]
FIGURES = [BAR_SHAPE, CROSS_SHAPE, L_SHAPE, I_SHAPE, SQUARE_SHAPE]


class Piece:
    def __init__(self, board, coords: list[tuple[int, int]]):
        self.board = board
        self.pos = (2, self.board.max_height + 3)
        self._coords = coords

    def absolute_coords(self):
        p = self.pos
        return [(b[0] + p[0], b[1] + p[1]) for b in self._coords]

    def move_down(self):
        self.pos = (self.pos[0], self.pos[1] - 1)

    def can_move_down(self):
        original_pos = self.pos
        self.move_down()
        rv = True
        for x, y in self.absolute_coords():
            if self.board.get_val(x, y):
                rv = False
                break
        self.pos = original_pos
        return rv

    def finish(self):
        self.board.setvals(self.absolute_coords())
        # self._coords = []


class Board:
    def __init__(self):
        self.width = WIDTH
        self.max_height = 0
        self.grid = []

    def get_val(self, x, y):
        if y < 0:
            return True
        elif y >= len(self.grid):
            return False
        else:
            return self.grid[y][x]

    def setvals(self, coords: list[tuple[int, int]]):
        max_height = max(coords, key=lambda x: x[1])[1]
        while max_height >= len(self.grid):
            self.grid.append([False] * self.width)
        for x, y in coords:
            self.grid[y][x] = True
        self.max_height = max(self.max_height, max_height)

    def get_row(self, i):
        if i < 0:
            rv = [True] * self.width
        elif i >= len(self.grid):
            rv = [False] * self.width
        else:
            rv = self.grid[i][::]
        return rv


def print_board(board: Board, piece: Piece):
    s = ''
    piece_blocks = piece.absolute_coords()
    key = lambda x: x[1]
    min_block, max_block = min(piece_blocks, key=key), max(piece_blocks, key=key)
    visible_max = max(max_block[1] + 1, len(board.grid) + 3)
    for i in range(visible_max, -1, -1):
        row = ['.#'[c] for c in board.get_row(i)]
        if min_block[1] <= i <=max_block[1]:
            for block in filter(lambda x: x[1] == i, piece_blocks):
                row[block[0]] = '@'
        row_str = ''.join(row)
        s += f'|{row_str}|\n'
    s += f'+{"-"*WIDTH}+\n'
    return s


if __name__ == '__main__':
    board = Board()
    for _ in range(3):
        for fig in FIGURES:
            piece = Piece(board=board, coords=fig)
            while piece.can_move_down():
                piece.move_down()
                s = print_board(board, piece)
                print(s)
            piece.finish()
            s = print_board(board, piece)
            print(s)
