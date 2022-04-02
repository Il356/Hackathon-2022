class ships():
	def __init__(self,starting_tile,ending_tile,health):
		self.starting_tile=starting_tile
		self.ending_tile=ending_tile
		self.health=health
		self.original_health=health
		self.being_repaired=False
		self.grid_limit=8
		self.moves={"D":(0,-1),"U":(0,1),"L":(-1,0),"R":(0,-1)}
		#(x,y)
		

	def heal(self):
		if self.being_repaired==False:
			if self.health < self.original_health:
				self.health+=1
				self.being_repaired=True
			else:
				return(f"You can't heal!!!")
		else:
			return(f"You can't heal!!")

	def got_hit(self):
		self.health-=1
		if self.health==0:
			return (f"Sunk!!")
		else:
			return(f"Got hit")

	def move(self,move_type):
		if move_type=="D" and starting_tile[1]==self.grid_limit or ending_tile[1]==self.grid_limit:
			return(f"Invalid move")

		elif move_type=="U" and starting_tile[1]==1 or ending_tile[1]==1:
			return(f"Invalid move")
		elif move_type=="L" and starting_tile[0]==1 or ending_tile[0]==1:
			return(f"Invalid move")
		elif move_type=="L" and starting_tile[0]==self.grid_limit or ending_tile[0]==self.grid_limit:
			return(f"Invalid move")
		else:
			print(self.starting_tile)
			self.starting_tile += moves[move_type]
			self.ending_tile+=moves[move_type]

	
			
		
		
		

	
		
		
	
			
			
