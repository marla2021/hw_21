from hero import Unit


class Cell:
    def __init__(self, obj):
        self.obj = obj

    def get_object(self):
        return self.obj

    def set_object(self, obj):
        self.obj = obj

class Field:
    def __init__(self, field, cols, rows):
        self.field = field
        self.unit = Unit
        self.cols = cols
        self.rows = rows

    def cell(self, x, y):
        # — метод, возвращающий объект находящийся по данным координатам;
        pass
    def move_unit_up(self,x,y):
        return self.unit.set_coordinates(Unit, x=x, y=y+1)

    def move_unit_down(self,x,y):
        return self.unit.set_coordinates(Unit, x=x, y=y-1)

    def move_unit_right(self,x,y):
        return self.unit.set_coordinates(Unit, x=x+1, y=y)

    def move_unit_left(self,x,y):
        return self.unit.set_coordinates(Unit, x=x-1, y=y)

    def get_field(self):
        # — возвращает свойство field.
        pass
    def get_cols(self):
        return self.cols == 10

    def get_rows(self):
        return self.rows == 10