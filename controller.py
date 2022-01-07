from field import Cell
from hero import Ghost, Unit
from terrain import Grass, Wall, Key, Door, Trap
from field import Field


class GameController:
    def __init__(self):
        self.mapping = {
	    'wall': '🔲',
        'grass': '⬜️',
	    'ghost': '👻',
       	'key': '🗝',
     	'door': '🚪',
    	'trap': '💀',
                       }
        self.game_on = True

        self.hero = Unit
        self.field = None
        self.col = 0
        self.row = 0
        self.wall = Wall
        self.key =Key

    def make_field(self):
        fields = []

            #fields = []
        with open('fields_schema.txt','r') as f:
            arr = f.readlines()
        row = len(arr)
        col = len(arr[0])
        hero = None
        for line_n, line in enumerate(arr):
            field_line = []
            for item_n, item in enumerate(line.strip("\n")):
                if item == "W":
                    field_line.append(Cell(Wall()))
                if item == "g":
                    field_line.append(Cell(Grass()))
                if item == "G":
                    field_line.append(Cell(Grass()))
                    self.hero = Ghost(item_n, line_n,item_n)
                if item == "K":
                    field_line.append(Cell(Key()))
                if item == "D":
                    field_line.append(Cell(Door()))
                if item == "T":
                    field_line.append(Cell(Trap(10)))
            fields.append(field_line)
            self.field = Field(fields, col,row, self.hero)

    def _draw_field(self):
        for y, line in enumerate(self.field.get_field()):
            s = ""
            for x, item in enumerate(line):
                if self.hero.has_position(x, y):
                    s += self.mapping["ghost"]
                else:
                    s += self.mapping[item.get_object().get_terrain()]
            print(s)



    def play(self):
        self.make_field()
        while self.game_on and not self.hero.escaped:
            print(self._draw_field())
            command = input()
            if command == "w":
                self.field.move_unit_up()
            if command == "a":
                self.field.move_unit_left()
            if command == "d":
                self.field.move_unit_right()
            if command == "s":
                self.field.move_unit_down()
            if command in ["stop", "exit"]:
                self.game_on = False