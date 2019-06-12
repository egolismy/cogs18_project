# import extra code and setup
import random
import string

from time import sleep
from IPython.display import clear_output

gladiator_postures = ["Charge", "Defend", "Sneak Attack"]
beast_postures = ["Charge", "Defend"]
# A collection of reactions when fighter would do when facing an enemy

# extra functions
def add_lists(list1, list2):
    
    output = []
    
    for it1, it2 in zip(list1, list2):
        temp = it1 + it2
        output.append(temp)
        
    return output
def check_bounds(position, size):
    
    length = 0
    
    for item in position:
        length = length + 1
        if item < 0 or item >= size:
            length = length - 1
            break
            
    if length == len(position):
        return True
    
    return False

def play_board(bots, n_iter=25, grid_size=4, sleep_time=0.3):
    """Run a bot across a board.
    
    Parameters
    ----------
    bots : Bot() type or list of Bot() type
        One or more bots to be be played on the board
    n_iter : int, optional
        Number of turns to play on the board. default = 25
    grid_size : int, optional
        Board size. default = 5
    sleep_time : float, optional
        Amount of time to pause between turns. default = 0.3.
    """
    
    # If input is a single bot, put it in a list so that procedures work
    if not isinstance(bots, list):
        bots = [bots]
    
    # Record the initial fighters
    ini_len = len(bots)
    
    # Mark two fighters
    if len(bots) == 2:
        bot1 = bots[0]
        bot2 = bots[1]
    
    # Update each bot to know about the grid_size they are on
    for bot in bots:
        bot.grid_size = grid_size

    for it in range(n_iter):
        
        # Hunger for beasts
        for bot in bots:
            if isinstance(bot,Beast):
                bot.hunger = random.choice([0,1,2,3,-1])
        # Fighters fight when they meet each other
        if bot1.position == bot2.position:
            print("They met at "+ str(bot1.position))
            bot1.combat_option()
            bot2.combat_option()
            # The fight
            if bot1.posture is "Sneak Attack" and bot2.posture is "Defend":
                bots.remove(bot2)
                print("The Champion is "+ bot1.name+ " !")
            elif bot1.posture is "Sneak Attack" and bot2.posture is "Charge":
                bots.remove(bot1)
                print("The Champion is "+ bot2.name+ " !")
            elif bot1.posture is "Charge" and bot2.posture is "Defend":
                bots.remove(bot1)
                print("The Champion is "+ bot2.name+ " !")
            elif bot1.posture is "Charge" and bot2.posture is "Sneak Attack":
                bots.remove(bot2)
                print("The Champion is "+ bot1.name+ " !")
            elif bot1.posture is "Defend" and bot2.posture is "Charge":
                bots.remove(bot2)
                print("The Champion is "+ bot1.name+ " !")
            elif bot1.posture is "Defend" and bot2.posture is "Sneak Attack":
                bots.remove(bot1)
                print("The Champion is "+ bot2.name+ " !")


        # Create the grid
        grid_list = [['.'] * grid_size for ncols in range(grid_size)]
        
        # Add bot(s) to the grid
        for bot in bots:
            grid_list[bot.position[0]][bot.position[1]] = bot.character    

        # Clear the previous iteration, print the new grid (as a string), and wait
        clear_output(True)
        print('\n'.join([' '.join(lst) for lst in grid_list]))
        sleep(sleep_time)
        
        # Fighters fight when they meet each other
        if bot1.position == bot2.position:
            print("They met at "+ str(bot1.position))
            bot1.combat_option()
            bot2.combat_option()
            # The fight
            if bot1.posture is "Sneak Attack" and bot2.posture is "Defend":
                print("The Champion is "+ bot1.name+ " !")
            elif bot1.posture is "Sneak Attack" and bot2.posture is "Charge":
                print("The Champion is "+ bot2.name+ " !")
            elif bot1.posture is "Charge" and bot2.posture is "Defend":
                print("The Champion is "+ bot2.name+ " !")
            elif bot1.posture is "Charge" and bot2.posture is "Sneak Attack":
                print("The Champion is "+ bot1.name+ " !")
            elif bot1.posture is "Defend" and bot2.posture is "Charge":
                print("The Champion is "+ bot1.name+ " !")
            elif bot1.posture is "Defend" and bot2.posture is "Sneak Attack":
                print("The Champion is "+ bot2.name+ " !")

        # Update bot position(s) for next turn
        for bot in bots:
            bot.move()
            if bot1.position == bot2.position:
                print("They met at "+ str(bot1.position))
                bot1.combat_option()
                bot2.combat_option()
                # The fight
                if bot1.posture is "Sneak Attack" and bot2.posture is "Defend":
                    print("The Champion is "+ bot1.name+ " !")
                elif bot1.posture is "Sneak Attack" and bot2.posture is "Charge":
                    print("The Champion is "+ bot2.name+ " !")
                elif bot1.posture is "Charge" and bot2.posture is "Defend":
                    print("The Champion is "+ bot2.name+ " !")
                elif bot1.posture is "Charge" and bot2.posture is "Sneak Attack":
                    print("The Champion is "+ bot1.name+ " !")
                elif bot1.posture is "Defend" and bot2.posture is "Charge":
                    print("The Champion is "+ bot1.name+ " !")
                elif bot1.posture is "Defend" and bot2.posture is "Sneak Attack":
                    print("The Champion is "+ bot2.name+ " !")

    if len(bots) == 1:
        # The last standing wins
        winner = bots[0]
        print("The Champion is "+ winner.name+ " !")
    
    if len(bots) is not 1:
        # There is no winner
        print("What a boring game")

class Gladiator():
    # A class used to descirbe galdiators in the arena
    position = []
    moves = []
    grid_size = None
    character = ""
    
    # Class Attributes
    
    def __init__(self, name, posture,character=8982):
        # Instance Attributes
        self.name = name
        self.posture = posture
        self.position = [0,0]
        self.moves = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        self.grid_size = None
        self.character = chr(character)

    # Choosing the posture
    def combat_option(self):
        # select combat posture when facing an enemy
            
        self.posture = random.choice(gladiator_postures)
    
    #decision to make a move
    def move_decision(self):
        new_pos = []
        has_new_pos = False
        while not has_new_pos:
            move = random.choice(self.moves)
            new_pos = add_lists(self.position, move)
            has_new_pos = check_bounds(new_pos, self.grid_size)
        return new_pos
    
    def move(self):
        self.position = self.move_decision()
    
    # when the fighter lost a fight
    def lose(self):
        delete 
    # Old method
    def loot(self, enemy):
        # loot the enemy after victory
        self.record = self.append(enemy.name)
        self.level = self.level + 1
        if isinstance(enemy,Gladiator):
            for item in enemy.inventory:
                self.inventory.append(item)
        print("The Champion is "+ self.name+ " !")

class Beast():
    # A class used to describe beasts in the aarena
    
    # Class Attributes
    def __init__(self, name, posture,character=1175):
        self.name = name
        self.hunger = 0
        self.posture = posture
        self.position = [0,0]
        self.moves = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        self.grid_size = None
        self.character = chr(character)
    
    def combat_option(self):
        if self.hunger > 0:
            self.posture = "Charge"
        else:
            self.posture = random.choice(["Charge","Defend"])
    
    #decision to make a move
    def move_decision(self):
        new_pos = []
        has_new_pos = False
        while not has_new_pos:
            move = random.choice(self.moves)
            new_pos = add_lists(self.position, move)
            has_new_pos = check_bounds(new_pos, self.grid_size)
        return new_pos
    
    def move(self):
        self.position = self.move_decision()
    