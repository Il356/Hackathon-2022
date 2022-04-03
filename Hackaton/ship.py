class Ship():
    def __init__(self, length, orientation, in_repair = False, is_extended = False):
        self.length = length
        self.orientation = orientation
        
        self.health = length
        self.in_repair = False
        self.is_extended = False