class Cell:
    def __init__(self, obj):
        self.obj = obj

    def get_object(self):
        return self.obj

    def set_object(self, obj):
        self.obj = obj

class Field:
    def __init__(self, field, unit, cols, rows):
        self.field = field
        self.unit = unit
        self.cols = cols
        self.rows = rows

    def cell(self, x, y):
        # — метод, возвращающий объект находящийся по данным координатам;
        pass
    def move_unit_up(self):
        # — метод, смещающий юнита вверх;
        pass
    def move_unit_down(self):
        # — метод, смещающий юнита вниз;
        pass
    def move_unit_right(self):
        # — метод, смещающий юнита вправо;
        pass
    def move_unit_left(self):
        # — метод, смещающий юнита влево;
        pass
    def get_field(self):
        # — возвращает свойство field.
        pass
    def get_cols(self):
        # - возвращает количество столбцов в поле.
        pass
    def get_rows(self):
        # - возвращает количество строк в поле
        pass