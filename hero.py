from exeptions import UnitDied


class Unit:
    def __init__(self, hp):
        self.hp = hp
        self.got_key = False
        self.coord = (0,0)
        self.escaped = False

    def has_key(self):
        return self.got_key

    def set_key(self):
        self.got_key = True

    def has_escaped(self):
        return self.escaped

    def is_alive(self):
        if self.hp <= 0:
            raise UnitDied()
        return True

    def get_damage(self, damage):
        # — обрабатывает входящий урон с учетом текущего параметра защиты.
        # Если юнит умирает после атаки, должно быть выброшено исключение UnitDied.
        if damage > self.hp:
            self.hp -= (damage - self.hp)
        self.is_alive()

    def set_coordinates(self, x, y):
        self.coord = (x, y)

    def get_coordinates(self):
        return self.coord

    def has_position(self):
        # bool - проверяет в этих ли координатах установлен юнит
        pass

class Ghost(Unit):
    def __init__(self, hp, name):
        super().__init__(hp)
        self.name = name



