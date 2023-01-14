from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item
import random

# ascii 219 :█

#Create Black MAgic
fire = Spell("Fire", 35, 150, "black")  #name, cost, dmg, Type
thunder = Spell("Thunder", 45, 200, "black")
blizzard = Spell("Blizzard", 52, 270, "black")
meteor = Spell("Mateor", 72, 300, "black")
quake = Spell("Quake", 100, 400, "black")

#Create White Magic
cure = Spell("Cure", 105, 620, "white")
cura = Spell("Cura", 117, 800, "white")

#Create some Items
potion = Item("Potion", "potion", "Heals 34 HP", 340)    # name, Type, description, prop
hipotion = Item("Hi-Potion", "potion", "Heals 500 HP", 500)
superpotion = Item("Super Potion", "potion", "Heals 900 HP", 900)
elixir = Item("Elixir", "elixir", "Fully restores HP/MP of one party member", 9999)
hielixir = Item("MegaElixir", "elixir", "Fully restores party's HP/MP", 9999)

grenade = Item("Grenade", "attack", "Deals 2110 damage", 2110)

player_spells = [fire, thunder, blizzard, meteor, cure, cura]
#player_items = [potion, hipotion, superpotion, elixir, hielixir, grenade]
player_items = [{"item": potion, "quantity": 15}, {"item":hipotion, "quantity": 5},
                {"item": superpotion, "quantity": 5}, {"item":elixir, "quantity": 5},
                {"item": hielixir, "quantity": 2}, {"item":grenade, "quantity": 5}]

'''magic = [{"name" : "Fire", "cost" : 5, "dmg" : 100},
         {"name" : "Thunder", "cost" : 10, "dmg" : 124},
         {"name" : "Blizzard", "cost" : 5, "dmg" : 100}]
'''
#Instantiate People, 
#         Person( name,         hp,   mp, atk, df, magic,         items)
Player1 = Person("Iron Man   ", 8760, 150, 375, 34, player_spells, player_items)
Player2 = Person("Thor       ", 9500, 122, 260, 27, player_spells, player_items)
Player3 = Person("BlackWidow ", 8210, 125, 390, 30, player_spells, player_items)

enemy1 = Person("Shaakaal   ", 1200, 50, 1005, 150, [], []) # high power enemy but less life
enemy2 = Person("Thanos     ", 17390, 180, 745, 25, [], []) # Main villain
enemy3 = Person("Mugambo    ", 900, 40, 925, 120, [], [])

players = [Player1, Player2, Player3]
enemies = [enemy1, enemy2, enemy3]

running = True

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:
    print("")
    print("NAME                         HP                                     MP")
    for Player in players:
        Player.get_stats()

    for enemy in enemies:
        enemy.get_enemy_stats()

    print(".....................................................................................")
    print("\n")


    for Player in players:
        Player.choose_action()  # Attack, Magic
        choice = input("    Choose action : ")
        index = int(choice) - 1

        if(index == 0):
            dmg = Player.generate_damage()
            enemy = Player.choose_target(enemies)

            enemies[enemy].take_damage(dmg)
            print( Player.name.replace(" ", "") + " attacked " + enemies[enemy].name.replace(" ", "") + " for ", dmg, "points of damage")

            if enemies[enemy].get_hp() == 0:
                print(bcolors.OKGREEN + enemies[enemy].name.replace(" ", "") + " has Died." + bcolors.ENDC)
                del enemies[enemy]

        elif(index == 1):
            Player.choose_magic()   # fire, thunder, blizzard, meteor, cure, cura
            magic_choice = int(input("    Choose magic : ")) - 1

            if magic_choice == -1:
                continue

            spell = Player.magic[magic_choice]
            magic_dmg = spell.generate_damage()

            current_mp = Player.get_mp()

            if(spell.cost > current_mp):
                print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
                continue

            Player.reduce_mp(spell.cost)

            if(spell.Type == "white"):
                Player.heal(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), " points of heal" + bcolors.ENDC)
            elif(spell.Type == "black"):
                enemy = Player.choose_target(enemies)
            
                enemies[enemy].take_damage(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), " points of damage to " + enemies[enemy].name.replace(" ", "") + bcolors.ENDC)

                if enemies[enemy].get_hp() == 0:
                    print(bcolors.OKGREEN + enemies[enemy].name.replace(" ", "") + " has Died." + bcolors.ENDC)
                    del enemies[enemy]

        elif index == 2:
            Player.choose_item()
            item_choice = int(input("    Choose item: ")) - 1

            if item_choice == -1:
                continue

            item = Player.items[item_choice]["item"]

            if Player.items[item_choice]["quantity"] == 0:
                print(bcolors.FAIL + "\nNone left...." + bcolors.ENDC )
                continue

            Player.items[item_choice]["quantity"] -=1


            if item.Type == "potion" :
                Player.heal(item.prop)
                print(bcolors.OKGREEN + "\n" + item.name + " heals for", str(item.prop), "HP" + bcolors.ENDC)

            elif item.Type == "elixir":
                if(item.name == "MegaElixir"):
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp
                else:
                    Player.hp = Player.maxhp
                    Player.mp = Player.maxmp

                print(bcolors.OKGREEN + "\n" + item.name + " fully restores HP/MP" + bcolors.ENDC)

            elif item.Type == "attack" :
                enemy = Player.choose_target(enemies)
            
                enemies[enemy].take_damage(item.prop)
                print(bcolors.FAIL + "\n" + item.name + " deals", str(item.prop), "points of damage to " + enemies[enemy].name.replace(" ", "") + bcolors.ENDC)

                if enemies[enemy].get_hp() == 0:
                    print(bcolors.OKGREEN + enemies[enemy].name.replace(" ", "") + " has Died." + bcolors.ENDC)
                    del enemies[enemy]
    print()
    for enemy in enemies:
        enemy_choice = 1
        player_count = len(players)
        enemy_target = random.randrange(0,player_count) # 
        enemy_dmg = enemy.generate_damage()
        players[enemy_target].take_damage(enemy_dmg)
        print(enemy.name.replace(" ", "") + " attacks to " + players[enemy_target].name.replace(" ", "") + " for " + str(enemy_dmg) + " points of damage.")  #, "Player HP : ", Player.get_hp())
        if players[enemy_target].get_hp() == 0:
            print(bcolors.FAIL + players[enemy_target].name.replace(" ", "") + " has Died." + bcolors.ENDC)
            del players[enemy_target]

    print("----------------------------------------------------")
    
    if(len(enemies) == 0):
        print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
        running = False

    elif(len(players) == 0):
        print(bcolors.FAIL + "Your enemies have defeated you!" + bcolors.ENDC)
        running = False
