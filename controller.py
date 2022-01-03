from field import Cell
from hero import Ghost
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
        self.hero = None
        self.field = None

    def make_field(self, levelstring):
        cell1 = Cell(Grass())
        cell2 = Cell(Grass())
        cell3 = Cell(Wall())
        field =[cell1, cell2, cell3]
        self.field = Field()
        self.field.get_field(field)

    def play(self):
        self.ghost = Ghost(name, got_key, hp, coord, escape)
        while self.game_on and not self.ghost.escaped:
            command = input()
            if command == "a":
                self.field.move_unit_up()