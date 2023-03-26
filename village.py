class Building():
    
    def __init__(self, HP):
        self.HP = HP
        self.totalHP = HP

class Cannon(Building):
    
    xy = ()
    
    def __init__(self, cannon_number, range, damage, HP):
        self.cannon_number = cannon_number
        self.range = range
        self.damage = damage
        self.HP = HP
        self.totalHP = HP
        
class Wizard_Tower(Building):
    
    xy = ()
    x_y = ()
    xy_ = ()
    x_y_ = ()
    
    def __init__(self, wizard_tower_number, range, damage, area, HP):
        self.wizard_tower_number = wizard_tower_number
        self.range = range
        self.damage = damage
        self.area = area
        self.HP = HP
        self.totalHP = HP

class Hut(Building):
    
    xy = ()
    x_y = ()
    xy_ = ()
    x_y_ = ()
    
    def __init__(self, hut_number, HP):
        self.hut_number = hut_number
        self.HP = HP
        self.totalHP = HP

class Town_Hall(Building):
    
    def __init__(self, size_length, size_breadth, HP):
        if (size_length % 2):
            self.size_length = size_length + 1
        else:
            self.size_length = size_length
        if (size_breadth % 2):
                self.size_breadth = size_breadth + 1
        else:
            self.size_breadth = size_breadth
        self.HP = HP
        self.totalHP = HP
    
class Village():
    
    def __init__(self, town_name, size_length, size_breadth):
        self.town_name = town_name
        if (size_length % 2):
            self.size_length = size_length + 1
        else:
            self.size_length = size_length
        if (size_breadth % 2):
                self.size_breadth = size_breadth + 1
        else:
            self.size_breadth = size_breadth