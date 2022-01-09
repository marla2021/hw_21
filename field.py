from terrain import Terrain, Wall


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

    def unit_move(self, x1, y1):
        x, y = self.unit.get_coordinates()
        if self.cell(y1, x1).get_object().get_terrain() == "trap":
            print('Вам нанесли урон')
            self.unit.set_coordinates(x=x1, y=y1)
        elif self.cell(y1, x1).get_object().get_terrain() == "key":
            print('Теперь у вас есть ключ! Идите к двери!')
            self.unit.set_coordinates(x=x1, y=y1)
            self.unit.set_key()
        elif self.cell(y1, x1).get_object().get_terrain() == "door":
            self.unit.set_coordinates(x=x1, y=y1)
            if self.unit.got_key():
                print("Вы переходите на следующий уровень!")
                self.unit.has_escaped()
        else:
            self.unit.set_coordinates(x=x1, y=y1)
        if self.cell(y1, x1).get_object().is_walkable():
            self.unit.set_coordinates(x=x1, y=y1)
        else:
            self.unit.set_coordinates(x=x, y=y)
            print('На эту ячейку перемещаться нельзя')

    def move_unit_up(self):
        x, y = self.unit.get_coordinates()
        self.unit_move(x1=x, y1=y-1)

    def move_unit_down(self):
        x, y = self.unit.get_coordinates()
        self.unit_move(x1=x, y1=y+1)

    def move_unit_right(self):
        x, y = self.unit.get_coordinates()
        self.unit_move(x1=x+1, y1=y)

    def move_unit_left(self):
        x, y = self.unit.get_coordinates()
        self.unit_move(x1=x-1, y1=y)

    def get_field(self):
        return self.field

    def get_cols(self):
        return self.cols

    def get_rows(self):
        return self.rows

