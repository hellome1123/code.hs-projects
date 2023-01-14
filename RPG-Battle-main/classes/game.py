import random
from .magic import Spell

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m' #red
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Person:
    def __init__(self,name, hp,mp, atk, df, magic, items):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Magic", "Items"]
        self.name = name

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if(self.hp < 0):
            self.hp = 0
        return self.hp

    def heal(self,dmg):
        self.hp += dmg
        return self.hp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_action(self):
        print("\n    " + bcolors.BOLD + self.name + bcolors.ENDC)
        i=1
        print("    " + bcolors.OKBLUE + bcolors.BOLD + "ACTIONS" + bcolors.ENDC)
        for item in self.actions:
            print("        " + str(i) + ".", item)
            i += 1

    def choose_magic(self):
        i = 1
        print("\n    " + bcolors.OKBLUE + bcolors.BOLD + "MAGIC" + bcolors.ENDC)
        for spell in self.magic:
            print("        " + str(i) + ".", spell.name, "(cost:", str(spell.cost) + ")")
            i += 1

    def choose_item(self):
        i = 1
        print("\n    " + bcolors.OKGREEN + bcolors.BOLD + "ITEMS" + bcolors.ENDC)
        for item in self.items:
            print("    " + str(i) + "." + item["item"].name + ":" + item["item"].description + " (x" + str(item["quantity"]) + ")")
            i += 1

    def choose_target(self, enemies):
        i = 1
        print("\n" + bcolors.FAIL + bcolors.BOLD + "    TARGET:" + bcolors.ENDC)
        for enemy in enemies:
            if enemy.get_hp() != 0:
                print("        " + str(i) + "." + enemy.name)
                i+=1
        choice = int(input("    Choose target:")) - 1
        return choice

    def get_enemy_stats(self):
        hp_bar = ""
        bar_ticks = (self.hp / self.maxhp) * 100 / 2 # per 50

        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1

        while len(hp_bar) < 50:
            hp_bar += " "

        currenthp = str(self.hp) + "/" + str(self.maxhp)

        if len(currenthp)<11:
            decrease = 11 - len(currenthp)
            while decrease > 0:
                currenthp = " " + currenthp
                decrease -= 1

        print("                                  __________________________________________________")
        print(bcolors.BOLD + self.name + "           " + currenthp + "|" + bcolors.FAIL + hp_bar + bcolors.ENDC + bcolors.BOLD + bcolors.ENDC + "|")

    def get_stats(self):
        hp_bar = ""
        bar_ticks = (self.hp / self.maxhp) * 100 / 4 # per 25

        mp_bar = ""
        mp_ticks = (self.mp / self.maxmp) * 100 / 10 # per 10

        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1

        while mp_ticks > 0:
            mp_bar += "█"
            mp_ticks -= 1

        while len(hp_bar) < 25:
            hp_bar += " "

        while len(mp_bar) < 10:
            mp_bar += " "

        powerhp = str(self.hp) + "/" + str(self.maxhp)
        if len(powerhp)<9:
            decrease = 9 - len(powerhp)
            while decrease > 0:
                powerhp = " " + powerhp
                decrease -= 1

        powermp = str(self.mp) + "/" + str(self.maxmp)
        if len(powermp)<7:
            decrease = 7 - len(powermp)
            while decrease > 0:
                powermp = " " + powermp
                decrease -= 1

        print("                                  _________________________               __________")
        print(bcolors.BOLD + self.name + "             " + powerhp + "|" + bcolors.OKGREEN + hp_bar + bcolors.ENDC + bcolors.BOLD + "|"
              + "     " + powermp + " |" + bcolors.OKBLUE + mp_bar + bcolors.ENDC + "|")
