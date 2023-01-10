
# made with python 2 

#import
import random

#functions
def GenerateRandomScene():
    scenes = ['Riverside','Top of the Mountain','Middle of Forest','Mountain Side']#desert excluded
    water = [True,False]
    startitems = ['Match','Match','Match','Match','Match','Pocket Knive','Jacket','Full Bottle of Clean Water','Full Bottle of Clean Water','Energy Bar','Banadges','Walking Stick','Journal','Match','Tea Leaves','Cooking Set']
    randomstarting1 = ['Magnesium Fire Starter', 'Warming Pack', 'Sleeping Bag', 'Axe', 'Torch']
    randomstarting2 = ['Batteries', 'Bucket', 'Vaseline', 'Hygiene Kit', 'String', 'Camp Set']
    sceneforplayer = random.choice(scenes)
    if sceneforplayer == 'Riverside':
        water = True
    elif sceneforplayer == 'Desert':
        water = False
    else:
        water = random.choice(water)
    startitems.append(random.choice(randomstarting1))
    startitems.append(random.choice(randomstarting2))
    return [[random.randint(50,100),sceneforplayer,water],startitems]


def GenerateRandomExplore(scene):
    itemscanbeobtained = ['Berries', 'Mushrooms', 'Tree Bark', 'Plant Fibre', 'Dead Grass', 'Dead Hare', 'Bones','Water Puddle']
    retlist = []
    if scene == 'Riverside':
        for i in range(random.randint(0,3)):
            retlist.append(random.choice(itemscanbeobtained))
        return retlist
    elif scene == 'Top of the Mountain':
        itemscanbeobtained.remove('Berries')
        itemscanbeobtained.remove('Mushrooms')
        itemscanbeobtained.remove('Dead Hare')
        itemscanbeobtained.append('Dead Birds')
        itemscanbeobtained.append('Bait')
        itemscanbeobtained.append('Bird Nest')
        for i in range(random.randint(0,3)):
            retlist.append(random.choice(itemscanbeobtained))
        return retlist
    elif scene == 'Middle of Forest':
        itemscanbeobtained.append('Bait')
        itemscanbeobtained.append('Bird Nest')
        for i in range(random.randint(0,3)):
            retlist.append(random.choice(itemscanbeobtained))
        return retlist
    elif scene == 'Desert':
        itemscanbeobtained = ['Catti', 'Dead Catti Skin', 'Tree Bark', 'Stick', 'Well', 'Bones']
        for i in range(random.randint(0,3)):
            retlist.append(random.choice(itemscanbeobtained))
        return retlist
    else:
        itemscanbeobtained.remove('Berries')
        itemscanbeobtained.remove('Mushrooms')
        itemscanbeobtained.remove('Dead Hare')
        itemscanbeobtained.append('Dead Birds')
        itemscanbeobtained.append('Bait')
        itemscanbeobtained.append('Bird Nest')
        for i in range(random.randint(0, 3)):
            retlist.append(random.choice(itemscanbeobtained))
        return retlist


def GetWood(inventory):
    if 'Axe' in inventory:
        minnum = 3
        maxnum = 7
    else:
        minnum = 1
        maxnum = 5
    return random.randint(minnum,maxnum)


def Hunting(location,inventory,water):
    fishingrod = SearchItem('Fishing Rod',inventory)
    hygiene = SearchItem('Hygiene Kit',inventory)
    prey = ['bear','lion','cheetah','deer','cow','pig','fox','wolf','rabbit','toad','','','']
    if fishingrod != 0 and water:
        prey.append('fish')
    if hygiene != 0:
        for i in range(2):
            prey.append('deer')
            prey.append('cow')
            prey.append('pig')
            prey.append('fox')
            prey.append('wolf')
            prey.append('rabbit')
            prey.append('toad')
    desertprey = ['camel','','','','','','','scorpian','poisonous scorpian']
    if location == 'Desert':
        appear = random.choice(desertprey)
        if appear == 'poisonous scorpian':
            return [appear,'lethal']
        else:
            return [appear,'True']
    else:
        appear = random.choice(prey)
        if appear in ['bear','lion','cheetah']:
            success = random.choice(['True','False','False','False','False','False','False','False','False','False','False'])
            if success == 'False':
                injury = random.choice(['leg','arm','chest','broken ribs','broken leg','neck','lethal'])
                return [appear,injury]
            else:
                return [appear,success]
        else:
            return [appear,'True']


def Menu(hydration,heat,hour,watersource,dndeterminer,dist,hunger):
    if hour > 12:
        hour = hour - 12
        if dndeterminer == 0:
            dndeterminer = 1
        elif dndeterminer == 1:
            dndeterminer = 0
    if dndeterminer == 1:
        print "There are "+str(12-hour)+" hours of night time left"
    else:
        print "There are "+str(12-hour)+" hours of day time left"
    print '1. Chop Trees'
    print '2. Make Fire'
    print '3. Discover'
    print '4. Read The Rule of 3'
    print '5. Rest'
    print '6. Hunt'
    print '7. Walk'
    print '8. Craft'
    print '9. View Inventory'
    print '10. Drink Water'
    print '11. Eat'
    print '12. Use Items'
    print '13. Build Shelter'
    if watersource:
        print "There are Water Sources around You"
        print '14. Get Water'
    print 'Hydration: '+str(hydration)
    print 'Body Heat: '+str(heat)
    print "Hunger: "+str(hunger)
    print 'Distance between Civilisation: '+str(dist)+ ' km'
    print
    return [raw_input('Action >>> '),hour,dndeterminer]


def Ruleof3():
    print '3 mins without air'
    print '3 hours without shelter'
    print '3 days without water'
    print '3 weeks without food'
    print '3 months without hope'


def Intro():
    print "Welcome!"
    print "This game is all about your survival techinques"
    print "Always Remember the rule of 3"
    Ruleof3()
    scene = GenerateRandomScene()
    print "Your charactor is trapped in a "+scene[0][1]
    print "The distance to civilisation is "+str(scene[0][0])+" km"
    print "Your aim is to help your charactor survive"
    DisplayInventoryTry2(scene[1])
    return scene


def Walk(dist,hydration,heat,inventory,dndeterminer):
    if 'Walking Stick' in inventory:
        maxwalking = 8
    else:
        maxwalking = 5
    if dndeterminer == 1 and ("Torch" not in inventory or "Fire Torch" not in inventory):
        maxwalking = 2

    walked = random.randint(1,maxwalking)
    dist -= walked
    hydration -= 10
    heat += 10
    return [walked,hydration,heat]


def DisplayInventoryTry2(inventory):
    amtcount = []
    amtcountunique = []
    for i in range(len(inventory)):
        if inventory[i] not in amtcountunique:
            amtcount.append([inventory[i],1])
            amtcountunique.append(inventory[i])
        else:
            for x in amtcount:
                if inventory[i] == x[0]:
                    x[1]+=1
    print "You have: "
    for i in amtcount:
        print str(i[1])+" x "+str(i[0])


def DrinkWater(inventory):
    amtcount = []
    amtcountunique = []
    water = []
    for i in range(len(inventory)):
        if inventory[i] not in amtcountunique:
            amtcount.append([inventory[i], 1])
            amtcountunique.append(inventory[i])
        else:
            for x in amtcount:
                if inventory[i] == x[0]:
                    x[1] += 1
    for i in amtcount:
        if i[0] in ["Full Bottle of Clean Water","Full Bottle of Dirty Water"]:
            water.append(i)
    if water[0][0] == "Full Bottle of Dirty Water":
        water[0],water[1] = water[1],water[0]
    print "You have: "
    if len(water) != 0:
        for i in range(len(water)):
            print str(i+1)+". " + str(water[i][1])+" x "+str(water[i][0])
        print "Which water would you want to drink? "
        waters = raw_input(">>> ")
        if waters == '1':
            if water[0][1] - 1 >= 0:
                inventory.remove('Full Bottle of Clean Water')
                inventory.append('Empty Bottle')
                return [50, inventory]
        elif waters[0] == '2':
                if water[1][1] - 1 >= 0:
                    inventory.remove('Full Bottle of Dirty Water')
                    inventory.append('Empty Bottle')
                    if random.randint(1,10)  < random.randint(1,10):
                        return [30,inventory]
                    else:
                        print "The water is contaminated. Hydration - 30!"
                        return [-30,inventory]
        else:
            print "Invalid Choice, No Such Choice Exists"
    else:
        print "You have no water supplies"


def CheckValidBody(hydration):
    if hydration > 100:
        hydration = 100
        return hydration
    else:
        return hydration


def CheckValidHunger(hydration):
    if hydration < 0:
        hydration = 0
        return hydration
    else:
        return hydration


def SearchItem(item,inventory):
    amtcount = []
    amtcountunique = []
    for i in range(len(inventory)):
        if inventory[i] not in amtcountunique:
            amtcount.append([inventory[i], 1])
            amtcountunique.append(inventory[i])
        else:
            for x in amtcount:
                if inventory[i] == x[0]:
                    x[1] += 1
    for i in amtcount:
        if i[0] == item:
            amount = i[1]
    try:
        return amount
    except:
        return 0


def ReplaceItem(item,changeto, inventory):
    inventoryx = inventory
    inventoryx.remove(item)
    for i in range(len(inventory)-len(inventoryx)):
        inventory.append(changeto)
    return inventoryx


def MakeFire(inventory):
    inventoryx = FireLightingMethod(inventory)
    if inventoryx == inventory:
        print "You cannot light fire as you do not have enough tinder"
        return [0,inventory]
    else:
        print 'Fire Lighted!'
        print 'Body Heat + 30!'
        return [30,inventoryx]


def SearchFood(inventory):
    food = ['berries',
            'mushrooms',
            'bear flesh',
            'lion flesh',
            'cheetah flesh',
            'deer flesh',
            'cow flesh',
            'pig flesh',
            'fox flesh',
            'wolf flesh',
            'rabbit flesh',
            'toad flesh',
            'camel flesh',
            'scorpian flesh',
            'poisonous scorpian flesh',
            'fish']
    energy = [15,15,40,70,70,40,50,40,20,20,40,20,40,20,20,60]
    ownedfood = []
    for i in inventory:
        if i in food:
            ownedfood.append(i)
    if len(ownedfood) == 0:
        print "You do not have any food"
    else:
        DisplayInventoryTry2(ownedfood)
        print "What do you want to eat?"
        consume = raw_input(">>> ").lower()
        for i in ownedfood:
            if consume == i:
                owned = True
            else:
                owned = False
        if not owned:
            print "You do not have this food"
        else:
            inventory.remove(consume)
            if consume == 'rabbit flesh':
                inventory.append('rabbit skin')
            for i in range(len(food)):
                if food[i] == consume:
                    energy = energy[i]
            return [inventory,energy]


def CraftingList():
    print ">>> Crafting List <<<"
    print "1. Tinder: 1 x Wood > 3 x Tinder"
    print "2. String: 1 x Plant Fibre > 1 x String"
    print "3. String: 1 x Dead Grass > 1 x String"
    print "4. String: 1 x Cloth > 2 x String"
    print "5. Cloth: 1 x Clothes > 3 x Cloth ***Tearing Clothes will increase the rate of heat loss!"
    print "6. Bow Drill: 1 x String, 2 x Wood > 1 x Bow Drill"
    print "7. Bone Knive: 1 x Bone, 1 x String > 1 x Bone Knive"
    print "8. Bandage: 1 x Cloth > 3 x Bandage"
    print "9. Fire Torch: 1 x Wood, 1 x String, 1 x Vaseline, 1 x Tree Bark > 1 x Fire Torch"
    print "10. Fishing Rod: 1 x Wood, 1 x String, 1 x Knive > 1 x Fishing Rod"
    print "11. Water Bottle: 1 x Rabbit Skin > 1 x Water Bottle"
    print "Which one do you want to craft?"
    print
    return raw_input(">>> ")


def CraftItem(inventory,required_materials,crafted):
    amtcount = []
    amtcountunique = []
    consumestr = ""
    for i in range(len(required_materials)):
        if required_materials[i] not in amtcountunique:
            amtcount.append([required_materials[i],1])
            amtcountunique.append(required_materials[i])
        else:
            for x in amtcount:
                if required_materials[i] == x[0]:
                    x[1]+=1
    for i in amtcount:
        consumestr = consumestr + str(i[1])+" x "+str(i[0]) + " "
    craftedstr = str(crafted[1])+" x "+str(crafted[0])
    print "Crafting "+str(craftedstr)+" will consume "+str(consumestr)
    print "Are you sure?"
    confirmation = raw_input("Y / N >>> ")
    if confirmation.lower() == "y":
        try:
            for i in required_materials:
                inventory.remove(i)
            for i in range(int(crafted[1])):
                inventory.append(crafted[0])
            return inventory
        except:
            print "You are missing some indgredients"
            return inventory


def FireLightingMethod(inventory):
    lightingitems = ['Bow Drill', 'Match', 'Magnesium Fire Starter', 'Batteries']
    ownedlighting = []
    for i in inventory:
        if i in lightingitems:
            ownedlighting.append(i)
    print "You have these lighting items:"
    DisplayInventoryTry2(ownedlighting)
    print "Which one do you want to use to light?"
    tolight = raw_input(">>> ").lower()
    found = False
    for i in ownedlighting:
        if tolight == i.lower():
            removeitem = i
            found = True
    if not found:
        print "You cannot light fire as you do not have the item"
    for i in inventory:
        if i == 'Tinder':
            if tolight == 'match':
                inventory.remove(removeitem)
            else:
                pass
            inventory.remove('Tinder')
    return inventory


def UseableItemsOutput(inventory):
    useableitems = ['Tea Leaves','Warming Pack','Energy Bar']
    useableowned = []
    for i in inventory:
        if i in useableitems:
            useableowned.append(i)
    if len(useableowned) != 0:
        print 'You own these useable items:'
        DisplayInventoryTry2(useableowned)
        print ">>> Which one do you want to use? <<<"
        use = raw_input("Please type in the full item name >>> ").lower()
        for i in useableowned:
            if use == i.lower():
                inventory.remove(i)
                return [inventory,i]
                break
    else:
        print 'You do not own any useable items'


def UsedItem(hydration,heat,hunger,useitem):
    import time
    useableitems = ['Tea Leaves', 'Warming Pack', 'Energy Bar']
    if useitem not in useableitems:
        print "Error 001, item to use is not in the Useable Items List!"
        print "Creating Crash Log."
        f = open('CrashLog: Error 001','a+')
        f.writelines(time.asctime())
        f.writelines('Item To Use: '+useitem)
        f.close()
        raise ValueError,'item to use is not in the Useable Items List!'
    else:
        if useitem == useableitems[0]:
            hydration = 100
            print "Hydration Restored to 100"
        elif useitem == useableitems[1]:
            heat = 100
            print "Heat Restored to 100"
        elif useitem == useableitems[2]:
            hunger -= 30
            print "Hunger - 30"
        return [hydration,heat,hunger]


#Variables
inform = Intro()
dist = inform[0][0]
scene = inform[0][1]
watersource = inform[0][2]
startingitems = inform[1]
hour = 0
dndeterminer = 0
hydration = 100
heat = 100
hunger = 0
shelter = False
clothing = True
#__main__
while dist > 0:
    if hydration > 0 and heat > 0 and hunger < 100:
        print
        if not clothing:
            #for minising
            heat -= 5
        action = Menu(hydration,heat,hour,watersource,dndeterminer,dist,hunger)
        hour = action[1]
        dndeterminer = action[2]
        action = action[0]
        if action == '1':
            if dndeterminer == 0:
                wood = GetWood(startingitems)
            else:
                wood = random.randint(0,2)
            for i in range(wood):
                startingitems.append('Wood')
            print str(wood) + ' log(s) are obtained'
            hour += 1
            heat += 10
            heat = CheckValidBody(heat)
            hydration -= 15
            hunger += 5
            hydration = CheckValidBody(hydration)
            print "You used 1 hour to collect some logs"
        elif action == '2':
            fire = MakeFire(startingitems)
            startingitems = fire[1]
            heat += fire[0]
            try:
                startingitems = ReplaceItem('Full Bottle of Dirty Water','Full Bottle of Clean Water', startingitems)
                print "Water Purified!"
            except:
                pass
        elif action == '3':
            if dndeterminer == 0:
                discover = GenerateRandomExplore(scene)
                discover_str = ''
            else:
                discover = ["Nothing"]
                discover_str = ''
            if discover != []:
                for i in discover:
                    discover_str = discover_str + i + ' '
                    startingitems.append(i)
                print discover_str + 'is/are obtained'
            else:
                print "Nothing is found"
            hour += 1
            heat += 10
            heat = CheckValidBody(heat)
            hydration -= 10
            hunger += 10
            hydration = CheckValidBody(hydration)
            print "You have used 1 hour to explore around you"
        elif action == '4':
            # this line is used for minising
            Ruleof3()
        elif action == '5':
            hour += 5
            print "You have used 5 hours to rest, energy is restored"
            hydration -= 5
            if shelter:
                pass
            else:
                heat -= 15
            if 'Sleeping Bag' in startingitems:
                heat += 20
            hunger += 15
            heat = CheckValidBody(heat)
            hydration = CheckValidBody(hydration)
        elif action == '6':
            captured = Hunting(scene,startingitems,watersource)
            hour += 1
            if captured[1] == 'True' and captured[0] != 'poisonous scorpian':
                if captured[0]:
                    print "You saw a "+captured[0]+" and you captured it"
                    startingitems.append((captured[0]+' flesh'))
                    print 'You have used 1 hour to hunt'
                    hydration -= 15
                    hydration = CheckValidBody(hydration)
                    heat += 15
                    heat = CheckValidBody(heat)
                else:
                    print "You didn't see anything"
            elif captured[1] == 'False':
                print "You saw a "+captured[0]+" and it escaped... bad luck!"
            else:
                print "You saw a "+captured[0]+" and it attacked you, causing a "+captured[1]+" injury!"
                if captured[1] in ['broken ribs','lethal','neck']:
                    print "You died"
                    dist = 0
            hunger += 20
        elif action == '7':
            walked = Walk(dist,hydration,heat,startingitems,dndeterminer)
            hour += 4
            dist -= walked[0]
            hydration = walked[1]
            hydration = CheckValidBody(hydration)
            heat = walked[2]
            heat = CheckValidBody(heat)
            watersource = random.choice([True,False])
            print "You have used 4 hours to walk "+str(walked[0])+" km"
            hunger += 20
        elif action == '8':
            craft = CraftingList()
            if craft == "1":
                startingitems = CraftItem(startingitems, ["Wood"], ["Tinder", "3"])
            elif craft == "2":
                startingitems = CraftItem(startingitems, ["Plant Fibre"], ["String", "1"])
            elif craft == "3":
                startingitems = CraftItem(startingitems, ["Dead Grass"], ["String", "1"])
            elif craft == "4":
                startingitems = CraftItem(startingitems, ["Cloth"], ["String", "2"])
            elif craft == "5":
                startingitemsx = CraftItem(startingitems, ["Clothes"], ["Cloth", "3"])
                if startingitemsx != startingitems:
                    clothing = False
                startingitemsx = startingitems
            elif craft == "6":
                startingitems = CraftItem(startingitems, ["String","Wood","Wood"], ["Bow Drill", "1"])
            elif craft == "7":
                startingitems = CraftItem(startingitems, ["Bone","String"], ["Bone Knive", "1"])
            elif craft == "8":
                startingitems = CraftItem(startingitems, ["Cloth"], ["Bandage", "3"])
            elif craft == "9":
                startingitems = CraftItem(startingitems, ["Wood","Vaseline","String","Tree Bark"], ["Fire Torch", "1"])
            elif craft == "10":
                startingitems = CraftItem(startingitems, ["Wood","String","Knive"], ["Fishing Rod", "1"])
            elif craft == "11":
                startingitems = CraftItem(startingitems, ["Rabbit Skin"], ["Water Bottle", "1"])
            else:
                print "This is not a valid choice"
        elif action == '9':
            #this line is used for minising
            DisplayInventoryTry2(startingitems)
        elif action == '10':
            water = DrinkWater(startingitems)
            try:
                hydration += water[0]
                hydration = CheckValidBody(hydration)
                startingitems = water[1]
            except:
                pass
        elif action == '11':
            print "Energy Bars are in Use Items Section. It has an amazing buff!"
            food = SearchFood(startingitems)
            try:
                startingitems = food[0]
                hunger -= food[1]
                CheckValidHunger(hunger)
            except:
                pass
        elif action == '12':
            check = UseableItemsOutput(startingitems)
            startingitems = check[0]
            used = check[1]
            useitem = UsedItem(hydration,heat,hunger,used)
            hydration = useitem[0]
            heat = useitem[1]
            hunger = CheckValidHunger(useitem[2])
        elif action == '13':
            if 'Camp Set' in startingitems:
                hour += 1
            else:
                hour += 4
            print "Shelter Built, Rest would not decrease heat."
        elif action == '14':
            if watersource:
                emptybottles = SearchItem('Empty Bottle',startingitems)
                if emptybottles == 0:
                    print "You do not have empty bottles"
                else:
                    startingitems = ReplaceItem('Empty Bottle',"Full Bottle of Dirty Water",startingitems)
                    print str(emptybottles)+' x Empty Bottles has been filled up to '+str(emptybottles)+' x Full Bottle of Dirty Water'
                    hunger += 5
            else:
                print "This is not a valid input"
        else:
            # this line is used for minising
            print "This is not a valid input!"
    else:
        dist = 0
        if hydration <= 0:
            print "You died of thirst"
            print "GAME OVER..."
        elif heat <= 0:
            print "You died of hypothermia"
            print "GAME OVER..."
        elif hunger >= 100:
            print "You have starved to death"
            print "GAME OVER..."
if dist <= 0 and hydration > 0 and heat > 0 and hunger < 100:
    print "WELL DONE!"
    print "YOU SURVIVED!!!!!"
W
