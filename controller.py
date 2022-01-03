from field import Cell
from hero import Ghost, Unit
from terrain import Grass, Wall
from field import Field


class GameController:
    def __init__(self):
        self.mapping = {
	    'Wall': '🔲',
        'Grass': '⬜️',
	    'Ghost': '👻',
       	'Key': '🗝',
     	'Door': '🚪',
    	'Trap': '💀',
                       }
        self.game_on = True
        self.hero = Unit
        self.field = Field
        self.col = Field
        self.row = Field

    def make_field(self):
        fields = []
        self.col = self.field.get_cols()
        self.row = self.field.get_rows()
        for y in range (self.col):
            field = []
            for x in range(self.row):
                cell = self.field.cell(x=x,y=y)
                cell_type = cell.get_object().get_terrain()
                if self.hero.get_coordinates(x,y):
                    field.append(self.mapping.get(cell_type,"ghost"))
                else:
                    field.append(self.mapping.get(cell_type,"grass"))
            field.append("".join(field))
        return "\n".join(fields)



    def play(self):
        self.ghost = Ghost(100)
        while self.game_on and not self.ghost.escaped:
            print(self.make_field())
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