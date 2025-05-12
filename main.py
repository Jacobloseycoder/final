import random
def main():
    print('_]WELCOME TO DUNGEN MONSTERS[_')
    print('1.play')
    print('2.rules')
    print('3.quit')
    bing = input('select:')
    if bing == '1':
    #call the start
        start()
    elif bing == '2':
        rules()
    elif bing == '3':
        print('ending...')
    else:
        print('not a option')
        main()

def rules():
    print('you will be placed in a maze and you have to escape')
    print('you will be given options to go north,south, west, or east')
    print("you can't move anyother way")
    print('you will have to find loot and fight monsters')
    print('you can pick up items by typing pick up when prompted')
    print('to fight back agenst a monster type sword well fighting to use the sword')
    print('if your hp goes to 0 you lose')
    print('but the most important thing is to have fun')
  
#classes: player, player_class, enermy, item, and 
#make a map
#add random chance to hit or damige amount
#shows the health
class player:
    #constructor for hero class
    #__ hides the thing from other classes
    def __init__(self, name, health, weapion, player_class):
        self.__name = name
        self.__health = health
        self.__maxhealth = health
        self.__weapion = weapion
        self.__player_class = player_class
        
    #####---getter meathods---#####
    def get_name(self):
        return self.__name
    def get_health(self):
        return self.__health
    ###---setter meathods---###
    def loss_health(self, less_health):
        # this reduses the heros health
        if less_health >= self.__health:
            print('you died')
            self.__health = 0
        else:
            self.__health = self.__health - less_health

    def gain_health(self, gain_health):
        self.__health = self.__health + gain_health
        if self.__health > self.__maxhealth:
            self.__health = self.__maxhealth
            
class enermy:
    def __init__(self, name, health, attack, max_health):
        self.__name = name
        self.__health = health
        self.__max_health = max_health
        self.__attack = attack
    def health_check(self):
        return self.__health
    def health_loss(self, damige):
        # this reduses the heros health
        if less_health >= self.__health:
            self.__health = 0
        else:
            self.__health = self.__health - damige
    def attack(self):
        less_health = random.randint(1,10)
        return less_health

class item:
    def __init__():
        pass
    def description(self):
        pass
    def damige(self):
        pass

class item_bar:
    def __init__(self):
        pass

class map_locations:
    def __init__():
        pass
    
#    MAP LAYOUT
#   __ __ __ __ __
#5 |__|__|__|__|__|
#4 |__|__|__|__|__|
#3 |__|__|__|__|__|
#2 |__|__|__|__|__|
#1 |__|__|__|__|__|
#    1  2  3  4  5
def map_gen():
    #(1,1)
    if up_down == 1 and left_right == 1:
        print('you see moss paches all around the room')
        print('you noutise there is only two doors')
        print('1. north')
        print('2. east')
        move = input('choose:')
        if move == 'north':
            up_down = up_down + 1
        elif move == 'east':
            left_right = left_right + 1
    #(1,2)
    elif up_down == 2 and left_right == 1:
        print('north')
        print('east')
        print('south')
        move = input('choose:')
        if move == 'north':
            up_down = up_down + 1
        elif move == 'east':
            left_right = left_right + 1
        elif move == 'south':
            up_down = up_down - 1
    #(1,3)
    elif up_down == 3 and left_right == 1:
        print('north')
        print('east')
        print('south')
        move = input('choose:')
        if move == 'north':
            up_down = up_down + 1
        elif move == 'east':
            left_right = left_right + 1
        elif move == 'south':
            up_down = up_down - 1
    #(1,4)
    elif up_down == 4 and left_right == 1:
        print('north')
        print('east')
        print('south')
        move = input('choose:')
        if move == 'north':
            up_down = up_down + 1
        elif move == 'east':
            left_right = left_right + 1
        elif move == 'south':
            up_down = up_down - 1
    #(1,5)
    elif up_down == 5 and left_right == 1:
        print('east')
        print('south')
        move = input('choose:')
        if move == 'south':
            up_down = up_down - 1
        elif move == 'east':
            left_right = left_right + 1
    #(2,1)
    elif up_down = 1 and left_right = 2:
        print('east')
        print('north')
        print('west')
        move = input('choose:')
        if move == 'south':
            up_down = up_down - 1
        elif move == 'north':
            up_down = up_down + 1
        elif move == 'west':
            left_right = left_right - 1
    #(2,2)
    elif up_down = 2 and left_right = 2:
        move = input('choose:')
    if move == 'north':
        up_down = up_down + 1
    elif move == 'south':
        up_down = up_down - 1
    elif move == 'east':
        left_right = left_right + 1
    elif move == 'west':
        left_right = left_right - 1
    #(2,3)
    elif up_down = 3 and left_right = 2:
        move = input('choose:')
    if move == 'north':
        up_down = up_down + 1
    elif move == 'south':
        up_down = up_down - 1
    elif move == 'east':
        left_right = left_right + 1
    elif move == 'west':
        left_right = left_right - 1
    #(2,4)
    elif up_down = 4 and left_right = 2:
        move = input('choose:')
    if move == 'north':
        up_down = up_down + 1
    elif move == 'south':
        up_down = up_down - 1
    elif move == 'east':
        left_right = left_right + 1
    elif move == 'west':
        left_right = left_right - 1
    #(2,5)
    elif up_down = 5 and left_right = 2:
        print('east')
        print('south')
        print('west')
        move = input('choose:')
        if move == 'south':
            up_down = up_down - 1
        elif move == 'east':
            left_right = left_right + 1
        elif move == 'west':
            left_right = left_right - 1
    #(3,1)
    elif up_down = 1 and left_right = 3:
        print('east')
        print('north')
        print('west')
        move = input('choose:')
        if move == 'south':
            up_down = up_down - 1
        elif move == 'east':
            left_right = left_right + 1
        elif move == 'west':
            left_right = left_right - 1
    #(3,2)
    elif up_down = 2 and left_right = 3:
        move = input('choose:')
    if move == 'north':
        up_down = up_down + 1
    elif move == 'south':
        up_down = up_down - 1
    elif move == 'east':
        left_right = left_right + 1
    elif move == 'west':
        left_right = left_right - 1
    #(3,3)
    elif up_down = 3 and left_right = 3:
        move = input('choose:')
    if move == 'north':
        up_down = up_down + 1
    elif move == 'south':
        up_down = up_down - 1
    elif move == 'east':
        left_right = left_right + 1
    elif move == 'west':
        left_right = left_right - 1
    #(3,4)
    elif up_down = 4 and left_right = 3:
        move = input('choose:')
    if move == 'north':
        up_down = up_down + 1
    elif move == 'south':
        up_down = up_down - 1
    elif move == 'east':
        left_right = left_right + 1
    elif move == 'west':
        left_right = left_right - 1
    #(3,5)
    elif up_down = 5 and left_right = 3:
        print('west')
        print('east')
        print('south')
        move = input('choose:')
        if move == 'west':
            left_right = left_right - 1
        elif move == 'east':
            left_right = left_right + 1
        elif move == 'south':
            up_down = up_down - 1
    #(4,1)
    elif up_down = 1 and left_right = 4:
        print('west')
        print('east')
        print('north')
        move = input('choose:')
        if move == 'west':
            left_right = left_right - 1
        elif move == 'east':
            left_right = left_right + 1
        elif move == 'north':
            up_down = up_down + 1
    #(4,2)
    elif up_down = 2 and left_right = 4:
        move = input('choose:')
    if move == 'north':
        up_down = up_down + 1
    elif move == 'south':
        up_down = up_down - 1
    elif move == 'east':
        left_right = left_right + 1
    elif move == 'west':
        left_right = left_right - 1
    #(4,3)
    elif up_down = 3 and left_right = 4:
        move = input('choose:')
    if move == 'north':
        up_down = up_down + 1
    elif move == 'south':
        up_down = up_down - 1
    elif move == 'east':
        left_right = left_right + 1
    elif move == 'west':
        left_right = left_right - 1
    #(4,4)
    elif up_down = 4 and left_right = 4:
        move = input('choose:')
    if move == 'north':
        up_down = up_down + 1
    elif move == 'south':
        up_down = up_down - 1
    elif move == 'east':
        left_right = left_right + 1
    elif move == 'west':
        left_right = left_right - 1
    #(4,5)
    elif up_down = 5 and left_right = 4:
        print('west')
        print('east')
        print('south')
        move = input('choose:')
        if move == 'west':
            left_right = left_right - 1
        elif move == 'east':
            left_right = left_right + 1
        elif move == 'south':
            up_down = up_down - 1
    #(5,1)
    elif up_down = 1 and left_right = 5:
        print('west')
        print('north')
        move = input('choose:')
        if move == 'west':
            left_right = left_right - 1
        elif move == 'south':
            up_down = up_down + 1
    #(5,2)
    elif up_down = 2 and left_right = 5:
        pass
    #(5,3)
    elif up_down = 3 and left_right = 5:
        pass
    #(5,4)
    elif up_down = 4 and left_right = 5:
        pass
    #(5,5)
    elif up_down = 5 and left_right = 5:
        pass

def move():
    move = input('choose:')
    if move == 'north':
        up_down = up_down + 1
    elif move == 'south':
        up_down = up_down - 1
    elif move == 'east':
        left_right = left_right + 1
    elif move == 'west':
        left_right = left_right - 1

def item_bar():
    pass

def play():
    name = input('enter the players name:')
    weapion = input('enter the players weapion')
    hp = 50
    print('select your class')
    print('1. runner: has a 50/50 chanes to run away in a fight')
    print('2. fighter: all attacks have a 20% chance of doing double damige')
    print('3. evader: has a 25% chanse not to get hit')
    clas = input('select here:')
    if clas == '1':
        classs = 'runner'
    elif clas == '2':
        classs = 'fighter'
    elif clas == '3':
        classs = 'evader'
    else:
        print('not a option')
        play()
    hero = player(name, hp, weapion, classs)
    hero_class = player_class(classs)
    
def effect_check():
    if hero_class.player_class() == 'runner':
        effect = 'run'
    elif hero_class.player_class() == 'fighter':
        effect = 'fight'
    elif hero_class.player_class() == 'evader':
        effect = 'evad'

def battle():
    pass
