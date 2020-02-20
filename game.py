import random

class Game:
    def __init__(self):
        self.player = Player("Nathan")
        self.cpu = CpuPlayer("STUPID ROBOT")
        self.die = Die()    
    
    def show_roll(self):
        print(f"Roll: {self.die.roll()}")
    
    def declare_winner(self): 
        if self.player.total_score > self.cpu.total_score:
            print("human wins!!!")
        else:
            print("robot wins!!!")

    def round(self):
        first_player_move = True
        while self.player.total_score < 100 and self.cpu.total_score < 100:
            if first_player_move == True:
                choice = input(f'{self.player}, do you want to (r)oll or (h)old? ')
                if choice == 'r':
                    roll = self.die.roll()
                    print(f"Roll: {roll}")
                    if roll == 1:
                        self.player.round_score = 0
                        print('PIG')
                        self.player.show_round_score()
                        first_player_move = False
                    else:
                        self.player.round_score += roll
                        # self.show_roll()  
                        self.player.show_round_score() 
                elif choice == 'h': 
                    self.player.total_score += self.player.round_score
                    self.player.show_total_score()
                    self.player.round_score = 0
                    first_player_move = False
            elif first_player_move == False:
                print((f'{self.cpu}, do you want to (r)oll or (h)old? '))
                while self.cpu.round_score < 20 and first_player_move == False:
                    roll = self.die.roll()
                    print(f"Roll: {roll}")
                    if roll == 1:
                        self.cpu.round_score = 0
                        print('PIG')
                        self.cpu.show_round_score()
                        first_player_move = True
                    else:
                        self.cpu.round_score += roll
                        # self.show_roll()  
                        self.cpu.show_round_score() 
                else: 
                    self.cpu.total_score += self.cpu.round_score
                    self.cpu.show_total_score()
                    self.cpu.round_score = 0
                    first_player_move = True
        else: 
            print("WE HAVE A WINNER!")
            self.declare_winner()

            
        
class Player:
    def __init__(self, name):
        self.name = name
        self.total_score = 0
        self.round_score = 0


    def __str__(self):
        return f'{self.name}'        

    def show_round_score(self):
        print(f'Round Score: {self.round_score}\n')

    def show_total_score(self):
        print(f"\n{self.name} Score: {self.total_score}\n")

class CpuPlayer:
    def __init__(self, name):
        self.name = name
        self.round_score = 0
        self.total_score = 0

    def __str__(self):
        return f'{self.name}'   
    
    def show_round_score(self):
        print(f'\nRound Score: {self.round_score}')
    
    def show_total_score(self):
        print(f"{self.name} Score: {self.total_score}")

    #hold score somehow



class Die:
    def __init__(self):
        self.sides = 6
  
    def roll(self):
        roll = random.randint(1, self.sides)
        return roll
        
    


game = Game()
game.round()
