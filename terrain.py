from hero import Unit


class Terrain:
    def __init__(self, terrain, walkable, unit=Unit):
        self.terrain = terrain
        self.walkable = walkable
        self.unit = unit

    def is_walkable(self):
        return self.walkable

    def get_terrain(self):
        return self.terrain


class Key(Terrain):
    def __init__(self):
        super().__init__(terrain='key', walkable=True)

    def step_on(self):
        if self.unit.has_key():
            self.walkable = True


class Door(Terrain):
    def __init__(self):
        super().__init__(terrain='door', walkable=False)

    def step_on(self):
        if self.unit.has_key():
            self.walkable = True


class Trap(Terrain):
    def __init__(self, damage):
        self.damage = damage
        super().__init__(terrain='trap', walkable=True)

    def step_on(self):
        self.unit.get_damage(self.damage)

class Grass(Terrain):
    def __init__(self):
        super().__init__(terrain='grass', walkable=True)


class Wall(Terrain):
    def __init__(self):
        super().__init__(terrain='wall', walkable=False)
