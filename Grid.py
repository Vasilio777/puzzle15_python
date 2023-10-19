import turtle
import random

class Grid(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.rt(90) # to offset a text pos
        
        self.shape('assets/Cell_tile.gif')

        self.win_positions = [
            [0,1,2,3],
            [4,5,6,7],
            [8,9,10,11],
            [12,13,14,None]
        ]

        self.generate_positions()

    def generate_positions(self):
        self.curr_positions = []
        seq = list(range(15)) + [None]
        random.shuffle(seq)
        
        for i in range(0, 16, 4):
            row = seq[i:i+4]
            self.curr_positions.append(row)

        if not self.is_boustrophedon_odd():
            self.generate_positions()

        # Find the void position
        for i in range(4):
            if None in self.curr_positions[i]:
                self.void_pos = (i, self.curr_positions[i].index(None))
                break

    def is_boustrophedon_odd(self) -> bool:
        seq = []
        for i in range(len(self.curr_positions)):
            for j in range(len(self.curr_positions[i])):
                el = self.curr_positions[i][j] if i % 2 == 0 else self.curr_positions[i][::-1][j]
                if el is not None:
                    seq.append(el)

        count_greater = sum(seq[i] > seq[j] for i in range(len(seq)) for j in range(i + 1, len(seq)))
        return count_greater % 2 != 0

    def up(self):
        self.move(1, 0)

    def down(self):
        self.move(-1, 0)

    def left(self):
        self.move(0, 1)

    def right(self):
        self.move(0, -1)

    def move(self, x_change, y_change):
        new_x = self.void_pos[0] + x_change
        new_y = self.void_pos[1] + y_change

        if 0 <= new_x < 4 and 0 <= new_y < 4:
            self.swap_void_with_target(new_x, new_y)

    def swap_void_with_target(self, x, y):
        self.curr_positions[self.void_pos[0]][self.void_pos[1]] = self.curr_positions[x][y]
        self.curr_positions[x][y] = None 
        self.void_pos = (x, y)

    def render_tick(self):
        self.clear()
        step = 140
        offset = len(self.curr_positions)/2 * step - step/2

        for row_i in range(len(self.curr_positions)):
            for col_j in range(len(self.curr_positions[row_i])):
                self.setpos(step * col_j - offset, -step * row_i + offset)
                cell_text = self.curr_positions[row_i][col_j]
                if cell_text == None:
                    cell_text = ''
                else:
                    cell_text += 1

                self.stamp()
                self.forward(30)
                self.write(f'{cell_text}', align="center", font=('Arial', 40, 'bold'))
