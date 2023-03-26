class Monarch():
    
    def __init__(self, damage, HP, movement_speed):
        self.damage = damage
        self.movement_speed = movement_speed
        self.HP = HP
        self.totalHP = HP

class King(Monarch):
    
    def __init__(self, damage, HP, movement_speed):
        self.damage = damage
        self.movement_speed = movement_speed
        self.HP = HP
        self.totalHP = HP
        
class Queen(Monarch):
    
    def __init__(self, damage, range, center_distance, HP, movement_speed):
        self.damage = damage
        self.movement_speed = movement_speed
        self.range = range
        self.center_distance = center_distance
        self.HP = HP
        self.totalHP = HP
        
class Troop():
    
    def __init__(self, damage, HP, movement_speed):
        self.damage = damage
        self.movement_speed = movement_speed
        self.HP = HP
        self.totalHP = HP

class Barbarian(Troop):
    
    def __init__(self, barbarian_number, damage, HP, movement_speed):
        self.barbarian_number = barbarian_number
        self.damage = damage
        self.movement_speed = movement_speed
        self.HP = HP
        self.totalHP = HP
        
class Archer(Troop):
    
    def __init__(self, archer_number, damage, range, HP, movement_speed):
        self.archer_number = archer_number
        self.damage = damage
        self.range = range
        self.movement_speed = movement_speed
        self.HP = HP
        self.totalHP = HP
        
class Balloon(Troop):
    
    def __init__(self, balloon_number, damage, range, HP, movement_speed):
        self.balloon_number = balloon_number
        self.damage = damage
        self.range = range
        self.movement_speed = movement_speed
        self.HP = HP
        self.totalHP = HP        

class Spawning_Point():
    
    def __init__(self, point_number, xy):
        self.point_number = point_number
        self.xy = xy 