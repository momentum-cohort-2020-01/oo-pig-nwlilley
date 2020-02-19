import random

class Game:
    def __init__(self):
        self.player = Player("Nathan")
        self.cpu = CpuPlayer()
        self.die = Die()        
    
    def show_roll(self):
        print(f"Roll: {self.die.roll()}")

    def round(self):
        print(f"Hello, {self.player}. It is your turn.")
        while self.player.round_score < 100 and self.cpu.round_score < 100:
            choice = input('Do you want to (r)oll or (h)old?')
            if choice == 'r':
                if self.die.roll() == 1:
                    self.player.round_score = 0
                    self.show_roll()
                    print('PIG')
                    self.player.show_round_score()
                    break
                        #change players
                else:
                    
                    self.player.round_score += self.die.roll()
                    self.show_roll()  
                    self.player.show_round_score() 
            elif choice == 'h': 
                self.player.total_score += self.player.round_score
                self.player.show_total_score()
                break
                #change player
            
        
class Player:
    def __init__(self, name):
        self.name = name
        self.total_score = 0
        self.round_score = 0


    def __str__(self):
        return f'{self.name}'        

    def show_round_score(self):
        print(f'Round Score: {self.round_score}')

    def show_total_score(self):
        print(f"Total Score: {self.total_score}")

class CpuPlayer:
    def __init__(self):
        self.name = "Robot"
        self.round_score = 0
        self.total_score = 0

    #hold score somehow



class Die:
    def __init__(self):
        self.sides = 6
  
    def roll(self):
        return random.randint(1, self.sides + 1)
        
    


game = Game()
game.round()
