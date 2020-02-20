import random

class Game:
    def __init__(self):
        self.player = Player("Nathan")
        self.cpu = CpuPlayer("STUPID ROBOT")
        self.die = Die()
        self.first_player = True
        self.second_player = False        
    
    def show_roll(self):
        print(f"Roll: {self.die.roll()}")
    
    def switch_players(self): 
        if self.first_player:
            self.first_player = False
            self.second_player = True
        elif self.second_player:
            self.second_player = False
            self.first_player = True

    def round(self):
        while self.player.total_score < 100 and self.cpu.total_score < 100:
            if self.first_player:
                choice = input(f'{self.player}, do you want to (r)oll or (h)old? ')
                if choice == 'r':
                    roll = self.die.roll()
                    print(f"Roll: {roll}")
                    if roll == 1:
                        self.player.round_score = 0
                        print('PIG')
                        self.player.show_round_score()
                        self.switch_players()
                    else:
                        self.player.round_score += roll
                        # self.show_roll()  
                        self.player.show_round_score() 
                elif choice == 'h': 
                    self.player.total_score += self.player.round_score
                    self.player.show_total_score()
                    self.player.round_score = 0
                    self.switch_players()
            elif self.second_player:
                choice = input(f'{self.cpu}, do you want to (r)oll or (h)old? ')
                while self.cpu.round_score < 20:
                    roll = self.die.roll()
                    print(f"Roll: {roll}")
                    if roll == 1:
                        self.cpu.round_score = 0
                        print('PIG')
                        self.cpu.show_round_score()
                        self.switch_players()
                    else:
                        self.cpu.round_score += roll
                        # self.show_roll()  
                        self.cpu.show_round_score() 
                else: 
                    self.cpu.total_score += self.cpu.round_score
                    self.cpu.show_total_score()
                    self.cpu.round_score = 0
                    self.switch_players()
        else: 
            print("WE HAVE A WINNER!")

            
        
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
        print(f"\nTotal Score: {self.total_score}\n")

class CpuPlayer:
    def __init__(self, name):
        self.name = name
        self.round_score = 0
        self.total_score = 0
    def __str__(self):
        return f'{self.name}'   
    
    def show_round_score(self):
        print(f'Round Score: {self.round_score}')
    
    def show_total_score(self):
        print(f"Total Score: {self.total_score}")

    #hold score somehow



class Die:
    def __init__(self):
        self.sides = 6
  
    def roll(self):
        roll = random.randint(1, self.sides)
        return roll
        
    


game = Game()
game.round()
