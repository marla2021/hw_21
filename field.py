from terrain import Wall, Terrain, Trap


class Cell:
    def __init__(self, obj):
        self.obj = obj

    def get_object(self):
        return self.obj

    def set_object(self, obj):
        self.obj = obj


class Field:
    def __init__(self, field, cols, rows, Unit):
        self.field = field
        self.unit = Unit
        self.cols = cols
        self.rows = rows

    def cell(self, x, y):
        return self.field[x][y]

    def move_unit_up(self):
        x, y = self.unit.get_coordinates()
        if Terrain(terrain="wall", walkable=False):
            self.unit.set_coordinates(x=x, y=y)
        else:
            self.unit.set_coordinates(x=x, y=y-1)

    def move_unit_down(self):
        x, y = self.unit.get_coordinates()
        if Terrain(terrain="wall", walkable=False):
            self.unit.set_coordinates(x=x, y=y)
        else:
            self.unit.set_coordinates(x=x, y=y + 1)

    def move_unit_right(self):
        x, y = self.unit.get_coordinates()
        if Terrain(terrain="wall", walkable=False):
            self.unit.set_coordinates(x=x, y=y)
        else:
            self.unit.set_coordinates(x=x+1, y=y)

    def move_unit_left(self):
        x, y = self.unit.get_coordinates()
        if Terrain(terrain="wall", walkable=False):
            self.unit.set_coordinates(x=x, y=y)
        else:
            self.unit.set_coordinates(x=x-1, y=y)

    def get_field(self):
        return self.field

    def get_cols(self):
        return self.cols

    def get_rows(self):
        return self.rows

