import random
import ast
import player_class
class game:
	def __init__(self,id):
		self.player1=player_class.player("p1")
		self.player2=player_class.player("p2")
		self.player1_game_dic={}
		self.player2_game_dic={}
		self.player2_ships={}
		self.player1_ships={}
		
	def fill_up_grid(self,start_pos,end_pos,my_dic,pos_dic):
		start=start_pos[1]
		s=start_pos[0]
		end=end_pos[1]
		while start < end:
			if my_dic[(s,start)]==1:
				return ("constraint")

				
			my_dic[(s,start)]=1
			pos_dic[(s,start)]=start_pos
			start+=1
		return pos_dic
			
			
		
	def initiate_grid_with_ships(self,game_dic):
		#t_list=[(1,1),(1,5),(3,1),(3,3),(4,1),(4,3),(5,1),(5,2)]
		game_dic={}
		for x in range(1,9):
			for y in range(1,9):
				self.player1_game_dic[(x,y)]=0
				self.player2_game_dic[(x,y)]=0
		"""for x in range(0,len(t_list)-1):
			self.player1.start(t_list[x],t_list[x+1])
			
			self.player2.start(t_list[x],t_list[x+1])
			self.fill_up_grid(t_list[x],t_list[x+1]) """

	def play(self):
		T=True
		t=1
		counter=0
		current_dic=self.player1_game_dic
		current_player=self.player1
		pos_dic=self.player1_ships
		
		self.initiate_grid_with_ships(self.player1_game_dic)
		self.initiate_grid_with_ships(self.player2_game_dic)
		while T:
			counter+=1
			user_input=input(f"player {t} goes for now")
			init_pos=ast.literal_eval(user_input)
			user_input=int(input("size"))
			end_pos=(init_pos[0],init_pos[1]+user_input+1)
			if end_pos[0]<1 or end_pos[0]> 7 or end_pos[1]<1 or end_pos[1]> 7:
				print(f"invalid position")
			else:
				if t==1:
					self.fill_up_grid(init_pos,end_pos,self.player1_game_dic,self.player1_ships)
					self.player1.start(init_pos,end_pos,user_input+1)
					t=2
				elif t==2:
					self.fill_up_grid(init_pos,end_pos,self.player2_game_dic,self.player2_ships)
					self.player2.start(init_pos,end_pos,user_input+1)
					t=1
				
				

			if counter==10:
				T=False
		T=True
		print(f"p1 ships are {self.player1.ships.keys()}")
		print(f"p2 shps are {self.player2.ships.keys()}")
		
		t=1
		attacker=self.player1
		attacker_dic=	self.player1_game_dic
		attacker_ships=self.player1_ships
		defender=self.player2
		defender_dic=	self.player2_game_dic
		defender_ships=self.player2_ships
		print(f"current dics are {defender_dic}")
		print(f"current dics are{attacker_dic}")
		print(f"current dics are{defender_ships}")
		print(f"current dics are{attacker_ships}")
		tounter=0
		prev_tounter=10000
		while T:
			tounter+=1
			option={1:"Attack",2:"Heal",3:"Move"}
			user_input=int(input(f"player {t} turn now 1:{option[1]},2:{option[2]},3:{option[3]}"))
			if user_input < 2:
				user_input=input("enter co-ordinates")
				attack_pos=ast.literal_eval(user_input)
				a=attacker.attack(attack_pos[0],attack_pos[1])
				if defender_dic[attack_pos]==1:
					defender.ships[defender_ships[attack_pos]].health-=1
					print(f"You hit something")
				else:
					defender.restrictions.append(attack_pos)
					prev_tounter=tounter
					
					if defender.ships[defender_ships[attack_pos]].health==0:
						defender.ships.pop(defender_ships[attack_pos],None)
						return (f"player{t} wins!!!")
			
			elif user_input >2:
				chosen_ship=input("which ship?")
				chosen_ship=ast.literal_eval(chosen_ship)
				direction=input("please enter D,U,L,R")
				attacker.move(chosen_ship,direction)
				new_start_tile=attacker.ships[chosen_ship].starting_tile
				new_end_tile=attacker.ships[chosen_ship].ending_tile
				new_health=attacker.ships[chosen_ship].health
				attacker.ships.pop(chosen_ship,None)
				attacker.start(new_start_tile,new_end_tile,new_health)
			else:
				chosen_ship=input("which ship?")
				chosen_ship=ast.literal_eval(chosen_ship)
				attacker.ships[chosen_ship].health+=1
			if tounter >= prev_tounter+4:
					defender.restrictions.pop(0)
	
			if len(defender.ships)==0:
				return(f"player{t} wins")
			
			
			
			if t==1:
				t=2
				attacker_dic=self.player2_game_dic
				defender_dic=self.player1_game_dic
			elif t==2:
				attacker_dic=self.player1_game_dic
				defender_dic=self.player2_game_dic
				t=1
		
		
#p1=player_class.player("Joe")
#p2=player_class.player("Jill")
id=420
g=game(id)
#ans=g.fill_up_grid((1,1),(1,5),{},{})
#print(ans)
g.play()
print("uwu")
		
			
			
		