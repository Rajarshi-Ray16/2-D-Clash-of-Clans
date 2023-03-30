from typing import overload
from village import Cannon, Wizard_Tower, Town_Hall, Hut, Village
from characters import Spawning_Point, King, Queen, Barbarian, Archer, Balloon 
from random import randint
from input import get_input
import time
import sys
from os import system, name 
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

FPS = 30
T = (1 / FPS)

def formVillage(village, town_hall, list_of_huts, list_of_cannons, list_of_wizard_towers):
    
    v_length, v_breadth = village.size_length, village.size_breadth
    th_length, th_breadth = town_hall.size_length, town_hall.size_breadth
    
    start_lth, end_lth = (int) ((v_length - th_length) / 2) + 4 + 8, (int) (((v_length - th_length) / 2) + th_length) + 3 + 8
    start_bth, end_bth = (int) ((v_breadth - th_breadth) / 2) + 4 + 8, (int) (((v_breadth - th_breadth) / 2) + th_breadth) + 3 + 8
    
    for i in range(v_length + 4 + 8):
        for j in range(v_breadth + 4 + 8):
            if ((i >= start_lth and i <= end_lth) and (j >= start_bth and j <= end_bth)):
                occupied.append((i, j))
                village_occupied["Town Hall"].append((i, j))
            elif (((i == 4 + 8) and (j >= 4 + 8)) or ((j == 4 + 8) and (i >= 4 + 8)) or ((i == v_length + 3 + 8) and (j <= v_breadth + 3 + 8) and not (j < 4 + 8)) or ((j == v_breadth + 3 + 8) and (i <= v_length + 3 + 8) and not (i < 4 + 8))):
                occupied.append((i, j))
                village_occupied["Walls"][(i, j)] = 50
                
            else:
                if ((i < 4 + 8) or (j < 4 + 8)):
                    found = False
                    for point in occupied:
                        if (point == (i, j)):
                            found == True
                            break
                    if (not found):     
                        occupied.append((i, j))
                        village_occupied["Empty Space"].append((i, j))
        
    # The number of huts is passed as an argument when making use of the function.
    for i in range(len(list_of_huts)):

        #This acts as a do-while loop. A value of x and y is initially passed.
        #First it ensures that the 4 places aren't taken up by looking through the list "occupied".
        while True:
            x = randint(5 + 8, v_length + 2 + 8)
            y = randint(5 + 8, v_breadth + 2 + 8)
            #"val" will be a tuple value. 

            applicable_value = True

            #The loop is quit once we're done with all the tuples in occupied and if the condition stays the same, 
            #then, the value is added to the list and the dictionary.
            for val in occupied:
                #Checking for the x-value being occupied or not.
                if (x == val[0]):
                    #If the x-value is occupied, looking through the same for the y-value.
                    if ((y == val[1]) or ((y + 1) == val[1])):
                        #break is applied because we've found the tuple value inside the "occupied" list, hence, no point going on.
                        applicable_value = False
                        break
                elif ((x + 1) == val[0]):
                    if ((y == val[1]) or ((y + 1) == val[1])):
                        #break is applied because we've found the tuple value inside the "occupied" list, hence, no point going on.
                        applicable_value = False
                        break
                else:
                    continue

            if (applicable_value):
                #(x, y) are added to the "village_occupied" dictionary so that we know to add the value while making the map.
                village_occupied["Huts"].append((x, y))
                village_occupied["Huts"].append((x, y + 1))
                village_occupied["Huts"].append((x + 1, y))
                village_occupied["Huts"].append((x + 1, y + 1))
                #(x, y) is added to "occupied" so that when we're making town hall, or cannons, we have the occupied values already.
                occupied.append((x, y))
                occupied.append((x, y + 1))
                occupied.append((x + 1, y))
                occupied.append((x + 1, y + 1))
                #(x, y) is added to the class value of each structure.
                list_of_huts[i].xy = (x, y)
                list_of_huts[i].xy_ = (x, y + 1)
                list_of_huts[i].x_y = (x + 1, y)
                list_of_huts[i].x_y_ = (x + 1, y + 1)
                break
            else:
                continue
            
    # The number of wizard towers is passed as an argument when making use of the function.
    for i in range(len(list_of_wizard_towers)):

        #This acts as a do-while loop. A value of x and y is initially passed.
        #First it ensures that the 4 places aren't taken up by looking through the list "occupied".
        while True:
            x = randint(5 + 8, v_length + 2 + 8)
            y = randint(5 + 8, v_breadth + 2 + 8)
            #"val" will be a tuple value. 

            applicable_value = True

            #The loop is quit once we're done with all the tuples in occupied and if the condition stays the same, 
            #then, the value is added to the list and the dictionary.
            for val in occupied:
                #Checking for the x-value being occupied or not.
                if (x == val[0]):
                    #If the x-value is occupied, looking through the same for the y-value.
                    if ((y == val[1]) or ((y + 1) == val[1])):
                        #break is applied because we've found the tuple value inside the "occupied" list, hence, no point going on.
                        applicable_value = False
                        break
                elif ((x + 1) == val[0]):
                    if ((y == val[1]) or ((y + 1) == val[1])):
                        #break is applied because we've found the tuple value inside the "occupied" list, hence, no point going on.
                        applicable_value = False
                        break
                else:
                    continue

            if (applicable_value):
                #(x, y) are added to the "village_occupied" dictionary so that we know to add the value while making the map.
                village_occupied["Wizard Towers"].append((x, y))
                village_occupied["Wizard Towers"].append((x, y + 1))
                village_occupied["Wizard Towers"].append((x + 1, y))
                village_occupied["Wizard Towers"].append((x + 1, y + 1))
                #(x, y) is added to "occupied" so that when we're making town hall, or cannons, we have the occupied values already.
                occupied.append((x, y))
                occupied.append((x, y + 1))
                occupied.append((x + 1, y))
                occupied.append((x + 1, y + 1))
                #(x, y) is added to the class value of each structure.
                list_of_wizard_towers[i].xy = (x, y)
                list_of_wizard_towers[i].xy_ = (x, y + 1)
                list_of_wizard_towers[i].x_y = (x + 1, y)
                list_of_wizard_towers[i].x_y_ = (x + 1, y + 1)
                break
            else:
                continue

    # The number of cannons is passed as an argument when making use of the function.
    for i in range(len(list_of_cannons)):

        #This acts as a do-while loop. A value of x and y is initially passed.
        #First it ensures that the place isn't taken up by looking through the list "occupied".
        while True:
            x = randint(5 + 8, v_length + 2 + 8)
            y = randint(5 + 8, v_breadth + 2 + 8)
            #"val" will be a tuple value. 

            applicable_value = True

            #The loop is quit once we're done with all the tuples in occupied and if the condition stays the same, 
            #then, the value is added to the list and the dictionary.
            for val in occupied:
                #Checking for the x-value being occupied or not.
                if (x == val[0]):
                    #If the x-value is occupied, looking through the same for the y-value.
                    if (y == val[1]):
                        #break is applied because we've found the tuple value inside the "occupied" list, hence, no point going on.
                        applicable_value = False
                        break
                else:
                    continue

            if (applicable_value):
                #(x, y) are added to the "village_occupied" dictionary so that we know to add the value while making the map.
                village_occupied["Cannons"].append((x, y))
                #(x, y) is added to "occupied" so that when we're making town hall, or huts, we have the occupied values already.
                occupied.append((x, y))
                #(x, y) is adde to the class value of the given structure.
                list_of_cannons[i].xy = (x, y)
                break
            else:
                continue

def printBackground(village, town_hall, list_of_huts, list_of_cannons, list_of_wizard_towers, monarch):
    
    v_length, v_breadth = village.size_length, village.size_breadth
    global king_position, queen_position, barbarian_position, archer_position, character
    
    pob_list1, pob_list2 = [], []
    for barbarian, position in barbarian_position.items():
        pob_list1.append(barbarian)
        pob_list2.append(position)

    poa_list1, poa_list2 = [], []
    for archer, position in archer_position.items():
        poa_list1.append(archer)
        poa_list2.append(position)

    for i in range(v_length + 4 + 8):
        for j in range(v_breadth + 4 + 8):
            printed_occupied = False
            coordinate = (i, j)
            for values in occupied:
                if (coordinate == values):
                    for empty_space_val in village_occupied["Empty Space"]:
                        if (coordinate == empty_space_val):
                            if ((character == 'k') and ((coordinate == king_position) and (monarch.HP > 0))):
                                print(f"{Fore.WHITE + Back.BLACK}K", end = "")
                                Back.RESET
                            if ((character == 'q') and ((coordinate == queen_position) and (monarch.HP > 0))):
                                print(f"{Fore.WHITE + Back.BLACK}Q", end = "")
                                Back.RESET
                            elif ((coordinate in pob_list2) and (pob_list1[pob_list2.index(coordinate)].HP > 0)):
                                print(f"{Fore.WHITE + Back.BLACK}B", end = "")
                                Back.RESET
                            elif ((coordinate in poa_list2) and (poa_list1[poa_list2.index(coordinate)].HP > 0)):
                                print(f"{Fore.WHITE + Back.BLACK}A", end = "")
                                Back.RESET
                            else:
                                print(f"{Back.BLACK} ", end = "")
                                Back.RESET
                            printed_occupied = True
                    for walls_val in village_occupied["Walls"].keys():
                        if ((coordinate == walls_val) and (coordinate in occupied)):
                            print(f"{Fore.BLACK + Back.YELLOW}W",  end = "")
                            Back.RESET
                            printed_occupied = True
                    for town_hall_val in village_occupied["Town Hall"]:
                        if (coordinate == town_hall_val):
                            if (town_hall.HP > 0):
                                print(f"{Fore.BLACK + Back.BLUE}T", end = "")
                                Back.RESET
                                printed_occupied = True
                            else:
                                if ((character == 'k') and ((coordinate == king_position) and (monarch.HP > 0))):
                                    print(f"{Back.GREEN + Fore.BLACK}K", end = "")
                                elif ((character == 'q') and ((coordinate == queen_position) and (monarch.HP > 0))):
                                    print(f"{Back.GREEN + Fore.BLACK}Q", end = "")
                                    Back.RESET
                                elif ((coordinate in pob_list2) and (pob_list1[pob_list2.index(coordinate)].HP > 0)):
                                    print(f"{Fore.BLACK + Back.GREEN}B", end = "")
                                    Back.RESET
                                elif ((coordinate in poa_list2) and (poa_list1[poa_list2.index(coordinate)].HP > 0)):
                                    print(f"{Fore.BLACK + Back.GREEN}A", end = "")
                                    Back.RESET
                                else:
                                    print(f"{Back.GREEN} ", end = "")
                                printed_occupied = True

                    #If it is in the list, then, we check the list of huts (which has the class values).
                    for hut in list_of_huts:
                        #If the HP is 0, then, print GREEN, otherwise, print the hut.
                        if ((coordinate == hut.xy) or (coordinate == hut.xy_) or (coordinate == hut.x_y) or (coordinate == hut.x_y_)):
                            if (hut.HP > 0):     
                                print(f"{Fore.BLACK + Back.MAGENTA}H", end = "")
                                Back.RESET
                                printed_occupied = True
                            else:
                                if ((character == 'k') and ((coordinate == king_position) and (monarch.HP > 0))):
                                    print(f"{Back.GREEN + Fore.BLACK}K", end = "")
                                elif ((character == 'q') and ((coordinate == queen_position) and (monarch.HP > 0))):
                                    print(f"{Back.GREEN + Fore.BLACK}Q", end = "")
                                elif ((coordinate in pob_list2) and (pob_list1[pob_list2.index(coordinate)].HP > 0)):
                                    print(f"{Back.GREEN + Fore.BLACK}B", end = "")
                                    Back.RESET
                                elif ((coordinate in poa_list2) and (poa_list1[poa_list2.index(coordinate)].HP > 0)):
                                    print(f"{Back.GREEN + Fore.BLACK}A", end = "")
                                    Back.RESET
                                else:
                                    print(f"{Back.GREEN} ", end = "")
                                printed_occupied = True

                    #If it is in the list, then, we check the list of wizard_towers (which has the class values).
                    for wizard_tower in list_of_wizard_towers:
                        #If the HP is 0, then, print GREEN, otherwise, print the wizard_tower.
                        if ((coordinate == wizard_tower.xy) or (coordinate == wizard_tower.xy_) or (coordinate == wizard_tower.x_y) or (coordinate == wizard_tower.x_y_)):
                            if (wizard_tower.HP > 0):     
                                print(f"{Fore.MAGENTA + Back.BLUE}W", end = "")
                                Back.RESET
                                printed_occupied = True
                            else:
                                if ((character == 'k') and ((coordinate == king_position) and (monarch.HP > 0))):
                                    print(f"{Back.GREEN + Fore.BLACK}K", end = "")
                                elif ((character == 'q') and ((coordinate == queen_position) and (monarch.HP > 0))):
                                    print(f"{Back.GREEN + Fore.BLACK}Q", end = "")
                                elif ((coordinate in pob_list2) and (pob_list1[pob_list2.index(coordinate)].HP > 0)):
                                    print(f"{Back.GREEN + Fore.BLACK}B", end = "")
                                    Back.RESET
                                elif ((coordinate in poa_list2) and (poa_list1[poa_list2.index(coordinate)].HP > 0)):
                                    print(f"{Back.GREEN + Fore.BLACK}A", end = "")
                                    Back.RESET
                                else:
                                    print(f"{Back.GREEN} ", end = "")
                                printed_occupied = True

                    #If it is in the list, then, we check the list of cannons (which has the class values).
                    for cannon in list_of_cannons:
                        #If the HP is 0, then, print GREEN, otherwise, print the cannon.
                        if (coordinate == cannon.xy):
                            if (cannon.HP > 0):                            
                                print(f"{Fore.BLACK + Back.RED}C", end = "")
                                Back.RESET
                                printed_occupied = True
                            else:
                                if ((character == 'k') and ((coordinate == king_position) and (monarch.HP > 0))):
                                    print(f"{Back.GREEN + Fore.BLACK}K", end = "")
                                elif ((character == 'q') and ((coordinate == queen_position) and (monarch.HP > 0))):
                                    print(f"{Back.GREEN + Fore.BLACK}Q", end = "")
                                    Back.RESET
                                elif ((coordinate in pob_list2) and (pob_list1[pob_list2.index(coordinate)].HP > 0)):
                                    print(f"{Back.GREEN + Fore.BLACK}B", end = "")
                                    Back.RESET
                                elif ((coordinate in poa_list2) and (poa_list1[poa_list2.index(coordinate)].HP > 0)):
                                    print(f"{Back.GREEN + Fore.BLACK}A", end = "")
                                    Back.RESET
                                else:
                                    print(f"{Back.GREEN} ", end = "")
                                printed_occupied = True
                else:
                    continue
            if (not printed_occupied):
                if ((character == 'k') and ((coordinate == king_position) and (monarch.HP > 0))):
                    print(f"{Back.GREEN + Fore.BLACK}K", end = "")
                elif ((character == 'q') and ((coordinate == queen_position) and (monarch.HP > 0))):
                    print(f"{Back.GREEN + Fore.BLACK}Q", end = "")
                    Back.RESET
                elif ((coordinate in pob_list2) and (pob_list1[pob_list2.index(coordinate)].HP > 0)):
                    print(f"{Back.GREEN + Fore.BLACK}B", end = "")
                    Back.RESET
                elif ((coordinate in poa_list2) and (poa_list1[poa_list2.index(coordinate)].HP > 0)):
                    print(f"{Back.GREEN + Fore.BLACK}A", end = "")
                    Back.RESET
                else:
                    print(f"{Back.GREEN} ", end = "")
            else:
                continue
        print("")

def printStats(town_hall, list_of_huts, list_of_cannons, list_of_wizard_towers, monarch, list_of_barbarians, list_of_archers):
    
    global character

    print("Town Hall: ", end = "")
    HP_percentage_remaining = (int) (100 * (town_hall.HP / town_hall.totalHP))
    if (HP_percentage_remaining > 70):
        for i in range(HP_percentage_remaining):
            print(f"{Fore.GREEN}|", end="")
    elif (HP_percentage_remaining > 40):
        for i in range(HP_percentage_remaining):
            print(f"{Fore.YELLOW}|", end="")
    elif (HP_percentage_remaining == 0):
        print(f"{Fore.RED}The structure has been destroyed completely.", end="")
    else:
        for i in range(HP_percentage_remaining):
            print(f"{Fore.RED}|", end="")
            
    print("")
    
    for hut_num in range(len(list_of_huts)):
        print("Hut", str(list_of_huts[hut_num].hut_number) + ":", end="")
        HP_percentage_remaining = (int) (100 * (list_of_huts[hut_num].HP / list_of_huts[hut_num].totalHP))
        if (HP_percentage_remaining > 70):
            for i in range(HP_percentage_remaining):
                print(f"{Fore.GREEN}|", end="")
        elif (HP_percentage_remaining > 40):
            for i in range(HP_percentage_remaining):
                print(f"{Fore.YELLOW}|", end="")
        elif (HP_percentage_remaining == 0):
            print(f"{Fore.RED}The structure has been destroyed completely.", end="")
        else:
            for i in range(HP_percentage_remaining):
                print(f"{Fore.RED}|", end="")
        print("")
                
    for cannon_num in range(len(list_of_cannons)):
        print("Cannon", str(list_of_cannons[cannon_num].cannon_number) + ":", end="")
        HP_percentage_remaining = (int) (100 * (list_of_cannons[cannon_num].HP / list_of_cannons[cannon_num].totalHP))
        if (HP_percentage_remaining > 70):
            for i in range(HP_percentage_remaining):
                print(f"{Fore.GREEN}|", end="")
        elif (HP_percentage_remaining > 40):
            for i in range(HP_percentage_remaining):
                print(f"{Fore.YELLOW}|", end="")
        elif (HP_percentage_remaining == 0):
            print(f"{Fore.RED}The structure has been destroyed completely.", end="")
        else:
            for i in range(HP_percentage_remaining):
                print(f"{Fore.RED}|", end="")
        print("")

    for wizard_tower_num in range(len(list_of_wizard_towers)):
        print("Wizard Tower", str(list_of_wizard_towers[wizard_tower_num].wizard_tower_number) + ":", end="")
        HP_percentage_remaining = (int) (100 * (list_of_wizard_towers[wizard_tower_num].HP / list_of_wizard_towers[wizard_tower_num].totalHP))
        if (HP_percentage_remaining > 70):
            for i in range(HP_percentage_remaining):
                print(f"{Fore.GREEN}|", end="")
        elif (HP_percentage_remaining > 40):
            for i in range(HP_percentage_remaining):
                print(f"{Fore.YELLOW}|", end="")
        elif (HP_percentage_remaining == 0):
            print(f"{Fore.RED}The structure has been destroyed completely.", end="")
        else:
            for i in range(HP_percentage_remaining):
                print(f"{Fore.RED}|", end="")
        print("")
    
    print("\n")
    
    if (character == 'k'):
        print("King: ", end = "")
        HP_percentage_remaining = (int) (100 * (monarch.HP / monarch.totalHP))
        if (HP_percentage_remaining > 70):
            for i in range(HP_percentage_remaining):
                print(f"{Fore.GREEN}|", end="")
        elif (HP_percentage_remaining > 40):
            for i in range(HP_percentage_remaining):
                print(f"{Fore.YELLOW}|", end="")
        elif (HP_percentage_remaining <= 0):
            print(f"{Fore.RED}THE KING IS DEAD.", end="")
        else:
            for i in range(HP_percentage_remaining):
                print(f"{Fore.RED}|", end="")
    elif (character == 'q'):
        print("Queen: ", end = "")
        HP_percentage_remaining = (int) (100 * (monarch.HP / monarch.totalHP))
        if (HP_percentage_remaining > 70):
            for i in range(HP_percentage_remaining):
                print(f"{Fore.GREEN}|", end="")
        elif (HP_percentage_remaining > 40):
            for i in range(HP_percentage_remaining):
                print(f"{Fore.YELLOW}|", end="")
        elif (HP_percentage_remaining <= 0):
            print(f"{Fore.RED}THE QUEEN IS DEAD.", end="")
        else:
            for i in range(HP_percentage_remaining):
                print(f"{Fore.RED}|", end="")
            
    print("")

    for barbarian_num in range(len(list_of_barbarians)):
        print("Barbarian", str(list_of_barbarians[barbarian_num].barbarian_number) + ":", end="")
        HP_percentage_remaining = (int) (100 * (list_of_barbarians[barbarian_num].HP / list_of_barbarians[barbarian_num].totalHP))
        if (HP_percentage_remaining > 70):
            for i in range(HP_percentage_remaining):
                print(f"{Fore.GREEN}|", end="")
        elif (HP_percentage_remaining > 40):
            for i in range(HP_percentage_remaining):
                print(f"{Fore.YELLOW}|", end="")
        elif (HP_percentage_remaining == 0):
            print(f"{Fore.RED}The soldier has fallen.", end="")
        else:
            for i in range(HP_percentage_remaining):
                print(f"{Fore.RED}|", end="")
        print("")
        
    for archer_num in range(len(list_of_archers)):
        print("Archer", str(list_of_archers[archer_num].archer_number) + ":", end="")
        HP_percentage_remaining = (int) (100 * (list_of_archers[archer_num].HP / list_of_archers[archer_num].totalHP))
        if (HP_percentage_remaining > 70):
            for i in range(HP_percentage_remaining):
                print(f"{Fore.GREEN}|", end="")
        elif (HP_percentage_remaining > 40):
            for i in range(HP_percentage_remaining):
                print(f"{Fore.YELLOW}|", end="")
        elif (HP_percentage_remaining == 0):
            print(f"{Fore.RED}This soldier has fallen.", end="")
        else:
            for i in range(HP_percentage_remaining):
                print(f"{Fore.RED}|", end="")
        print("")

def rage_spell(monarch, list_of_barbarians, list_of_archers):

    
    monarch.damage = monarch.damage * 2
    monarch.movement_speed = monarch.movement_speed * 2
    
    for barbarian in list_of_barbarians:
        barbarian.damage = barbarian.damage * 2
        barbarian.movement_speed = barbarian.movement_speed * 2
        
    for archer in list_of_archers:
        archer.damage = archer.damage * 2
        archer.movement_speed = archer.movement_speed * 2

def heal_spell(monarch, list_of_barbarians, list_of_archers):
# def heal_spell(monarch, list_of_barbarians, list_of_archers, list_of_balloons):
    
    if (monarch.HP > 0):
        if (((int) (monarch.HP * (1.5))) >= monarch.totalHP):
            monarch.HP = monarch.totalHP
        else:
            monarch.HP = (int) (monarch.HP * (1.5))
    
    for barbarian in list_of_barbarians:
        if (barbarian.HP > 0):
            if (((int) (barbarian.HP * (1.5))) >= barbarian.totalHP):
                barbarian.HP = barbarian.totalHP
            else:
                barbarian.HP = (int) (barbarian.HP * (1.5))
    
    for archer in list_of_archers:
        if (archer.HP > 0):
            if (((int) (archer.HP * (1.5))) >= archer.totalHP):
                archer.HP = archer.totalHP
            else:
                archer.HP = (int) (archer.HP * (1.5))
            
def king_attack(king, list_of_barbarians, list_of_archers, town_hall, list_of_huts, list_of_cannons, list_of_wizard_towers):

    global king_position, village_occupied, occupied
    for wizard_tower in list_of_wizard_towers:
        print(wizard_tower.xy)

    try:
        if (town_hall.HP > 0):
            for coordinate in village_occupied["Town Hall"]:
                if (king_position[0] == coordinate[0]):
                    if ((king_position[1] == (coordinate[1] - 1)) or (king_position[1] == (coordinate[1] + 1))):
                        if (town_hall.HP <= king.damage):
                            print("The king dealt a damage of", town_hall.HP, "on the town hall and destroyed the structure.")
                            town_hall.HP = 0
                        else:                
                            print("The king dealt a damage of", king.damage, "on the town hall.")
                            town_hall.HP -= king.damage
                if (king_position[1] == coordinate[1]):
                    if ((king_position[0] == (coordinate[0] - 1)) or (king_position[0] == (coordinate[0] + 1))):
                        if (town_hall.HP <= king.damage):
                            print("The king dealt a damage of", town_hall.HP, "on the town hall and destroyed the structure.")
                            town_hall.HP = 0
                        else:                
                            print("The king dealt a damage of", king.damage, "on the town hall.")
                            town_hall.HP -= king.damage

        if (town_hall.HP == 0):
            for coordinate in village_occupied["Town Hall"]:
                occupied.remove(coordinate)
            village_occupied["Town Hall"].clear()
            # check_situation(town_hall, list_of_huts, list_of_cannons, list_of_wizard_towers, king, list_of_barbarians, list_of_archers)

        for wizard_tower in list_of_wizard_towers:
            
            if (((king_position[0] == (wizard_tower.xy[0] - 1)) and (king_position[1] == wizard_tower.xy[1])) or 
            ((king_position[0] == (wizard_tower.x_y[0] + 1)) and (king_position[1] == wizard_tower.x_y[1])) or 
            ((king_position[0] == (wizard_tower.xy_[0] - 1)) and (king_position[1] == wizard_tower.xy_[1])) or 
            ((king_position[0] == (wizard_tower.x_y_[0] + 1)) and (king_position[1] == wizard_tower.x_y_[1])) or 
            ((king_position[0] == wizard_tower.xy_[0]) and (king_position[1] == (wizard_tower.xy_[1] + 1))) or 
            ((king_position[0] == wizard_tower.x_y_[0]) and (king_position[1] == (wizard_tower.x_y_[1] + 1))) or 
            ((king_position[0] == wizard_tower.xy[0]) and (king_position[1] == (wizard_tower.xy[1] - 1))) or 
            ((king_position[0] == wizard_tower.x_y[0]) and (king_position[1] == (wizard_tower.x_y[1] - 1)))):
                if (wizard_tower.HP <= king.damage):
                    print("The king dealt a damage of", wizard_tower.HP, "on a wizard_tower and destroyed the structure.")
                    wizard_tower.HP = 0
                    occupied.remove(wizard_tower.xy)
                    village_occupied["Wizard Towers"].remove(wizard_tower.xy)
                    occupied.remove(wizard_tower.x_y)
                    village_occupied["Wizard Towers"].remove(wizard_tower.x_y)
                    occupied.remove(wizard_tower.xy_)
                    village_occupied["Wizard Towers"].remove(wizard_tower.xy_)
                    occupied.remove(wizard_tower.x_y_)
                    village_occupied["Wizard Towers"].remove(wizard_tower.x_y_)
                    # check_situation(town_hall, list_of_huts, list_of_cannons, list_of_wizard_towers, king, list_of_barbarians, list_of_archers)
                    break
                else:                
                    print("The king dealt a damage of", king.damage, "on a wizard_tower.")
                    wizard_tower.HP -= king.damage
            else:
                continue

        for hut in list_of_huts:
        
            if (((king_position[0] == (hut.xy[0] - 1)) and (king_position[1] == hut.xy[1])) 
            or ((king_position[0] == hut.xy[0]) and (king_position[1] == (hut.xy[1] - 1))) 
            or ((king_position[0] == (hut.x_y[0] + 1)) and (king_position[1] == hut.x_y[1])) 
            or ((king_position[0] == hut.x_y[0]) and (king_position[1] == (hut.x_y[1] - 1)))
            or ((king_position[0] == (hut.xy_[0] - 1)) and (king_position[1] == hut.xy_[1])) 
            or ((king_position[0] == hut.xy_[0]) and (king_position[1] == (hut.xy_[1] + 1))) 
            or ((king_position[0] == (hut.x_y_[0] + 1)) and (king_position[1] == hut.x_y_[1])) 
            or ((king_position[0] == hut.x_y_[0]) and (king_position[1] == (hut.x_y_[1] + 1)))):
                if (hut.HP <= king.damage):
                    print("The king dealt a damage of", hut.HP, "on a hut and destroyed the structure.")
                    hut.HP = 0
                    occupied.remove(hut.xy)
                    village_occupied["Huts"].remove(hut.xy)
                    occupied.remove(hut.x_y)
                    village_occupied["Huts"].remove(hut.x_y)
                    occupied.remove(hut.xy_)
                    village_occupied["Huts"].remove(hut.xy_)
                    occupied.remove(hut.x_y_)
                    village_occupied["Huts"].remove(hut.x_y_)
                    # check_situation(town_hall, list_of_huts, list_of_cannons, list_of_wizard_towers, king, list_of_barbarians, list_of_archers)
                    break
                else:                
                    print("The king dealt a damage of", king.damage, "on a hut.")
                    hut.HP -= king.damage

        for cannon in list_of_cannons:
            if (((king_position[0] == (cannon.xy[0] - 1)) and (king_position[1] == cannon.xy[1])) or ((king_position[0] == (cannon.xy[0] + 1)) and (king_position[1] == cannon.xy[1])) or ((king_position[0] == cannon.xy[0]) and (king_position[1] == (cannon.xy[1] - 1))) or ((king_position[0] == cannon.xy[0]) and (king_position[1] == (cannon.xy[1] + 1)))):
                if (cannon.HP <= king.damage):
                    print("The king dealt a damage of", cannon.HP, "on a cannon and destroyed the structure.")
                    cannon.HP = 0
                    occupied.remove(cannon.xy)
                    village_occupied["Cannons"].remove(cannon.xy)
                    # check_situation(town_hall, list_of_huts, list_of_cannons, king, list_of_barbarians)
                    break
                else:                
                    print("The king dealt a damage of", king.damage, "on a cannon.")
                    cannon.HP -= king.damage

        for wall, HP in village_occupied["Walls"].items():
            if (((king_position[0] == (wall[0] - 1)) and (king_position[1] == wall[1])) or ((king_position[0] == (wall[0] - 1)) and (king_position[1] == wall[1])) or ((king_position[0] == (wall[0] + 1)) and (king_position[1] == wall[1])) or ((king_position[0] == (wall[0] + 1)) and (king_position[1] == wall[1])) or ((king_position[0] == wall[0]) and (king_position[1] == (wall[1] - 1))) or ((king_position[0] == wall[0]) and (king_position[1] == (wall[1] + 1))) or ((king_position[0] == wall[0]) and (king_position[1] == (wall[1] - 1))) or ((king_position[0] == wall[0]) and (king_position[1] == (wall[1] + 1)))):
                print(wall)
                if (HP <= king.damage):
                    print("The king dealt a damage of", HP, "on a wall and destroyed the structure.")
                    village_occupied["Walls"][wall] = 0
                    del village_occupied["Walls"][wall]
                    occupied.remove(wall)
                    break
                else:
                    print("The king dealt a damage of", king.damage, "on a wall")
                    village_occupied["Walls"][wall] -= king.damage

    except ValueError:
        print("Slow down. Move about.")
        
    except IndexError:
        print("The king is not on the field yet. Spawn him.")

def queen_attack(queen, list_of_barbarians, list_of_archers, town_hall, list_of_huts, list_of_cannons, list_of_wizard_towers):
    
    global queen_position, village_occupied, occupied

    try:
        
        four_points = [(list(queen_position)[0] - queen.center_distance, list(queen_position)[1]), 
                        (list(queen_position)[0] + queen.center_distance, list(queen_position)[1]), 
                        (list(queen_position)[0], list(queen_position)[1] - queen.center_distance),
                        (list(queen_position)[0], list(queen_position)[1] + queen.center_distance)]
        
        queen_possible_attack = []
        
        for point in four_points:
            
            point = list(point)
            
            for i in range(point[0] - queen.range, point[0] + queen.range + 1): 
                for j in range(point[1] - queen.range, point[1] + queen.range + 1):
                    queen_possible_attack.append((i, j))
        
            point = tuple(point)


        if (town_hall.HP > 0):
            for coordinate in village_occupied["Town Hall"]:
                
                if (coordinate in queen_possible_attack):
                    if (town_hall.HP <= queen.damage):
                        print("The queen dealt a damage of", town_hall.HP, "on the town hall and destroyed the structure.")
                        town_hall.HP = 0
                    else:                
                        print("The queen dealt a damage of", queen.damage, "on the town hall.")
                        town_hall.HP -= queen.damage

        if (town_hall.HP == 0):
            for coordinate in village_occupied["Town Hall"]:
                occupied.remove(coordinate)
            village_occupied["Town Hall"].clear()
            # check_situation(town_hall, list_of_huts, list_of_cannons, queen, list_of_barbarians)

        for wizard_tower in list_of_wizard_towers:
            
            if ((wizard_tower.xy in queen_possible_attack) or (wizard_tower.x_y in queen_possible_attack) or (wizard_tower.xy_ in queen_possible_attack) or (wizard_tower.x_y_ in queen_possible_attack)):
                if (wizard_tower.HP <= queen.damage):
                    print("The queen dealt a damage of", wizard_tower.HP, "on a wizard tower and destroyed the structure.")
                    wizard_tower.HP = 0
                    occupied.remove(wizard_tower.xy)
                    village_occupied["Wizard Towers"].remove(wizard_tower.xy)
                    occupied.remove(wizard_tower.x_y)
                    village_occupied["Wizard Towers"].remove(wizard_tower.x_y)
                    occupied.remove(wizard_tower.xy_)
                    village_occupied["Wizard Towers"].remove(wizard_tower.xy_)
                    occupied.remove(wizard_tower.x_y_)
                    village_occupied["Wizard Towers"].remove(wizard_tower.x_y_)
                    # check_situation(town_hall, list_of_huts, list_of_cannons, list_of_wizard_towers, queen, list_of_barbarians)
                    break
                else:                
                    print("The queen dealt a damage of", queen.damage, "on a wizard tower.")
                    wizard_tower.HP -= queen.damage

        for hut in list_of_huts:
        
            if ((hut.xy in queen_possible_attack) or (hut.x_y in queen_possible_attack) or (hut.xy_ in queen_possible_attack) or (hut.x_y_ in queen_possible_attack)):
                if (hut.HP <= queen.damage):
                    print("The queen dealt a damage of", hut.HP, "on a hut and destroyed the structure.")
                    hut.HP = 0
                    occupied.remove(hut.xy)
                    village_occupied["Huts"].remove(hut.xy)
                    occupied.remove(hut.x_y)
                    village_occupied["Huts"].remove(hut.x_y)
                    occupied.remove(hut.xy_)
                    village_occupied["Huts"].remove(hut.xy_)
                    occupied.remove(hut.x_y_)
                    village_occupied["Huts"].remove(hut.x_y_)
                    # check_situation(town_hall, list_of_huts, list_of_cannons, list_of_wizard_towers, queen, list_of_barbarians)
                    break
                else:                
                    print("The queen dealt a damage of", queen.damage, "on a hut.")
                    hut.HP -= queen.damage

        for cannon in list_of_cannons:
            if (cannon.xy in queen_possible_attack):
                if (cannon.HP <= queen.damage):
                    print("The queen dealt a damage of", cannon.HP, "on a cannon and destroyed the structure.")
                    cannon.HP = 0
                    occupied.remove(cannon.xy)
                    village_occupied["Cannons"].remove(cannon.xy)
                    # check_situation(town_hall, list_of_huts, list_of_cannons, list_of_wizard_towers, queen, list_of_barbarians)
                    break
                else:                
                    print("The queen dealt a damage of", queen.damage, "on a cannon.")
                    cannon.HP -= queen.damage

        for wall, HP in village_occupied["Walls"].items():
            if (wall in queen_possible_attack):
                if (HP <= queen.damage):
                    print("The queen dealt a damage of", HP, "on a wall and destroyed the structure.")
                    village_occupied["Walls"][wall] = 0
                    del village_occupied["Walls"][wall]
                    occupied.remove(wall)
                    break
                else:
                    print("The queen dealt a damage of", queen.damage, "on a wall")
                    village_occupied["Walls"][wall] -= queen.damage

    except ValueError:
        print("Slow down. Move about.")
        
    except IndexError:
        print("The queen is not on the field yet. Spawn her.")

def barbarian_attack(monarch, list_of_barbarians, list_of_archers, town_hall, list_of_huts, list_of_cannons, list_of_wizard_towers):
    
    global barbarian_position, village_occupied, occupied

    try:
        for barbarian, position in barbarian_position.items(): 
            # print(town_hall, town_hall.HP)
            if (town_hall.HP > 0):
                for coordinate in village_occupied["Town Hall"]:
                    if (position[0] == coordinate[0]):
                        if ((position[1] == (coordinate[1] - 1)) or (position[1] == (coordinate[1] + 1))):
                            if (town_hall.HP < barbarian.damage):
                                # print("The barbarian dealt a damage of", town_hall.HP, "on the town hall and destroyed the structure.")
                                town_hall.HP = 0
                            else:                
                                # print("The barbarian dealt a damage of", barbarian.damage, "on the town hall.")
                                town_hall.HP -= barbarian.damage
                    if (position[1] == coordinate[1]):
                        if ((position[0] == (coordinate[0] - 1)) or (position[0] == (coordinate[0] + 1))):
                            if (town_hall.HP < barbarian.damage):
                                # print("The barbarian dealt a damage of", town_hall.HP, "on the town hall and destroyed the structure.")
                                town_hall.HP = 0
                            else:                
                                # print("The barbarian dealt a damage of", barbarian.damage, "on the town hall.")
                                town_hall.HP -= barbarian.damage

            if (town_hall.HP == 0):
                for coordinate in village_occupied["Town Hall"]:
                    occupied.remove(coordinate)
                village_occupied["Town Hall"].clear()

            for hut in list_of_huts:
                
                if (((position[0] == (hut.xy[0] - 1)) and (position[1] == hut.xy[1])) 
                or ((position[0] == (hut.x_y[0] + 1)) and (position[1] == hut.x_y[1])) 
                or ((position[0] == (hut.xy_[0] - 1)) and (position[1] == hut.xy_[1])) 
                or ((position[0] == (hut.x_y_[0] + 1)) and (position[1] == hut.x_y_[1])) 
                or ((position[0] == hut.xy_[0]) and (position[1] == (hut.xy_[1] + 1))) 
                or ((position[0] == hut.x_y_[0]) and (position[1] == (hut.x_y_[1] + 1))) 
                or ((position[0] == hut.xy[0]) and (position[1] == (hut.xy[1] - 1))) 
                or ((position[0] == hut.x_y[0]) and (position[1] == (hut.x_y[1] - 1)))):
                    if (hut.HP < barbarian.damage):
                        # print("The barbarian dealt a damage of", hut.HP, "on a hut and destroyed the structure.")
                        hut.HP = 0
                        occupied.remove(hut.xy)
                        village_occupied["Huts"].remove(hut.xy)
                        occupied.remove(hut.x_y)
                        village_occupied["Huts"].remove(hut.x_y)
                        occupied.remove(hut.xy_)
                        village_occupied["Huts"].remove(hut.xy_)
                        occupied.remove(hut.x_y_)
                        village_occupied["Huts"].remove(hut.x_y_)
                        # check_situation(town_hall, list_of_huts, list_of_cannons, list_of_wizard_towers, monarch, list_of_barbarians, list_of_archers)
                        break
                    else:                
                        # print("The barbarian dealt a damage of", barbarian.damage, "on a hut.")
                        hut.HP -= barbarian.damage

            for wizard_tower in list_of_wizard_towers:
                
                if (((position[0] == (wizard_tower.xy[0] - 1)) and (position[1] == wizard_tower.xy[1])) 
                or ((position[0] == (wizard_tower.x_y[0] + 1)) and (position[1] == wizard_tower.x_y[1])) 
                or ((position[0] == (wizard_tower.xy_[0] - 1)) and (position[1] == wizard_tower.xy_[1])) 
                or ((position[0] == (wizard_tower.x_y_[0] + 1)) and (position[1] == wizard_tower.x_y_[1])) 
                or ((position[0] == wizard_tower.xy_[0]) and (position[1] == (wizard_tower.xy_[1] + 1))) 
                or ((position[0] == wizard_tower.x_y_[0]) and (position[1] == (wizard_tower.x_y_[1] + 1))) 
                or ((position[0] == wizard_tower.xy[0]) and (position[1] == (wizard_tower.xy[1] - 1))) 
                or ((position[0] == wizard_tower.x_y[0]) and (position[1] == (wizard_tower.x_y[1] - 1)))):
                    if (wizard_tower.HP < barbarian.damage):
                        # print("The barbarian dealt a damage of", wizard_tower.HP, "on a wizard_tower and destroyed the structure.")
                        wizard_tower.HP = 0
                        occupied.remove(wizard_tower.xy)
                        village_occupied["Huts"].remove(wizard_tower.xy)
                        occupied.remove(wizard_tower.x_y)
                        village_occupied["Huts"].remove(wizard_tower.x_y)
                        occupied.remove(wizard_tower.xy_)
                        village_occupied["Huts"].remove(wizard_tower.xy_)
                        occupied.remove(wizard_tower.x_y_)
                        village_occupied["Huts"].remove(wizard_tower.x_y_)
                        # check_situation(town_hall, list_of_huts, list_of_cannons, list_of_wizard_towers, monarch, list_of_barbarians, list_of_archers)
                        break
                    else:                
                        # print("The barbarian dealt a damage of", barbarian.damage, "on a wizard_tower.")
                        wizard_tower.HP -= barbarian.damage

            for cannon in list_of_cannons:
                if (((position[0] == (cannon.xy[0] - 1)) and (position[1] == cannon.xy[1])) or ((position[0] == (cannon.xy[0] + 1)) and (position[1] == cannon.xy[1])) or ((position[0] == cannon.xy[0]) and (position[1] == (cannon.xy[1] - 1))) or ((position[0] == cannon.xy[0]) and (position[1] == (cannon.xy[1] + 1)))):
                    if (cannon.HP < barbarian.damage):
                        # print("The barbarian dealt a damage of", cannon.HP, "on a cannon and destroyed the structure.")
                        cannon.HP = 0
                        occupied.remove(cannon.xy)
                        village_occupied["Cannons"].remove(cannon.xy)
                        # check_situation(town_hall, list_of_huts, list_of_cannons, list_of_wizard_towers, monarch, list_of_barbarians, list_of_archers)
                        break
                    else:                
                        # print("The barbarian dealt a damage of", barbarian.damage, "on a cannon.")
                        cannon.HP -= barbarian.damage

            for wall, HP in village_occupied["Walls"].items():
                if (((position[0] == (wall[0] - 1)) and (position[1] == wall[1])) or ((position[0] == (wall[0] - 1)) and (position[1] == wall[1])) or ((position[0] == (wall[0] + 1)) and (position[1] == wall[1])) or ((position[0] == (wall[0] + 1)) and (position[1] == wall[1])) or ((position[0] == wall[0]) and (position[1] == (wall[1] - 1))) or ((position[0] == wall[0]) and (position[1] == (wall[1] + 1))) or ((position[0] == wall[0]) and (position[1] == (wall[1] - 1))) or ((position[0] == wall[0]) and (position[1] == (wall[1] + 1)))):
                    # print(wall)
                    if (HP < barbarian.damage):
                        # print("The barbarian dealt a damage of", HP, "on a wall and destroyed the structure.")
                        village_occupied["Walls"][wall] = 0
                        del village_occupied["Walls"][wall]
                        occupied.remove(wall)
                        break
                    else:
                        # print("The barbarian dealt a damage of", barbarian.damage, "on a wall")
                        village_occupied["Walls"][wall] -= barbarian.damage

    except ValueError:
        ("Barbarian error. Will be taken care of.")
        
def archer_attack(monarch, list_of_barbarians, list_of_archers, town_hall, list_of_huts, list_of_cannons, list_of_wizard_towers):
    
    global archer_position, village_occupied, occupied

    try:
        for archer, position in archer_position.items():

            archer_possible_attack = []

            for i in range(position[0] - archer.range, position[0] + archer.range + 1): 
                for j in range(position[1] - archer.range, position[1] + archer.range + 1):
                    archer_possible_attack.append((i, j))
                    
            if (town_hall.HP > 0):
                for coordinate in village_occupied["Town Hall"]:
                    if (coordinate in archer_possible_attack):
                        if (town_hall.HP < archer.damage):
                            town_hall.HP = 0
                        else:
                            town_hall.HP -= archer.damage

            if (town_hall.HP == 0):
                for coordinate in village_occupied["Town Hall"]:
                    occupied.remove(coordinate)
                village_occupied["Town Hall"].clear()

            for hut in list_of_huts:
                if ((hut.xy in archer_possible_attack) or (hut.x_y in archer_possible_attack) or (hut.xy_ in archer_possible_attack) or (hut.x_y_ in archer_possible_attack)):
                    if (hut.HP < archer.damage):
                        # print("The barbarian dealt a damage of", hut.HP, "on a hut and destroyed the structure.")
                        hut.HP = 0
                        occupied.remove(hut.xy)
                        village_occupied["Huts"].remove(hut.xy)
                        occupied.remove(hut.x_y)
                        village_occupied["Huts"].remove(hut.x_y)
                        occupied.remove(hut.xy_)
                        village_occupied["Huts"].remove(hut.xy_)
                        occupied.remove(hut.x_y_)
                        village_occupied["Huts"].remove(hut.x_y_)
                        # check_situation(town_hall, list_of_huts, list_of_cannons, list_of_wizard_towers, monarch, list_of_barbarians, list_of_archers)
                        break
                    else:                
                        # print("The barbarian dealt a damage of", barbarian.damage, "on a hut.")
                        hut.HP -= archer.damage

            for wizard_tower in list_of_wizard_towers:
                if ((wizard_tower.xy in archer_possible_attack) or (wizard_tower.x_y in archer_possible_attack) or (wizard_tower.xy_ in archer_possible_attack) or (wizard_tower.x_y_ in archer_possible_attack)):
                    if (wizard_tower.HP < archer.damage):
                        wizard_tower.HP = 0
                        occupied.remove(wizard_tower.xy)
                        village_occupied["Wizard Towers"].remove(wizard_tower.xy)
                        occupied.remove(wizard_tower.x_y)
                        village_occupied["Wizard Towers"].remove(wizard_tower.x_y)
                        occupied.remove(wizard_tower.xy_)
                        village_occupied["Wizard Towers"].remove(wizard_tower.xy_)
                        occupied.remove(wizard_tower.x_y_)
                        village_occupied["Wizard Towers"].remove(wizard_tower.x_y_)
                        break
                    else:                
                        wizard_tower.HP -= archer.damage

            for cannon in list_of_cannons:
                if (cannon.xy in archer_possible_attack):
                    if (cannon.HP < archer.damage):
                        cannon.HP = 0
                        occupied.remove(cannon.xy)
                        village_occupied["Cannons"].remove(cannon.xy)
                        break
                    else:                
                        cannon.HP -= archer.damage

            if ((position[0] < 12) or (position[1] < 12)):
                for wall, HP in village_occupied["Walls"].items():
                    if (wall in archer_possible_attack):
                        if (HP < archer.damage):
                            village_occupied["Walls"][wall] = 0
                            del village_occupied["Walls"][wall]
                            occupied.remove(wall)
                            break
                        else:
                            village_occupied["Walls"][wall] -= archer.damage

    except ValueError:
        ("Archer error. Will be taken care of.")
    
def cannon_attack(list_of_cannons, monarch):
    
    global king_position, queen_position, barbarian_position, cannon_done, archer_position
    
    attack_done = False

    for cannon in list_of_cannons:
    
        cannon_possible_attack = []
        
        # print(f"{Fore.WHITE + Back.BLACK}Cannon at {cannon.xy} has the following: ", end = "")
        # Back.RESET
        for i in range(cannon.xy[0] - cannon.range, cannon.xy[0] + cannon.range + 1):
            for j in range(cannon.xy[1] - cannon.range, cannon.xy[1] + cannon.range + 1):
                cannon_possible_attack.append((i, j))
        
        # print(cannon_possible_attack)

        if ((king_position in cannon_possible_attack) and (cannon.HP != 0)):
            if (monarch.HP > cannon.damage):
                monarch.HP -= cannon.damage
            else:
                monarch.HP = 0
            attack_done = True
            break
        if ((queen_position in cannon_possible_attack) and (cannon.HP != 0)):
            if (monarch.HP > cannon.damage):
                monarch.HP -= cannon.damage
            else:
                monarch.HP = 0
            attack_done = True
            break
        for barbarian, a_barbarian_position in barbarian_position.items():
            if ((a_barbarian_position in cannon_possible_attack) and (cannon.HP != 0)):
                if (barbarian.HP > cannon.damage):
                    barbarian.HP -= cannon.damage
                else:
                    barbarian.HP = 0
                attack_done = True
                break
        for archer, an_archer_position in archer_position.items():
            if ((an_archer_position in cannon_possible_attack) and (cannon.HP != 0)):
                if (archer.HP > cannon.damage):
                    archer.HP = 0
                    archer.HP -= cannon.damage
                else:
                    archer.HP = 0
                attack_done = True
                break

        if (attack_done):
            break

    cannon_done = True
    
def wizard_tower_attack(list_of_wizard_towers, monarch):
    
    global king_position, queen_position, barbarian_position, wizard_tower_done, archer_position
    
    attack_done = False
    
    for wizard_tower in list_of_wizard_towers:
    
        wizard_tower_possible_attack = []
        
        for i in range(wizard_tower.xy[0] - wizard_tower.range, wizard_tower.xy[0] + wizard_tower.range + 1): 
            for j in range(wizard_tower.xy[1] - wizard_tower.range, wizard_tower.xy[1] + wizard_tower.range + 1):
                wizard_tower_possible_attack.append((i, j))
                
        if ((king_position in wizard_tower_possible_attack) and (wizard_tower.HP != 0)):
            
            area_possible_attack = []

            for i in range(king_position[0] - wizard_tower.area, king_position[0] + wizard_tower.area + 1): 
                for j in range(king_position[1] - wizard_tower.area, king_position[1] + wizard_tower.area + 1):
                    area_possible_attack.append((i, j))
            
            if (monarch.HP > wizard_tower.damage):
                monarch.HP -= wizard_tower.damage
            else:
                monarch.HP = 0

            for barbarian, a_barbarian_position in barbarian_position.items():
                if ((a_barbarian_position in area_possible_attack) and (wizard_tower.HP != 0)):
                    if (barbarian.HP > wizard_tower.damage):
                            barbarian.HP -= wizard_tower.damage
                    else:
                        barbarian.HP = 0
            for archer, an_archer_position in archer_position.items():
                if ((an_archer_position in area_possible_attack) and (wizard_tower.HP != 0)):
                    if (archer.HP > wizard_tower.damage):
                        archer.HP -= wizard_tower.damage
                    else:
                        archer.HP = 0
            # for balloon, a_balloon_position in balloon_position.items():
            #     if ((a_balloon_position in area_possible_attack) and (wizard_tower.HP != 0)):
            #         if (balloon.HP > wizard_tower.damage):
            #             balloon.HP -= wizard_tower.damage
            #         else:
            #             balloon.HP = 0
            attack_done = True
        elif ((queen_position in wizard_tower_possible_attack) and (wizard_tower.HP != 0)):
                
            area_possible_attack = []

            for i in range(queen_position[0] - wizard_tower.area, queen_position[0] + wizard_tower.area + 1): 
                for j in range(queen_position[1] - wizard_tower.area, queen_position[1] + wizard_tower.area + 1):
                    area_possible_attack.append((i, j))
            
            if (monarch.HP > wizard_tower.damage):
                monarch.HP -= wizard_tower.damage
            else:
                monarch.HP = 0
                
            for barbarian, a_barbarian_position in barbarian_position.items():
                if ((a_barbarian_position in area_possible_attack) and (wizard_tower.HP != 0)):
                    if (barbarian.HP > wizard_tower.damage):
                            barbarian.HP -= wizard_tower.damage
                    else:
                        barbarian.HP = 0
            for archer, an_archer_position in archer_position.items():
                if ((an_archer_position in area_possible_attack) and (wizard_tower.HP != 0)):
                    if (archer.HP > wizard_tower.damage):
                        archer.HP -= wizard_tower.damage
                    else:
                        archer.HP = 0
            # for balloon, a_balloon_position in balloon_position.items():
            #     if ((a_balloon_position in area_possible_attack) and (wizard_tower.HP != 0)):
            #         if (balloon.HP > wizard_tower.damage):
            #             balloon.HP -= wizard_tower.damage
            #         else:
            #             balloon.HP = 0
            attack_done = True
        for barbarian, a_barbarian_position in barbarian_position.items():
            if ((a_barbarian_position in wizard_tower_possible_attack) and (wizard_tower.HP != 0)):
                area_possible_attack = []

                for i in range(a_barbarian_position[0] - wizard_tower.area, a_barbarian_position[0] + wizard_tower.area + 1): 
                    for j in range(a_barbarian_position[1] - wizard_tower.area, a_barbarian_position[1] + wizard_tower.area + 1):
                        area_possible_attack.append((i, j))
                if (barbarian.HP > wizard_tower.damage):
                    barbarian.HP -= wizard_tower.damage
                else:
                    barbarian.HP = 0
                    
                if ((king_position in area_possible_attack) and (wizard_tower.HP != 0)):
                    if (monarch.HP > wizard_tower.damage):
                            monarch.HP -= wizard_tower.damage
                    else:
                        monarch.HP = 0
                if ((queen_position in area_possible_attack) and (wizard_tower.HP != 0)):
                    if (monarch.HP > wizard_tower.damage):
                            monarch.HP -= wizard_tower.damage
                    else:
                        monarch.HP = 0
                for barbarian, b_barbarian_position in barbarian_position.items():
                    if ((b_barbarian_position in area_possible_attack) and (b_barbarian_position != a_barbarian_position) and (wizard_tower.HP != 0)):
                        if (barbarian.HP > wizard_tower.damage):
                                barbarian.HP -= wizard_tower.damage
                        else:
                            barbarian.HP = 0
                for archer, an_archer_position in archer_position.items():
                    if ((an_archer_position in area_possible_attack) and (wizard_tower.HP != 0)):
                        if (archer.HP > wizard_tower.damage):
                            archer.HP -= wizard_tower.damage
                        else:
                            archer.HP = 0
                # for balloon, a_balloon_position in balloon_position.items():
                #     if ((a_balloon_position in area_possible_attack) and (wizard_tower.HP != 0)):
                #         if (balloon.HP > wizard_tower.damage):
                #             balloon.HP -= wizard_tower.damage
                #         else:
                #             balloon.HP = 0
                attack_done = True
                break
        for archer, an_archer_position in archer_position.items():
            if ((an_archer_position in wizard_tower_possible_attack) and (wizard_tower.HP != 0)):
                area_possible_attack = []

                for i in range(an_archer_position[0] - wizard_tower.area, an_archer_position[0] + wizard_tower.area + 1): 
                    for j in range(an_archer_position[1] - wizard_tower.area, an_archer_position[1] + wizard_tower.area + 1):
                        area_possible_attack.append((i, j))
                if (archer.HP > wizard_tower.damage):
                    archer.HP -= wizard_tower.damage
                else:
                    archer.HP = 0
                    
                if ((king_position in area_possible_attack) and (wizard_tower.HP != 0)):
                    if (monarch.HP > wizard_tower.damage):
                        monarch.HP -= wizard_tower.damage
                    else:
                        monarch.HP = 0
                if ((queen_position in area_possible_attack) and (wizard_tower.HP != 0)):
                    if (monarch.HP > wizard_tower.damage):
                            monarch.HP -= wizard_tower.damage
                    else:
                        monarch.HP = 0
                for barbarian, a_barbarian_position in barbarian_position.items():
                    if ((a_barbarian_position in area_possible_attack) and (wizard_tower.HP != 0)):
                        if (barbarian.HP > wizard_tower.damage):
                                barbarian.HP -= wizard_tower.damage
                        else:
                            barbarian.HP = 0
                for archer, bn_archer_position in archer_position.items():
                    if ((bn_archer_position in area_possible_attack) and (bn_archer_position != an_archer_position) and (wizard_tower.HP != 0)):
                        if (archer.HP > wizard_tower.damage):
                            archer.HP -= wizard_tower.damage
                        else:
                            archer.HP = 0
                # for balloon, a_balloon_position in balloon_position.items():
                #     if ((a_balloon_position in area_possible_attack) and (wizard_tower.HP != 0)):
                #         if (balloon.HP > wizard_tower.damage):
                #             balloon.HP -= wizard_tower.damage
                #         else:
                #             balloon.HP = 0
                attack_done = True
                break
        # for balloon, a_balloon_position in balloon_position.items():
        #     if ((a_balloon_position in wizard_tower_possible_attack) and (wizard_tower.HP != 0)):
        #         area_possible_attack = []

        #         for i in range(a_balloon_position[0] - wizard_tower.area, a_balloon_position[0] + wizard_tower.area + 1): 
        #             for j in range(a_balloon_position[1] - wizard_tower.area, a_balloon_position[1] + wizard_tower.area + 1):
        #                 a_possible_attack.append((i, j))
        #         if (balloon.HP > wizard_tower.damage):
        #             balloon.HP -= wizard_tower.damage
        #         else:
        #             balloon.HP = 0
                    
        #         if ((king_position in area_possible_attack) and (wizard_tower.HP != 0)):
        #             if (monarch.HP > wizard_tower.damage):
        #                 monarch.HP -= wizard_tower.damage
        #             else:
        #                 monarch.HP = 0
        #         if ((queen_position in area_possible_attack) and (wizard_tower.HP != 0)):
        #             if (monarch.HP > wizard_tower.damage):
        #                     monarch.HP -= wizard_tower.damage
        #             else:
        #                 monarch.HP = 0
        #         for barbarian, a_barbarian_position in barbarian_position.items():
        #             if ((a_barbarian_position in area_possible_attack) and (wizard_tower.HP != 0)):
        #                 if (barbarian.HP > wizard_tower.damage):
        #                         barbarian.HP -= wizard_tower.damage
        #                 else:
        #                     barbarian.HP = 0
        #         for archer, an_archer_position in archer_position.items():
        #             if ((an_archer_position in area_possible_attack) and (wizard_tower.HP != 0)):
        #                 if (archer.HP > wizard_tower.damage):
        #                     archer.HP -= wizard_tower.damage
        #                 else:
        #                     archer.HP = 0
        #         for balloon, b_balloon_position in balloon_position.items():
        #             if ((b_balloon_position in area_possible_attack) and (b_balloon_position != a_balloon_position) and (wizard_tower.HP != 0)):
        #                 if (balloon.HP > wizard_tower.damage):
        #                     balloon.HP -= wizard_tower.damage
        #                 else:
        #                     balloon.HP = 0
        #         attack_done = True
        #         break
        
        if (attack_done):
            break

    wizard_tower_done = True

def check_situation(town_hall, list_of_huts, list_of_cannons, list_of_wizard_towers, monarch, list_of_barbarians, list_of_archers):

    global level, character
    
    thS, hS, cS, wtS, mS, bS, aS, baS = True, True, True, True, True, True, True, True
    
    if (town_hall.HP == 0):
        thS = False
        
    if (monarch.HP == 0):
        mS = False
        
    count_hut = 0
    for hut in list_of_huts:
        if (hut.HP == 0):
            count_hut += 1
    if (count_hut == len(list_of_huts)):
        hS = False
        
    count_cannon = 0
    for cannon in list_of_cannons:
        if (cannon.HP == 0):
            count_cannon += 1
    if (count_cannon == len(list_of_cannons)):
        cS = False

    count_wizard_tower = 0
    for wizard_tower in list_of_wizard_towers:
        if (wizard_tower.HP == 0):
            count_wizard_tower += 1
    if (count_wizard_tower == len(list_of_wizard_towers)):
        wtS = False

    count_barbarian = 0
    for barbarian in list_of_barbarians:
        if (barbarian.HP == 0):
            count_barbarian += 1
    if (count_barbarian == len(list_of_barbarians)):
        bS = False
        
    count_archer = 0
    for archer in list_of_archers:
        if (archer.HP == 0):
            count_archer += 1
    if (count_archer == len(list_of_archers)):
        aS = False
        
    # count_balloon = 0
    # for balloon in list_of_balloons:
    #     if (balloon.HP == 0):
    #         count_balloon += 1
    # if (count_balloon == len(list_of_balloons)):
    #     baS = False
        
    if ((not mS) and (not bS) and (not baS) and (not aS)):
        print("The village has defended itself and won.")
        return 1
    elif ((not thS) and (not cS) and (not hS) and (not wtS)):
        print("The troops have conquered the village.")
        return 2
    else:
        return 0

def spawn_king(point, list_of_spawning_points):
    
    global king_position, king_spawned

    if (point == "i"):
        which_point = 0
    elif (point == "o"):
        which_point = 1
    elif (point == "p"):
        which_point = 2
    king_position = list(king_position)
    point_of_development = list(list_of_spawning_points[which_point].xy)
    point = [-1, -1]
    if (point_of_development[0] > point_of_development[1]):
        point[0] = point_of_development[0]
        point[1] = point_of_development[1] + 1
    else:
        point[0] = point_of_development[0] + 1
        point[1] = point_of_development[1]
        
    king_position = tuple(point)
    
    king_spawned = True
    
def spawn_queen(point, list_of_spawning_points):
    
    global queen_position, queen_spawned

    if (point == "i"):
        which_point = 0
    elif (point == "o"):
        which_point = 1
    elif (point == "p"):
        which_point = 2
    queen_position = list(queen_position)
    # print(queen_position)
    point_of_development = list(list_of_spawning_points[which_point].xy)
    point = [-1, -1]
    # print(point_of_development)
    if (point_of_development[0] > point_of_development[1]):
        point[0] = point_of_development[0]
        point[1] = point_of_development[1] + 1
    else:
        point[0] = point_of_development[0] + 1
        point[1] = point_of_development[1]
        
    queen_position = tuple(point)
    
    queen_spawned = True

def king_move(king, direction):
    
    global king_position, occupied
    
    try:
        if (direction == "w"):
            king_position = list(king_position)
            val = 0
            for i in range(1, king.movement_speed + 1):
                if (((king_position[0] - i, king_position[1]) in occupied) and ((king_position[0] - i, king_position[1]) not in village_occupied["Empty Space"])):
                    val = king.movement_speed - i + 1
                    break
            king_position[0] = king_position[0] - (king.movement_speed - val)
            king_position = tuple(king_position)
        elif (direction == "s"):
            king_position = list(king_position)
            val = 0
            for i in range(1, king.movement_speed + 1):
                if (((king_position[0] + i, king_position[1]) in occupied) and ((king_position[0] + i, king_position[1]) not in village_occupied["Empty Space"])):
                    val = king.movement_speed - i + 1
                    break
            king_position[0] = king_position[0] + (king.movement_speed - val)
            king_position = tuple(king_position)
        elif (direction == "a"):
            king_position = list(king_position)
            val = 0
            for i in range(1, king.movement_speed + 1):
                if (((king_position[0], king_position[1] - i) in occupied) and ((king_position[0], king_position[1] - i) not in village_occupied["Empty Space"])):
                    val = king.movement_speed - i + 1
                    break
            king_position[1] = king_position[1] - (king.movement_speed - val)
            king_position = tuple(king_position)
        elif (direction == "d"):
            king_position = list(king_position)
            val = 0
            for i in range(1, king.movement_speed + 1):
                if (((king_position[0], king_position[1] + i) in occupied) and ((king_position[0], king_position[1] + i) not in village_occupied["Empty Space"])):
                    val = king.movement_speed - i + 1
                    break
            king_position[1] = king_position[1] + (king.movement_speed - val)
            king_position = tuple(king_position)
            
    except IndexError:
        print("The king hasn't spawned yet. Bring him on with the use of \'i\' or \'o\' or \'p\'")

def queen_move(queen, direction):
    
    global queen_position, occupied
    
    try:
        if (direction == "w"):
            queen_position = list(queen_position)
            val = 0
            for i in range(1, queen.movement_speed + 1):
                if (((queen_position[0] - i, queen_position[1]) in occupied) and ((queen_position[0] - i, queen_position[1]) not in village_occupied["Empty Space"])):
                    val = queen.movement_speed - i + 1
                    break
            queen_position[0] = queen_position[0] - (queen.movement_speed - val)
            queen_position = tuple(queen_position)
        elif (direction == "s"):
            queen_position = list(queen_position)
            val = 0
            for i in range(1, queen.movement_speed + 1):
                if (((queen_position[0] + i, queen_position[1]) in occupied) and ((queen_position[0] + i, queen_position[1]) not in village_occupied["Empty Space"])):
                    val = queen.movement_speed - i + 1
                    break
            queen_position[0] = queen_position[0] + (queen.movement_speed - val)
            queen_position = tuple(queen_position)
        elif (direction == "a"):
            queen_position = list(queen_position)
            val = 0
            for i in range(1, queen.movement_speed + 1):
                if (((queen_position[0], queen_position[1] - i) in occupied) and ((queen_position[0], queen_position[1] - i) not in village_occupied["Empty Space"])):
                    val = queen.movement_speed - i + 1
                    break
            queen_position[1] = queen_position[1] - (queen.movement_speed - val)
            queen_position = tuple(queen_position)
        elif (direction == "d"):
            queen_position = list(queen_position)
            val = 0
            for i in range(1, queen.movement_speed + 1):
                if (((queen_position[0], queen_position[1] + i) in occupied) and ((queen_position[0], queen_position[1] + i) not in village_occupied["Empty Space"])):
                    val = queen.movement_speed - i + 1
                    break
            queen_position[1] = queen_position[1] + (queen.movement_speed - val)
            queen_position = tuple(queen_position)
            
    except IndexError:
        print("The queen hasn't spawned yet. Bring him on with the use of \'i\' or \'o\' or \'p\'")

def barbarian_spawn(position, list_of_barbarians, list_of_spawning_points):
    
    global barbarian_position

    number_on_field = len(barbarian_position)
    if (position == "i"):
        if ((archer_position != {}) or (barbarian_position != {})):
            there = False
            for res_position in archer_position.values():
                if (res_position == list_of_spawning_points[0].xy):
                    there = True
                    break
            for res_position in barbarian_position.values():
                if (not there):
                    if (res_position == list_of_spawning_points[0].xy):
                        there = True
                        break
                else:
                    break
            if (there):
                print("One troop is already here.")
            else:
                barbarian_position[list_of_barbarians[number_on_field]] = list_of_spawning_points[0].xy
        else:
            barbarian_position[list_of_barbarians[number_on_field]] = list_of_spawning_points[0].xy
    elif (position == "o"):
        if ((archer_position != {}) or (barbarian_position != {})):
            there = False
            for res_position in archer_position.values():
                if (res_position == list_of_spawning_points[0].xy):
                    there = True
                    break
            for res_position in barbarian_position.values():
                if (not there):
                    if (res_position == list_of_spawning_points[0].xy):
                        there = True
                        break
                else:
                    break
            if (there):
                print("One troop is already here.")
            else:
                barbarian_position[list_of_barbarians[number_on_field]] = list_of_spawning_points[1].xy
        else:
            barbarian_position[list_of_barbarians[number_on_field]] = list_of_spawning_points[1].xy
    elif (position == "p"):
        if ((archer_position != {}) or (barbarian_position != {})):
            there = False
            for res_position in archer_position.values():
                if (res_position == list_of_spawning_points[0].xy):
                    there = True
                    break
            for res_position in barbarian_position.values():
                if (not there):
                    if (res_position == list_of_spawning_points[0].xy):
                        there = True
                        break
                else:
                    break
            if (there):
                print("One troop is already here.")
            else:
                barbarian_position[list_of_barbarians[number_on_field]] = list_of_spawning_points[2].xy
        else:
            barbarian_position[list_of_barbarians[number_on_field]] = list_of_spawning_points[2].xy
            
def archer_spawn(position, list_of_archers, list_of_spawning_points):
    
    global archer_position, barbarian_position

    number_on_field = len(archer_position)
    if (position == "i"):
        if ((archer_position != {}) or (barbarian_position != {})):
            there = False
            for res_position in archer_position.values():
                if (res_position == list_of_spawning_points[0].xy):
                    there = True
                    break
            for res_position in barbarian_position.values():
                if (not there):
                    if (res_position == list_of_spawning_points[0].xy):
                        there = True
                        break
                else:
                    break
            if (there):
                print("One troop is already here.")
            else:
                archer_position[list_of_archers[number_on_field]] = list_of_spawning_points[0].xy
        else:
            archer_position[list_of_archers[number_on_field]] = list_of_spawning_points[0].xy
    elif (position == "o"):
        if ((archer_position != {}) or (barbarian_position != {})):
            there = False
            for res_position in archer_position.values():
                if (res_position == list_of_spawning_points[0].xy):
                    there = True
                    break
            for res_position in barbarian_position.values():
                if (not there):
                    if (res_position == list_of_spawning_points[0].xy):
                        there = True
                        break
                else:
                    break
            if (there):
                print("One troop is already here.")
            else:
                archer_position[list_of_archers[number_on_field]] = list_of_spawning_points[1].xy
        else:
            archer_position[list_of_archers[number_on_field]] = list_of_spawning_points[1].xy
    elif (position == "p"):
        if ((archer_position != {}) or (barbarian_position != {})):
            there = False
            for res_position in archer_position.values():
                if (res_position == list_of_spawning_points[0].xy):
                    there = True
                    break
            for res_position in barbarian_position.values():
                if (not there):
                    if (res_position == list_of_spawning_points[0].xy):
                        there = True
                        break
                else:
                    break
            if (there):
                print("One troop is already here.")
            else:
                archer_position[list_of_archers[number_on_field]] = list_of_spawning_points[2].xy
        else:
            archer_position[list_of_archers[number_on_field]] = list_of_spawning_points[2].xy

def barbarian_movement(village):
    
    global occupied, village_occupied, barbarian_position, archer_position
    
    
    no_wall_list = []
    v_length, v_breadth = village.size_length, village.size_breadth
    
    for i in range(12, v_length):
        if ((i, 12) not in occupied):
            no_wall_list.append((i, 12))
            
    for j in range(12, v_breadth):
        if ((12, j) not in occupied):
            no_wall_list.append((12, j))
    
    for barbarian, position in barbarian_position.items():
        
        if (barbarian.HP > 0):
            
            # We are doing so that the barbarians are attracted to the walls when they are outside the village parameters.
            if ((position[0] < 12) or (position[1] < 12)):
                
                # print("Outside the village at", position)
                
                if (no_wall_list != []):

                    # print("Inside the village boundaries.")
                    
                    add = 10000
                    cc = []

                    for closest_coordinate in no_wall_list:
                        if (((abs(position[0] - closest_coordinate[0])) + (abs(position[1] - closest_coordinate[1]))) < add):
                            add = abs(position[0] - closest_coordinate[0]) + abs(position[1] - closest_coordinate[1])
                            cc = list(closest_coordinate)
                            
                    y_difference = position[0] - cc[0]
                    x_difference = position[1] - cc[1]
                    
                    # print("Moving to the closest coordinate of a building -", str(cc), "- from the current position:", str(position) + ".")
                    
                    if (((abs(y_difference) < abs(x_difference)) and (y_difference != 0)) or (x_difference == 0)):
                        if (y_difference > 0):
                            barbarian_position[barbarian] = list(barbarian_position[barbarian])
                            pos = barbarian_position[barbarian]
                            val = 0
                            for i in range(1, barbarian.movement_speed + 1):
                                if (((pos[0] - i, pos[1]) in occupied) and ((pos[0] - i, pos[1]) not in village_occupied["Empty Space"])):
                                    val = barbarian.movement_speed - i + 1
                                    break
                            # print("Moving up.")
                            barbarian_position[barbarian][0] = barbarian_position[barbarian][0] - (barbarian.movement_speed - val)
                            barbarian_position[barbarian] = tuple(barbarian_position[barbarian])
                        elif (y_difference < 0):
                            barbarian_position[barbarian] = list(barbarian_position[barbarian])
                            pos = barbarian_position[barbarian]
                            val = 0
                            for i in range(1, barbarian.movement_speed + 1):
                                if (((pos[0] + i, pos[1]) in occupied) and ((pos[0] + i, pos[1]) not in village_occupied["Empty Space"])):
                                    val = barbarian.movement_speed - i + 1
                                    break
                            # print("Moving down.")
                            barbarian_position[barbarian][0] = barbarian_position[barbarian][0] + (barbarian.movement_speed - val)
                            barbarian_position[barbarian] = tuple(barbarian_position[barbarian])
                    elif (((abs(y_difference) > abs(x_difference)) and (x_difference != 0)) or (y_difference == 0)):
                        if (x_difference > 0):
                            barbarian_position[barbarian] = list(barbarian_position[barbarian])
                            pos = barbarian_position[barbarian]
                            val = 0
                            for i in range(1, barbarian.movement_speed + 1):
                                if (((pos[0], pos[1] - i) in occupied) and ((pos[0], pos[1] - i) not in village_occupied["Empty Space"])):
                                    val = barbarian.movement_speed - i + 1
                                    break
                            # print("Moving left.")
                            barbarian_position[barbarian][1] = barbarian_position[barbarian][1] - (barbarian.movement_speed - val)
                            barbarian_position[barbarian] = tuple(barbarian_position[barbarian])
                        elif (x_difference < 0):
                            barbarian_position[barbarian] = list(barbarian_position[barbarian])
                            pos = barbarian_position[barbarian]
                            val = 0
                            for i in range(1, barbarian.movement_speed + 1):
                                if (((pos[0], pos[1] + i) in occupied) and ((pos[0], pos[1] + i) not in village_occupied["Empty Space"])):
                                    val = barbarian.movement_speed - i + 1
                                    break
                            # print("Moving right.")
                            barbarian_position[barbarian][1] = barbarian_position[barbarian][1] + (barbarian.movement_speed - val)
                            barbarian_position[barbarian] = tuple(barbarian_position[barbarian])
                    elif (abs(y_difference) == abs(x_difference)):
                        if (y_difference > 0):
                            barbarian_position[barbarian] = list(barbarian_position[barbarian])
                            pos = barbarian_position[barbarian]
                            val = 0
                            for i in range(1, barbarian.movement_speed + 1):
                                if (((pos[0] - i, pos[1]) in occupied) and ((pos[0] - i, pos[1]) not in village_occupied["Empty Space"])):
                                    val = barbarian.movement_speed - i + 1
                                    break
                            # print("Moving up.")
                            barbarian_position[barbarian][0] = barbarian_position[barbarian][0] - (barbarian.movement_speed - val)
                            barbarian_position[barbarian] = tuple(barbarian_position[barbarian])
                        elif (y_difference < 0):
                            barbarian_position[barbarian] = list(barbarian_position[barbarian])
                            pos = barbarian_position[barbarian]
                            val = 0
                            for i in range(1, barbarian.movement_speed + 1):
                                if (((pos[0] + i, pos[1]) in occupied) and ((pos[0] + i, pos[1]) not in village_occupied["Empty Space"])):
                                    val = barbarian.movement_speed - i + 1
                                    break
                            # print("Moving down.")
                            barbarian_position[barbarian][0] = barbarian_position[barbarian][0] + (barbarian.movement_speed - val)
                            barbarian_position[barbarian] = tuple(barbarian_position[barbarian]) 
                
                else:
                    if (position[0] < position[1]):
                        barbarian_position[barbarian] = list(barbarian_position[barbarian])
                        pos = barbarian_position[barbarian]
                        val = 0
                        for i in range(1, barbarian.movement_speed + 1):
                            if (((pos[0] + i, pos[1]) in occupied) and ((pos[0] + i, pos[1]) not in village_occupied["Empty Space"])):
                                val = barbarian.movement_speed - i + 1
                                break
                        barbarian_position[barbarian][0] = barbarian_position[barbarian][0] + (barbarian.movement_speed - val)
                        barbarian_position[barbarian] = tuple(barbarian_position[barbarian])
                    else:
                        barbarian_position[barbarian] = list(barbarian_position[barbarian])
                        pos = barbarian_position[barbarian]
                        val = 0
                        for i in range(1, barbarian.movement_speed + 1):
                            if (((pos[0], pos[1] + i) in occupied) and ((pos[0], pos[1] + i) not in village_occupied["Empty Space"])):
                                val = barbarian.movement_speed - i + 1
                                break
                        barbarian_position[barbarian][1] = barbarian_position[barbarian][1] + (barbarian.movement_speed - val)
                        barbarian_position[barbarian] = tuple(barbarian_position[barbarian])
            # For the barbarian to move into the village from the wall position
            elif ((position[0] == 12) or (position[1] == 12)):
                
                # print("Moving into the village from the wall:", str(position))
                
                if (position[0] == 12):
                    barbarian_position[barbarian] = list(barbarian_position[barbarian])
                    pos = barbarian_position[barbarian]
                    val = 0
                    for i in range(1, barbarian.movement_speed + 1):
                        if (((pos[0] + i, pos[1]) in occupied) and ((pos[0] + i, pos[1]) not in village_occupied["Empty Space"])):
                            val = barbarian.movement_speed - i + 1
                            break
                    barbarian_position[barbarian][0] = barbarian_position[barbarian][0] + (barbarian.movement_speed - val)
                    barbarian_position[barbarian] = tuple(barbarian_position[barbarian])
                else:
                    barbarian_position[barbarian] = list(barbarian_position[barbarian])
                    pos = barbarian_position[barbarian]
                    val = 0
                    for i in range(1, barbarian.movement_speed + 1):
                        if (((pos[0], pos[1] + i) in occupied) and ((pos[0], pos[1] + i) not in village_occupied["Empty Space"])):
                            val = barbarian.movement_speed - i + 1
                            break
                    barbarian_position[barbarian][1] = barbarian_position[barbarian][1] + (barbarian.movement_speed - val)
                    barbarian_position[barbarian] = tuple(barbarian_position[barbarian])
            #Up until here, the barbarian is capable of moving towards the walls and past it by one barbarian.movement_speed.
            elif ((position[0] > 12) and (position[1] > 12)):
                
                add = 10000
                cc = []
    
                for closest_coordinate in village_occupied["Huts"]:
                    if (((abs(position[0] - closest_coordinate[0])) + (abs(position[1] - closest_coordinate[1]))) < add):
                        add = abs(position[0] - closest_coordinate[0]) + abs(position[1] - closest_coordinate[1])
                        cc = list(closest_coordinate)
                
                for closest_coordinate in village_occupied["Cannons"]:
                    if (((abs(position[0] - closest_coordinate[0])) + (abs(position[1] - closest_coordinate[1]))) < add):
                        add = abs(position[0] - closest_coordinate[0]) + abs(position[1] - closest_coordinate[1])
                        cc = list(closest_coordinate)
                        
                for closest_coordinate in village_occupied["Wizard Towers"]:
                    if (((abs(position[0] - closest_coordinate[0])) + (abs(position[1] - closest_coordinate[1]))) < add):
                        add = abs(position[0] - closest_coordinate[0]) + abs(position[1] - closest_coordinate[1])
                        cc = list(closest_coordinate)
                
                for closest_coordinate in village_occupied["Town Hall"]:
                    if (((abs(position[0] - closest_coordinate[0])) + (abs(position[1] - closest_coordinate[1]))) < add):
                        add = abs(position[0] - closest_coordinate[0]) + abs(position[1] - closest_coordinate[1])
                        cc = list(closest_coordinate)
                        
                y_difference = position[0] - cc[0]
                x_difference = position[1] - cc[1]
                
                if (((abs(y_difference) < abs(x_difference)) and (y_difference != 0)) or (x_difference == 0)):
                    if (y_difference > 0):
                        barbarian_position[barbarian] = list(barbarian_position[barbarian])
                        pos = barbarian_position[barbarian]
                        val = 0
                        for i in range(1, barbarian.movement_speed + 1):
                            if (((pos[0] - i, pos[1]) in occupied) and ((pos[0] - i, pos[1]) not in village_occupied["Empty Space"])):
                                val = barbarian.movement_speed - i + 1
                                break
                        # print("Moving up.")
                        barbarian_position[barbarian][0] = barbarian_position[barbarian][0] - (barbarian.movement_speed - val)
                        barbarian_position[barbarian] = tuple(barbarian_position[barbarian])
                    elif (y_difference < 0):
                        barbarian_position[barbarian] = list(barbarian_position[barbarian])
                        pos = barbarian_position[barbarian]
                        val = 0
                        for i in range(1, barbarian.movement_speed + 1):
                            if (((pos[0] + i, pos[1]) in occupied) and ((pos[0] + i, pos[1]) not in village_occupied["Empty Space"])):
                                val = barbarian.movement_speed - i + 1
                                break
                        # print("Moving down.")
                        barbarian_position[barbarian][0] = barbarian_position[barbarian][0] + (barbarian.movement_speed - val)
                        barbarian_position[barbarian] = tuple(barbarian_position[barbarian])
                elif (((abs(y_difference) > abs(x_difference)) and (x_difference != 0)) or (y_difference == 0)):
                    if (x_difference > 0):
                        barbarian_position[barbarian] = list(barbarian_position[barbarian])
                        pos = barbarian_position[barbarian]
                        val = 0
                        for i in range(1, barbarian.movement_speed + 1):
                            if (((pos[0], pos[1] - i) in occupied) and ((pos[0], pos[1] - i) not in village_occupied["Empty Space"])):
                                val = barbarian.movement_speed - i + 1
                                break
                        # print("Moving left.")
                        barbarian_position[barbarian][1] = barbarian_position[barbarian][1] - (barbarian.movement_speed - val)
                        barbarian_position[barbarian] = tuple(barbarian_position[barbarian])
                    elif (x_difference < 0):
                        barbarian_position[barbarian] = list(barbarian_position[barbarian])
                        pos = barbarian_position[barbarian]
                        val = 0
                        for i in range(1, barbarian.movement_speed + 1):
                            if (((pos[0], pos[1] + i) in occupied) and ((pos[0], pos[1] + i) not in village_occupied["Empty Space"])):
                                val = barbarian.movement_speed - i + 1
                                break
                        # print("Moving right.")
                        barbarian_position[barbarian][1] = barbarian_position[barbarian][1] + (barbarian.movement_speed - val)
                        barbarian_position[barbarian] = tuple(barbarian_position[barbarian])
                elif (abs(y_difference) == abs(x_difference)):
                    if (y_difference > 0):
                        barbarian_position[barbarian] = list(barbarian_position[barbarian])
                        pos = barbarian_position[barbarian]
                        val = 0
                        for i in range(1, barbarian.movement_speed + 1):
                            if (((pos[0] - i, pos[1]) in occupied) and ((pos[0] - i, pos[1]) not in village_occupied["Empty Space"])):
                                val = barbarian.movement_speed - i + 1
                                break
                        # print("Moving up.")
                        barbarian_position[barbarian][0] = barbarian_position[barbarian][0] - (barbarian.movement_speed - val)
                        barbarian_position[barbarian] = tuple(barbarian_position[barbarian])
                    elif (y_difference < 0):
                        barbarian_position[barbarian] = list(barbarian_position[barbarian])
                        pos = barbarian_position[barbarian]
                        val = 0
                        for i in range(1, barbarian.movement_speed + 1):
                            if (((pos[0] + i, pos[1]) in occupied) and ((pos[0] + i, pos[1]) not in village_occupied["Empty Space"])):
                                val = barbarian.movement_speed - i + 1
                                break
                        # print("Moving down.")
                        barbarian_position[barbarian][0] = barbarian_position[barbarian][0] + (barbarian.movement_speed - val)
                        barbarian_position[barbarian] = tuple(barbarian_position[barbarian])

def archer_movement(village):
    
    global occupied, village_occupied, archer_position, barbarian_position

    printing = True
    
    no_wall_list = []
    v_length, v_breadth = village.size_length, village.size_breadth
    
    for i in range(12, v_length):
        if ((i, 12) not in occupied):
            no_wall_list.append((i, 12))
            
    for j in range(12, v_breadth):
        if ((12, j) not in occupied):
            no_wall_list.append((12, j))
    
    for archer, position in archer_position.items():
        
        if (archer.HP > 0):
            
            # We are doing so that the archers are attracted to the walls when they are outside the village parameters.
            if ((position[0] < 12) or (position[1] < 12)):

                if (no_wall_list != []):

                    add = 10000
                    cc = []
                    
                    for closest_coordinate in no_wall_list:
                        if (((abs(position[0] - closest_coordinate[0])) + (abs(position[1] - closest_coordinate[1]))) < add):
                            add = abs(position[0] - closest_coordinate[0]) + abs(position[1] - closest_coordinate[1])
                            cc = list(closest_coordinate)
                            
                    y_difference = position[0] - cc[0]
                    x_difference = position[1] - cc[1]
                    
                    if (((abs(y_difference) < abs(x_difference)) and (y_difference != 0)) or (x_difference == 0)):
                        if (y_difference > 0):
                            archer_position[archer] = list(archer_position[archer])
                            pos = archer_position[archer]
                            val = 0
                            for i in range(1, archer.movement_speed + 1):
                                if (((pos[0] - i, pos[1]) in occupied) and ((pos[0] - i, pos[1]) not in village_occupied["Empty Space"])):
                                    val = archer.movement_speed - i + 1
                                    break
                            archer_position[archer][0] = archer_position[archer][0] - (archer.movement_speed - val)
                            archer_position[archer] = tuple(archer_position[archer])
                        elif (y_difference < 0):
                            archer_position[archer] = list(archer_position[archer])
                            pos = archer_position[archer]
                            val = 0
                            for i in range(1, archer.movement_speed + 1):
                                if (((pos[0] + i, pos[1]) in occupied) and ((pos[0] + i, pos[1]) not in village_occupied["Empty Space"])):
                                    val = archer.movement_speed - i + 1
                                    break
                            archer_position[archer][0] = archer_position[archer][0] + (archer.movement_speed - val)
                            archer_position[archer] = tuple(archer_position[archer])
                    elif (((abs(y_difference) > abs(x_difference)) and (x_difference != 0)) or (y_difference == 0)):
                        if (x_difference > 0):
                            archer_position[archer] = list(archer_position[archer])
                            pos = archer_position[archer]
                            val = 0
                            for i in range(1, archer.movement_speed + 1):
                                if (((pos[0], pos[1] - i) in occupied) and ((pos[0], pos[1] - i) not in village_occupied["Empty Space"])):
                                    val = archer.movement_speed - i + 1
                                    break
                            archer_position[archer][1] = archer_position[archer][1] - (archer.movement_speed - val)
                            archer_position[archer] = tuple(archer_position[archer])
                        elif (x_difference < 0):
                            archer_position[archer] = list(archer_position[archer])
                            pos = archer_position[archer]
                            val = 0
                            for i in range(1, archer.movement_speed + 1):
                                if (((pos[0], pos[1] + i) in occupied) and ((pos[0], pos[1] + i) not in village_occupied["Empty Space"])):
                                    val = archer.movement_speed - i + 1
                                    break
                            archer_position[archer][1] = archer_position[archer][1] + (archer.movement_speed - val)
                            archer_position[archer] = tuple(archer_position[archer])
                    elif (abs(y_difference) == abs(x_difference)):
                        if (y_difference > 0):
                            archer_position[archer] = list(archer_position[archer])
                            pos = archer_position[archer]
                            val = 0
                            for i in range(1, archer.movement_speed + 1):
                                if (((pos[0] - i, pos[1]) in occupied) and ((pos[0] - i, pos[1]) not in village_occupied["Empty Space"])):
                                    val = archer.movement_speed - i + 1
                                    break
                            archer_position[archer][0] = archer_position[archer][0] - (archer.movement_speed - val)
                            archer_position[archer] = tuple(archer_position[archer])
                        elif (y_difference < 0):
                            archer_position[archer] = list(archer_position[archer])
                            pos = archer_position[archer]
                            val = 0
                            for i in range(1, archer.movement_speed + 1):
                                if (((pos[0] + i, pos[1]) in occupied) and ((pos[0] + i, pos[1]) not in village_occupied["Empty Space"])):
                                    val = archer.movement_speed - i + 1
                                    break
                            archer_position[archer][0] = archer_position[archer][0] + (archer.movement_speed - val)
                            archer_position[archer] = tuple(archer_position[archer])                    
                else:
                    if (position[0] < position[1]):
                        archer_position[archer] = list(archer_position[archer])
                        pos = archer_position[archer]
                        val = 0
                        for i in range(1, archer.movement_speed + 1):
                            if (((pos[0] + i, pos[1]) in occupied) and ((pos[0] + i, pos[1]) not in village_occupied["Empty Space"])):
                                val = archer.movement_speed - i + 1
                                break
                        archer_position[archer][0] = archer_position[archer][0] + (archer.movement_speed - val)
                        archer_position[archer] = tuple(archer_position[archer])
                    else:
                        archer_position[archer] = list(archer_position[archer])
                        pos = archer_position[archer]
                        val = 0
                        for i in range(1, archer.movement_speed + 1):
                            if (((pos[0], pos[1] + i) in occupied) and ((pos[0], pos[1] + i) not in village_occupied["Empty Space"])):
                                val = archer.movement_speed - i + 1
                                break
                        archer_position[archer][1] = archer_position[archer][1] + (archer.movement_speed - val)
                        archer_position[archer] = tuple(archer_position[archer])
            # Move into the village
            elif ((position[0] == 12) or (position[1] == 12)):
                if (position[0] == 12):
                    archer_position[archer] = list(archer_position[archer])
                    pos = archer_position[archer]
                    val = 0
                    for i in range(1, archer.movement_speed + 1):
                        if (((pos[0] + i, pos[1]) in occupied) and ((pos[0] + i, pos[1]) not in village_occupied["Empty Space"])):
                            val = archer.movement_speed - i + 1
                            break
                    archer_position[archer][0] = archer_position[archer][0] + (archer.movement_speed - val)
                    archer_position[archer] = tuple(archer_position[archer])
                else:
                    archer_position[archer] = list(archer_position[archer])
                    pos = archer_position[archer]
                    val = 0
                    for i in range(1, archer.movement_speed + 1):
                        if (((pos[0], pos[1] + i) in occupied) and ((pos[0], pos[1] + i) not in village_occupied["Empty Space"])):
                            val = archer.movement_speed - i + 1
                            break
                    archer_position[archer][1] = archer_position[archer][1] + (archer.movement_speed - val)
                    archer_position[archer] = tuple(archer_position[archer])

            # Up until here, the archer is capable of moving towards the walls and past it by one archer.movement_speed.
            elif ((position[0] > 12) and (position[1] > 12)):
                
                add = 10000
                cc = []
    
                for closest_coordinate in village_occupied["Huts"]:
                    if (((abs(position[0] - closest_coordinate[0])) + (abs(position[1] - closest_coordinate[1]))) < add):
                        add = abs(position[0] - closest_coordinate[0]) + abs(position[1] - closest_coordinate[1])
                        cc = list(closest_coordinate)
                
                for closest_coordinate in village_occupied["Cannons"]:
                    if (((abs(position[0] - closest_coordinate[0])) + (abs(position[1] - closest_coordinate[1]))) < add):
                        add = abs(position[0] - closest_coordinate[0]) + abs(position[1] - closest_coordinate[1])
                        cc = list(closest_coordinate)
                        
                for closest_coordinate in village_occupied["Wizard Towers"]:
                    if (((abs(position[0] - closest_coordinate[0])) + (abs(position[1] - closest_coordinate[1]))) < add):
                        add = abs(position[0] - closest_coordinate[0]) + abs(position[1] - closest_coordinate[1])
                        cc = list(closest_coordinate)
                
                for closest_coordinate in village_occupied["Town Hall"]:
                    if (((abs(position[0] - closest_coordinate[0])) + (abs(position[1] - closest_coordinate[1]))) < add):
                        add = abs(position[0] - closest_coordinate[0]) + abs(position[1] - closest_coordinate[1])
                        cc = list(closest_coordinate)
                        
                y_difference = position[0] - cc[0]
                x_difference = position[1] - cc[1]
                
                # print("Moving to the closest coordinate of a building -", str(cc), "- from the current position:", str(position) + ".")
                
                if (((abs(y_difference) < abs(x_difference)) and (y_difference != 0)) or (x_difference == 0)):
                    if (y_difference > 0):
                        archer_position[archer] = list(archer_position[archer])
                        pos = archer_position[archer]
                        val = 0
                        for i in range(1, archer.movement_speed + 1):
                            if (((pos[0] - i, pos[1]) in occupied) and ((pos[0] - i, pos[1]) not in village_occupied["Empty Space"])):
                                val = archer.movement_speed - i + 1
                                break
                        # print("Moving up.")
                        archer_position[archer][0] = archer_position[archer][0] - (archer.movement_speed - val)
                        archer_position[archer] = tuple(archer_position[archer])
                    elif (y_difference < 0):
                        archer_position[archer] = list(archer_position[archer])
                        pos = archer_position[archer]
                        val = 0
                        for i in range(1, archer.movement_speed + 1):
                            if (((pos[0] + i, pos[1]) in occupied) and ((pos[0] + i, pos[1]) not in village_occupied["Empty Space"])):
                                val = archer.movement_speed - i + 1
                                break
                        # print("Moving down.")
                        archer_position[archer][0] = archer_position[archer][0] + (archer.movement_speed - val)
                        archer_position[archer] = tuple(archer_position[archer])
                elif (((abs(y_difference) > abs(x_difference)) and (x_difference != 0)) or (y_difference == 0)):
                    if (x_difference > 0):
                        archer_position[archer] = list(archer_position[archer])
                        pos = archer_position[archer]
                        val = 0
                        for i in range(1, archer.movement_speed + 1):
                            if (((pos[0], pos[1] - i) in occupied) and ((pos[0], pos[1] - i) not in village_occupied["Empty Space"])):
                                val = archer.movement_speed - i + 1
                                break
                        # print("Moving left.")
                        archer_position[archer][1] = archer_position[archer][1] - (archer.movement_speed - val)
                        archer_position[archer] = tuple(archer_position[archer])
                    elif (x_difference < 0):
                        archer_position[archer] = list(archer_position[archer])
                        pos = archer_position[archer]
                        val = 0
                        for i in range(1, archer.movement_speed + 1):
                            if (((pos[0], pos[1] + i) in occupied) and ((pos[0], pos[1] + i) not in village_occupied["Empty Space"])):
                                val = archer.movement_speed - i + 1
                                break
                        # print("Moving right.")
                        archer_position[archer][1] = archer_position[archer][1] + (archer.movement_speed - val)
                        archer_position[archer] = tuple(archer_position[archer])
                elif (abs(y_difference) == abs(x_difference)):
                    if (y_difference > 0):
                        archer_position[archer] = list(archer_position[archer])
                        pos = archer_position[archer]
                        val = 0
                        for i in range(1, archer.movement_speed + 1):
                            if (((pos[0] - i, pos[1]) in occupied) and ((pos[0] - i, pos[1]) not in village_occupied["Empty Space"])):
                                val = archer.movement_speed - i + 1
                                break
                        # print("Moving up.")
                        archer_position[archer][0] = archer_position[archer][0] - (archer.movement_speed - val)
                        archer_position[archer] = tuple(archer_position[archer])
                    elif (y_difference < 0):
                        archer_position[archer] = list(archer_position[archer])
                        pos = archer_position[archer]
                        val = 0
                        for i in range(1, archer.movement_speed + 1):
                            if (((pos[0] + i, pos[1]) in occupied) and ((pos[0] + i, pos[1]) not in village_occupied["Empty Space"])):
                                val = archer.movement_speed - i + 1
                                break
                        # print("Moving down.")
                        archer_position[archer][0] = archer_position[archer][0] + (archer.movement_speed - val)
                        archer_position[archer] = tuple(archer_position[archer])

def clear():
      
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
        
level = 0

Ray = Village("Ray", 40, 80)
RayHall = Town_Hall(4, 6, 432)
Hut1 = Hut(1, 60)
Hut2 = Hut(2, 60)
Hut3 = Hut(3, 60)
Hut4 = Hut(4, 60)
Hut5 = Hut(5, 60)
Hut6 = Hut(6, 60)
Hut7 = Hut(7, 60)
Hut8 = Hut(8, 60)
hut_list = [Hut1, Hut2, Hut3, Hut4, Hut5, Hut6, Hut7, Hut8]
Cannon1 = Cannon(1, 2, 10, 80)
Cannon2 = Cannon(2, 2, 6, 80)
Cannon3 = Cannon(3, 4, 5, 80)
Cannon4 = Cannon(4, 1, 18, 80)
Cannon5 = Cannon(5, 3, 6, 80)
Cannon6 = Cannon(6, 1, 12, 80)
cannon_list = [Cannon1, Cannon2, Cannon3, Cannon4, Cannon5, Cannon6]
Wizard_Tower1 = Wizard_Tower(1, 3, 15, 3, 80)
Wizard_Tower2 = Wizard_Tower(2, 3, 11, 4, 80)
Wizard_Tower3 = Wizard_Tower(3, 5, 10, 2, 80)
Wizard_Tower4 = Wizard_Tower(4, 2, 23, 3, 80)
wizard_tower_list = [Wizard_Tower1, Wizard_Tower2, Wizard_Tower3, Wizard_Tower4]
SP1 = Spawning_Point(1, (16, 4))
SP2 = Spawning_Point(2, (6, 14))
SP3 = Spawning_Point(3, (38, 3))
spawning_point_list = [SP1, SP2, SP3]
Raja = King(100, 4000, 1)
Rani = Queen(30, 5, 8, 300, 2)
Barbarian1 = Barbarian(1, 10, 150, 1)
Barbarian2 = Barbarian(2, 14, 120, 1)
Barbarian3 = Barbarian(3, 18, 120, 2)
Barbarian4 = Barbarian(4, 14, 140, 1)
Barbarian5 = Barbarian(5, 18, 130, 2)
barbarian_list = [Barbarian1, Barbarian2, Barbarian3, Barbarian4, Barbarian5]
Archer1 = Archer(1, 6, 3, 80, 1)
Archer2 = Archer(2, 8, 4, 100, 1)
Archer3 = Archer(3, 8, 3, 120, 1)
archer_list = [Archer1, Archer2, Archer3]

occupied = []
village_occupied = {"Huts" : [], "Cannons" : [], "Wizard Towers": [], "Town Hall" : [], "Walls": {}, "Empty Space": [], "Spawning Points": []}
king_position = ()
queen_position = ()
barbarian_position = {}
archer_position = {}
# balloon_position = {}

IsEnd = False
print_bg_stats = True
king_spawned = False
queen_spawned = False

character = input("Type 'q' for choosing Queen and 'k' for choosing King: ")

if (character == 'q'):

    while (level <= 3):
    
        if (level == 1):
            formVillage(Ray, RayHall, hut_list[0:4], cannon_list[0: 4], wizard_tower_list[0:2])
            while(not IsEnd):
                
                cannon_attack(cannon_list[0:4], Rani)
                wizard_tower_attack(wizard_tower_list[0:2], Rani)
                barbarian_movement(Ray)
                barbarian_attack(Rani, barbarian_list, archer_list, RayHall, hut_list[0:4], cannon_list[0:4], wizard_tower_list[0:2])
                archer_movement(Ray)
                archer_attack(Rani, barbarian_list, archer_list, RayHall, hut_list[0:4], cannon_list[0:4], wizard_tower_list[0:2])

                if (print_bg_stats):
                    # clear()
                    printBackground(Ray, RayHall, hut_list[0:4], cannon_list[0:4], wizard_tower_list[0:2], Rani)
                    print("\n\n")
                    printStats(RayHall, hut_list[0:4], cannon_list[0:4], wizard_tower_list[0:2], Rani, barbarian_list, archer_list)
                    print("\n")
                    print_bg_stats = False
                check = get_input()

                if ((check == 'w') or (check == 's') or (check == 'a') or (check == 'd')):
                    queen_move(Rani, check)
                elif (check == "l"):
                    clear()
                    print_bg_stats = True
                elif (check == "y"):
                    barbarian_movement(Ray)
                    barbarian_attack(Rani, barbarian_list, archer_list, RayHall, hut_list[0:4], cannon_list[0:4], wizard_tower_list[0:2])
                elif (check == "m"):
                    print(barbarian_position)
                elif (check == 'r'):
                    rage_spell(Rani, barbarian_list, archer_list)
                elif (check == 'h'):
                    heal_spell(Rani, barbarian_list, archer_list)
                elif (check == ' '):
                    queen_attack(Rani, barbarian_list, archer_list, RayHall, hut_list[0:4], cannon_list[0:4], wizard_tower_list[0:2])
                elif ((check == 'p') or (check == 'o') or (check == 'i')):
                    if ((queen_position != ()) and (len(barbarian_position) == len(barbarian_list)) and (len(archer_position) == len(archer_list))):
                        print("All troops on field.")
                    else:
                        if (not queen_spawned):
                            spawn_queen(check, spawning_point_list)
                        else:
                            if (not (len(barbarian_position) == len(barbarian_list))):
                                barbarian_spawn(check, barbarian_list, spawning_point_list)
                            elif (len(barbarian_position) == len(barbarian_list)):
                                archer_spawn(check, archer_list, spawning_point_list)
                                print("Here are the archers")
                elif (check == 'x'):
                    print("Exiting")
                    sys.exit(0)

                if (check_situation(RayHall, hut_list[0:4], cannon_list[0:4], wizard_tower_list[0:2], Rani, barbarian_list, archer_list) == 2):
                    RayHall.HP = Ray
                    for hut in hut_list:
                        hut.HP = hut.totalHP
                    for cannon in cannon_list:
                        cannon.HP = cannon.totalHP
                    for wizard_tower in wizard_tower_list:
                        wizard_tower.HP = wizard_tower.totalHP
                    Rani.HP = Rani.totalHP
                    for barbarian in barbarian_list:
                        barbarian.HP = barbarian.totalHP
                    for archer in archer_list:
                        archer.HP = archer.totalHP
                    level += 1
                    break
                
                if (check != None):
                    time.sleep(0.3)

        if (level == 2):
            formVillage(Ray, RayHall, hut_list[0:6], cannon_list[0: 5], wizard_tower_list[0:3])
            while(not IsEnd):

                cannon_attack(cannon_list[0:5], Rani)
                wizard_tower_attack(wizard_tower_list[0:3], Rani)
                barbarian_movement(Ray)
                barbarian_attack(Rani, barbarian_list, archer_list, RayHall, hut_list[0:6], cannon_list[0:5], wizard_tower_list[0:3])
                archer_movement(Ray)
                archer_attack(Rani, barbarian_list, archer_list, RayHall, hut_list[0:6], cannon_list[0:5], wizard_tower_list[0:3])

                if (print_bg_stats):
                    # clear()
                    printBackground(Ray, RayHall, hut_list[0:6], cannon_list[0:5], wizard_tower_list[0:3], Rani)
                    print("\n\n")
                    printStats(RayHall, hut_list[0:6], cannon_list[0:5], wizard_tower_list[0:3], Rani, barbarian_list, archer_list)
                    print("\n")
                    print_bg_stats = False
                check = get_input()

                if ((check == 'w') or (check == 's') or (check == 'a') or (check == 'd')):
                    queen_move(Rani, check)
                elif (check == "l"):
                    print_bg_stats = True
                elif (check == "y"):
                    barbarian_movement(Ray)
                    barbarian_attack(Rani, barbarian_list, archer_list, RayHall, hut_list[0:6], cannon_list[0:5], wizard_tower_list[0:3])
                elif (check == "m"):
                    print(barbarian_position)
                elif (check == 'r'):
                    rage_spell(Rani, barbarian_list)
                elif (check == 'h'):
                    heal_spell(Rani, barbarian_list)
                elif (check == ' '):
                    queen_attack(Rani, barbarian_list, archer_list, RayHall, hut_list[0:6], cannon_list[0:5], wizard_tower_list[0:3])
                elif ((check == 'p') or (check == 'o') or (check == 'i')):
                    if ((queen_position != ()) and (len(barbarian_position) == len(barbarian_list))):
                        print("All troops on field.")
                    else:
                        if (not queen_spawned):
                            spawn_queen(check, spawning_point_list)
                        else:
                            if (not (len(barbarian_position) == len(barbarian_list))):
                                barbarian_spawn(check, barbarian_list, spawning_point_list)
                            elif (len(barbarian_position) == len(barbarian_list)):
                                archer_spawn(check, archer_list, spawning_point_list)
                elif (check == 'x'):
                    print("Exiting")
                    sys.exit(0)

                if (check_situation(RayHall, hut_list[0:6], cannon_list[0:5], wizard_tower_list[0:3], Rani, barbarian_list, archer_list) == 2):
                    RayHall.HP = Ray
                    for hut in hut_list:
                        hut.HP = hut.totalHP
                    for cannon in cannon_list:
                        cannon.HP = cannon.totalHP
                    for wizard_tower in wizard_tower_list:
                        wizard_tower.HP = wizard_tower.totalHP
                    Rani.HP = Rani.totalHP
                    for barbarian in barbarian_list:
                        barbarian.HP = barbarian.totalHP
                    for archer in archer_list:
                        archer.HP = archer.totalHP
                    level += 1
                    break
                
                if (check != None):
                    time.sleep(0.3)

        if (level == 3):
            formVillage(Ray, RayHall, hut_list[0:8], cannon_list[0: 6], wizard_tower_list[0:4])
            while(not IsEnd):

                cannon_attack(cannon_list[0:6], Rani)
                wizard_tower_attack(wizard_tower_list[0:4], Rani)
                barbarian_movement(Ray)
                barbarian_attack(Rani, barbarian_list, archer_list, RayHall, hut_list[0:8], cannon_list[0:6], wizard_tower_list[0:4])
                archer_movement(Ray)
                archer_attack(Rani, barbarian_list, archer_list, RayHall, hut_list[0:8], cannon_list[0:6], wizard_tower_list[0:4])

                if (print_bg_stats):
                    printBackground(Ray, RayHall, hut_list[0:8], cannon_list[0:6], wizard_tower_list[0:4], Rani)
                    print("\n\n")
                    printStats(RayHall, hut_list[0:8], cannon_list[0:6], wizard_tower_list[0:4], Rani, barbarian_list, archer_list)
                    print("\n")
                    print_bg_stats = False
                check = get_input()

                if ((check == 'w') or (check == 's') or (check == 'a') or (check == 'd')):
                    queen_move(Rani, check)
                elif (check == "l"):
                    print_bg_stats = True
                elif (check == "y"):
                    barbarian_movement(Ray)
                    barbarian_attack(Rani, barbarian_list, archer_list, RayHall, hut_list[0:8], cannon_list[0:6], wizard_tower_list[0:2])
                elif (check == "m"):
                    print(barbarian_position)
                elif (check == 'r'):
                    rage_spell(Rani, barbarian_list)
                elif (check == 'h'):
                    heal_spell(Rani, barbarian_list)
                elif (check == ' '):
                    queen_attack(Rani, barbarian_list, archer_list, RayHall, hut_list[0:8], cannon_list[0:6], wizard_tower_list[0:2])
                elif ((check == 'p') or (check == 'o') or (check == 'i')):
                    if ((queen_position != ()) and (len(barbarian_position) == len(barbarian_list))):
                        print("All troops on field.")
                    else:
                        if (not queen_spawned):
                            spawn_queen(check, spawning_point_list)
                        else:
                            if (not (len(barbarian_position) == len(barbarian_list))):
                                barbarian_spawn(check, barbarian_list, spawning_point_list)
                            elif (len(barbarian_position) == len(barbarian_list)):
                                archer_spawn(check, archer_list, spawning_point_list)
                elif (check == 'x'):
                    print("Exiting")
                    sys.exit(0)

                if (check_situation(RayHall, hut_list[0:8], cannon_list[0:6], wizard_tower_list[0:4], Rani, barbarian_list, archer_list) == 2):
                    RayHall.HP = Ray
                    for hut in hut_list:
                        hut.HP = hut.totalHP
                    for cannon in cannon_list:
                        cannon.HP = cannon.totalHP
                    for wizard_tower in wizard_tower_list:
                        wizard_tower.HP = wizard_tower.totalHP
                    Rani.HP = Rani.totalHP
                    for barbarian in barbarian_list:
                        barbarian.HP = barbarian.totalHP
                    for archer in archer_list:
                        archer.HP = archer.totalHP
                    level += 1
                    break
                
                if (check != None):
                    time.sleep(0.3)

elif (character == 'k'):

    while (level <= 3):

        if (level == 0):
            formVillage(Ray, RayHall, hut_list[0:1], cannon_list[0: 1], wizard_tower_list[0:1])
            while(not IsEnd):
                
                cannon_attack(cannon_list[0:1], Raja)
                wizard_tower_attack(wizard_tower_list[0:1], Raja)
                barbarian_movement(Ray)
                barbarian_attack(Raja, barbarian_list, archer_list, RayHall, hut_list[0:1], cannon_list[0:1], wizard_tower_list[0:1])
                archer_movement(Ray)
                archer_attack(Raja, barbarian_list, archer_list, RayHall, hut_list[0:1], cannon_list[0:1], wizard_tower_list[0:1])

                if (print_bg_stats):
                    # clear()
                    printBackground(Ray, RayHall, hut_list[0:1], cannon_list[0:1], wizard_tower_list[0:1], Raja)
                    print("\n\n")
                    printStats(RayHall, hut_list[0:1], cannon_list[0:1], wizard_tower_list[0:1], Raja, barbarian_list, archer_list)
                    print("\n")
                    print_bg_stats = False
                check = get_input()

                if ((check == 'w') or (check == 's') or (check == 'a') or (check == 'd')):
                    king_move(Raja, check)
                elif (check == "l"):
                    print_bg_stats = True
                elif (check == "y"):
                    Raja.movement_speed = 10
                elif (check == "x"):
                    Raja.movement_speed = 1
                    # barbarian_movement(Ray)
                    # barbarian_attack(Raja, barbarian_list, archer_list, RayHall, hut_list[0:1], cannon_list[0:1], wizard_tower_list[0:1])
                elif (check == "m"):
                    print(barbarian_position)
                elif (check == 'r'):
                    rage_spell(Raja, barbarian_list, archer_list)
                elif (check == 'h'):
                    heal_spell(Raja, barbarian_list, archer_list)
                elif (check == ' '):
                    king_attack(Raja, barbarian_list, archer_list, RayHall, hut_list[0:1], cannon_list[0:1], wizard_tower_list[0:1])
                # elif (check = 't')
                elif ((check == 'p') or (check == 'o') or (check == 'i')):
                    if ((king_position != ()) and (len(barbarian_position) == len(barbarian_list)) and (len(archer_position) == len(archer_list))):
                        print("All troops on field.")
                    else:
                        if (not king_spawned):
                            spawn_king(check, spawning_point_list)
                        else:
                            if (not (len(barbarian_position) == len(barbarian_list))):
                                barbarian_spawn(check, barbarian_list, spawning_point_list)
                            elif (len(barbarian_position) == len(barbarian_list)):
                                archer_spawn(check, archer_list, spawning_point_list)
                                print("Here are the archers")
                elif (check == 'x'):
                    print("Exiting")
                    sys.exit(0)

                if (check_situation(RayHall, hut_list[0:1], cannon_list[0:1], wizard_tower_list[0:1], Raja, barbarian_list, archer_list) == 2):
                    RayHall.HP = RayHall.totalHP
                    for hut in hut_list:
                        hut.HP = hut.totalHP
                    for cannon in cannon_list:
                        cannon.HP = cannon.totalHP
                    for wizard_tower in wizard_tower_list:
                        wizard_tower.HP = wizard_tower.totalHP
                    Raja.HP = Raja.totalHP
                    for barbarian in barbarian_list:
                        barbarian.HP = barbarian.totalHP
                    for archer in archer_list:
                        archer.HP = archer.totalHP
                    level += 1
                    isEnd = False
                    break
                
                if (check != None):
                    time.sleep(0.3)
    
        if (level == 1):
            formVillage(Ray, RayHall, hut_list[0:4], cannon_list[0: 4], wizard_tower_list[0:2])
            printBackground(Ray, RayHall, hut_list[0:4], cannon_list[0:4], wizard_tower_list[0:2], Raja)
            isEnd = True
            while(not IsEnd):

                if (print_bg_stats):
                    # clear()
                    printBackground(Ray, RayHall, hut_list[0:4], cannon_list[0:4], wizard_tower_list[0:2], Raja)
                    print("\n\n")
                    printStats(RayHall, hut_list[0:4], cannon_list[0:4], wizard_tower_list[0:2], Raja, barbarian_list, archer_list)
                    print("\n")
                    print_bg_stats = False
                check = get_input()

                cannon_attack(cannon_list[0:4], Raja)
                wizard_tower_attack(wizard_tower_list[0:2], Raja)
                barbarian_movement(Ray)
                barbarian_attack(Raja, barbarian_list, archer_list, RayHall, hut_list[0:4], cannon_list[0:4], wizard_tower_list[0:2])
                archer_movement(Ray)
                archer_attack(Raja, barbarian_list, archer_list, RayHall, hut_list[0:4], cannon_list[0:4], wizard_tower_list[0:2])

                if ((check == 'w') or (check == 's') or (check == 'a') or (check == 'd')):
                    king_move(Raja, check)
                elif (check == "l"):
                    print_bg_stats = True
                elif (check == "y"):
                    barbarian_movement(Ray)
                    barbarian_attack(Raja, barbarian_list, archer_list, RayHall, hut_list[0:4], cannon_list[0:4], wizard_tower_list[0:2])
                elif (check == "m"):
                    print(barbarian_position)
                elif (check == 'r'):
                    rage_spell(Raja, barbarian_list, archer_list)
                elif (check == 'h'):
                    heal_spell(Raja, barbarian_list, archer_list)
                elif (check == ' '):
                    king_attack(Raja, barbarian_list, archer_list, RayHall, hut_list[0:4], cannon_list[0:4], wizard_tower_list[0:2])
                elif ((check == 'p') or (check == 'o') or (check == 'i')):
                    if ((king_position != ()) and (len(barbarian_position) == len(barbarian_list)) and (len(archer_position) == len(archer_list))):
                        print("All troops on field.")
                    else:
                        if (not king_spawned):
                            spawn_king(check, spawning_point_list)
                        else:
                            if (not (len(barbarian_position) == len(barbarian_list))):
                                barbarian_spawn(check, barbarian_list, spawning_point_list)
                            elif (len(barbarian_position) == len(barbarian_list)):
                                archer_spawn(check, archer_list, spawning_point_list)
                                print("Here are the archers")
                elif (check == 'x'):
                    print("Exiting")
                    sys.exit(0)

                if (check_situation(RayHall, hut_list[0:4], cannon_list[0:4], wizard_tower_list[0:2], Raja, barbarian_list, archer_list) == 2):
                    RayHall.HP = RayHall.totalHP
                    for hut in hut_list:
                        hut.HP = hut.totalHP
                    for cannon in cannon_list:
                        cannon.HP = cannon.totalHP
                    for wizard_tower in wizard_tower_list:
                        wizard_tower.HP = wizard_tower.totalHP
                    Raja.HP = Raja.totalHP
                    for barbarian in barbarian_list:
                        barbarian.HP = barbarian.totalHP
                    for archer in archer_list:
                        archer.HP = archer.totalHP
                    level += 1
                    break
                
                if (check != None):
                    time.sleep(0.3)

        if (level == 2):
            formVillage(Ray, RayHall, hut_list[0:6], cannon_list[0: 5], wizard_tower_list[0:3])
            while(not IsEnd):

                cannon_attack(cannon_list[0:5], Raja)
                wizard_tower_attack(wizard_tower_list[0:3], Raja)
                barbarian_movement(Ray)
                barbarian_attack(Raja, barbarian_list, archer_list, RayHall, hut_list[0:6], cannon_list[0:5], wizard_tower_list[0:3])
                archer_movement(Ray)
                archer_attack(Raja, barbarian_list, archer_list, RayHall, hut_list[0:6], cannon_list[0:5], wizard_tower_list[0:3])

                if (print_bg_stats):
                    # clear()
                    printBackground(Ray, RayHall, hut_list[0:6], cannon_list[0:5], wizard_tower_list[0:3], Raja)
                    print("\n\n")
                    printStats(RayHall, hut_list[0:6], cannon_list[0:5], wizard_tower_list[0:3], Raja, barbarian_list, archer_list)
                    print("\n")
                    print_bg_stats = False
                check = get_input()

                if ((check == 'w') or (check == 's') or (check == 'a') or (check == 'd')):
                    king_move(Raja, check)
                elif (check == "l"):
                    print_bg_stats = True
                elif (check == "y"):
                    barbarian_movement(Ray)
                    barbarian_attack(Raja, barbarian_list, archer_list, RayHall, hut_list[0:6], cannon_list[0:5], wizard_tower_list[0:3])
                elif (check == "m"):
                    print(barbarian_position)
                elif (check == 'r'):
                    rage_spell(Raja, barbarian_list)
                elif (check == 'h'):
                    heal_spell(Raja, barbarian_list)
                elif (check == ' '):
                    king_attack(Raja, barbarian_list, archer_list, RayHall, hut_list[0:6], cannon_list[0:5], wizard_tower_list[0:3])
                elif ((check == 'p') or (check == 'o') or (check == 'i')):
                    if ((king_position != ()) and (len(barbarian_position) == len(barbarian_list))):
                        print("All troops on field.")
                    else:
                        if (not king_spawned):
                            spawn_king(check, spawning_point_list)
                        else:
                            if (not (len(barbarian_position) == len(barbarian_list))):
                                barbarian_spawn(check, barbarian_list, spawning_point_list)
                            elif (len(barbarian_position) == len(barbarian_list)):
                                archer_spawn(check, archer_list, spawning_point_list)
                elif (check == 'x'):
                    print("Exiting")
                    sys.exit(0)

                if (check_situation(RayHall, hut_list[0:6], cannon_list[0:5], wizard_tower_list[0:3], Raja, barbarian_list, archer_list) == 2):
                    RayHall.HP = Ray
                    for hut in hut_list:
                        hut.HP = hut.totalHP
                    for cannon in cannon_list:
                        cannon.HP = cannon.totalHP
                    for wizard_tower in wizard_tower_list:
                        wizard_tower.HP = wizard_tower.totalHP
                    Raja.HP = Raja.totalHP
                    for barbarian in barbarian_list:
                        barbarian.HP = barbarian.totalHP
                    for archer in archer_list:
                        archer.HP = archer.totalHP
                    level += 1
                    break
                
                if (check != None):
                    time.sleep(0.3)

        if (level == 3):
            formVillage(Ray, RayHall, hut_list[0:8], cannon_list[0: 6], wizard_tower_list[0:4])
            while(not IsEnd):

                cannon_attack(cannon_list[0:6], Raja)
                wizard_tower_attack(wizard_tower_list[0:4], Raja)
                barbarian_movement(Ray)
                barbarian_attack(Raja, barbarian_list, archer_list, RayHall, hut_list[0:8], cannon_list[0:6], wizard_tower_list[0:4])
                archer_movement(Ray)
                archer_attack(Raja, barbarian_list, archer_list, RayHall, hut_list[0:8], cannon_list[0:6], wizard_tower_list[0:4])

                if (print_bg_stats):
                    # clear()
                    printBackground(Ray, RayHall, hut_list[0:8], cannon_list[0:6], wizard_tower_list[0:4], Raja)
                    print("\n\n")
                    printStats(RayHall, hut_list[0:8], cannon_list[0:6], wizard_tower_list[0:4], Raja, barbarian_list, archer_list)
                    print("\n")
                    print_bg_stats = False
                check = get_input()

                if ((check == 'w') or (check == 's') or (check == 'a') or (check == 'd')):
                    king_move(Raja, check)
                elif (check == "l"):
                    print_bg_stats = True
                elif (check == "y"):
                    barbarian_movement(Ray)
                    barbarian_attack(Raja, barbarian_list, archer_list, RayHall, hut_list[0:8], cannon_list[0:6], wizard_tower_list[0:2])
                elif (check == "m"):
                    print(barbarian_position)
                elif (check == 'r'):
                    rage_spell(Raja, barbarian_list)
                elif (check == 'h'):
                    heal_spell(Raja, barbarian_list)
                elif (check == ' '):
                    king_attack(Raja, barbarian_list, archer_list, RayHall, hut_list[0:8], cannon_list[0:6], wizard_tower_list[0:2])
                elif ((check == 'p') or (check == 'o') or (check == 'i')):
                    if ((king_position != ()) and (len(barbarian_position) == len(barbarian_list))):
                        print("All troops on field.")
                    else:
                        if (not king_spawned):
                            spawn_king(check, spawning_point_list)
                        else:
                            if (not (len(barbarian_position) == len(barbarian_list))):
                                barbarian_spawn(check, barbarian_list, spawning_point_list)
                            elif (len(barbarian_position) == len(barbarian_list)):
                                archer_spawn(check, archer_list, spawning_point_list)
                elif (check == 'x'):
                    print("Exiting")
                    sys.exit(0)

                if (check_situation(RayHall, hut_list[0:8], cannon_list[0:6], wizard_tower_list[0:4], Raja, barbarian_list, archer_list) == 2):
                    RayHall.HP = Ray
                    for hut in hut_list:
                        hut.HP = hut.totalHP
                    for cannon in cannon_list:
                        cannon.HP = cannon.totalHP
                    for wizard_tower in wizard_tower_list:
                        wizard_tower.HP = wizard_tower.totalHP
                    Raja.HP = Raja.totalHP
                    for barbarian in barbarian_list:
                        barbarian.HP = barbarian.totalHP
                    for archer in archer_list:
                        archer.HP = archer.totalHP
                    level += 1
                    break
                
                if (check != None):
                    time.sleep(0.3)
