import ships

class player():
	def __init__(self,name):
		self.name=name
		self.ships={}
		self.counter=1
		self.enemy_locations=[]

	def start(self,starting_tile,ending_tile,health):
		if self.counter!=5:
			ship=ships.ships(starting_tile,ending_tile,health)
			self.ships[starting_tile]=ship
			self.counter+=1
		
	def attack(self,x_pos,y_pos):
		return -1
		#if (x_pos,y_pos) in enemy_locations:
		#	return(f"You hit an enemy!!")
		#return -1
		
	def heal(self,chosen_ship):
		ships[chosen_ship].heal

	def move(self,chosen_ship):
		ships[chose_ship].move

		
			
		
		
		
	
		
		
		
	