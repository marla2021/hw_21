class Unit:
    def __init__(self, hp, got_key, coord):
        self.hp = hp
        self.got_key = got_key
        self.coord = coord
        self.escaped = False

    def has_key(self):
         # bool — проверяет, есть ли у данного юнита ключ.
         pass

    def set_key(self):
        # — ставит маркер got_key в True
        pass

    def has_escaped(self):
        # → bool — проверяет, удалось ли сбежать.
        pass

    def is_alive(self):
        # → bool — проверяет, есть ли еще у юнита положительное количество хит-поинтов.
        pass

    def get_damage(self):
        # — обрабатывает входящий урон с учетом текущего параметра защиты.
        # Если юнит умирает после атаки, должно быть выброшено исключение UnitDied.
        pass

    def set_coordinates(self, x, y):
        # — устанавливает координаты юнита.
        pass

    def get_coordinates(self):
        # → tuple — возвращает координаты юнита.
        pass

    def has_position(self):
        # bool - проверяет в этих ли координатах установлен юнит
        pass

class Ghost(Unit):
    def __init__(self, name, got_key, hp, coord, escape):
        super().__init__(hp, got_key, coord)
        self.name = name



