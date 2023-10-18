import turtle

class Grid(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()

        self.win_positions = [
            [0,1,2,3],
            [4,5,6,7],
            [8,9,10,11],
            [12,13,14,None]
        ]

        self.curr_positions = [
            [2,1,4,3],
            [0,7,None,6],
            [11,9,10,8],
            [14,13,12,5]
        ]

        self.void_pos = self.get_void_pos()

    def get_void_pos(self):
        for row_i in range(len(self.curr_positions)):
            for col_j in range(len(self.curr_positions[row_i])):
                curr_pos = self.curr_positions[row_i][col_j]
                if curr_pos == None:
                    return (row_i, col_j)
        return None

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
        step = 50
        for row_i in range(len(self.curr_positions)):
            for col_j in range(len(self.curr_positions[row_i])):
                self.setpos(step * col_j, -step * row_i)
                cell_text = self.curr_positions[row_i][col_j]
                if cell_text == None:
                    cell_text = '[ ]'
                self.write(f'{cell_text}', align="center", font=('Arial', 14, 'bold'))
