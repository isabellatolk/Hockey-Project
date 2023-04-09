import random
import time
from os import system, name
from colorama import init
from termcolor import cprint
init()
#system('mode con: cols=105 lines=100')


rink = [["." for x in range(9)] for y in range(20)]

goals = {
    "blue_goal": 0,
    "red_goal": 0
}

stats = {
    "winger": {
        "speed": 5,
        "toughness": 3,
        "strength": 3,
        "talent": 5,
        "creativity": 4
    },
    "defenseman": {
        "speed": 3,
        "toughness": 4,
        "strength": 5,
        "talent": 4,
        "creativity": 4
    },
    "center": {
        "speed": 4,
        "toughness": 4,
        "strength": 3,
        "talent": 4,
        "creativity": 5
    },
    "goalie": {
        "speed": 2,
        "toughness": -1,
        "strength": -1,
        "talent": 4,
        "creativity": 4
    }
}

red_team = {
    "center":{
        "icon": "RC",
        "x": 4,
        "y": 9
    },
    "rightwinger":{
        "icon": "RW",
        "x": 6,
        "y": 9
    },
    "leftwinger":{
        "icon": "RW",
        "x": 2,
        "y": 9
    },
    "rightdefenseman":{
        "icon": "RD",
        "x": 5,
        "y": 8
    },
    "leftdefenseman":{
        "icon": "RD",
        "x": 3,
        "y": 8
    },
    "goalie":{
        "icon": "RG",
        "x": 4,
        "y": 1
    }
}

blue_team = {
    "center":{
        "icon": "BCP",
        "x": 4,
        "y": 10
    },
    "rightwinger":{
        "icon": "BW",
        "x": 6,
        "y": 10
    },
    "leftwinger":{
        "icon": "BW",
        "x": 2,
        "y": 10
    },
    "rightdefenseman":{
        "icon": "BD",
        "x": 5,
        "y": 11
    },
    "leftdefenseman":{
        "icon": "BD",
        "x": 3,
        "y": 11
    },
    "goalie":{
        "icon": "BG",
        "x": 4,
        "y": 18
    }
}


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


#title menu
def print_menu():
    print("  _______ ______ _____  __  __ _____ _   _          _        _    _  ____   _____ _  __________     __")
    print(" |__   __|  ____|  __ \|  \/  |_   _| \ | |   /\   | |      | |  | |/ __ \ / ____| |/ /  ____\ \   / /")
    print("    | |  | |__  | |__) | \  / | | | |  \| |  /  \  | |      | |__| | |  | | |    | ' /| |__   \ \_/ / ")
    print("    | |  |  __| |  _  /| |\/| | | | | . ` | / /\ \ | |      |  __  | |  | | |    |  < |  __|   \   /  ")
    print("    | |  | |____| | \ \| |  | |_| |_| |\  |/ ____ \| |____  | |  | | |__| | |____| . \| |____   | |   ")
    print("    |_|  |______|_|  \_\_|  |_|_____|_| \_/_/    \_\______| |_|  |_|\____/ \_____|_|\_\______|  |_|   ")
    cprint("\n\n\n\t\t\t\t\tPress Enter to play", attrs=['blink'])

    help = input("")
    return help

def print_goal():
    cprint("                                 _____  ____          _        _   _ ", attrs=['blink'])
    cprint("                                / ____|/ __ \   /\   | |      | | | |", attrs=['blink'])
    cprint("                               | |  __| |  | | /  \  | |      | | | |", attrs=['blink'])
    cprint("                               | | |_ | |  | |/ /\ \ | |      | | | |", attrs=['blink'])
    cprint("                               | |__| | |__| / ____ \| |____  |_| |_|", attrs=['blink'])
    cprint("                                \_____|\____/_/    \_\______| (_) (_)", attrs=['blink'])
    cprint("\n\n\n\n\n")
    cprint("                                                               .''.             " , attrs=['blink'])
    cprint("                                   .''.      .        *''*    :_\/_:     .      " , attrs=['blink'])
    cprint("                                  :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'.   ", attrs=['blink'])
    cprint("                              .''.: /\ :   ./)\   ':'* /\ * :  '..'.  -=:o:=-   ", attrs=['blink'])
    cprint("                             :_\/_:'.:::.    ' *''*    * '.\'/.' _\(/_'.':'.'   ", attrs=['blink'])
    cprint("                             : /\ : :::::     *_\/_*     -= o =-  /)\    '  *   ", attrs=['blink'])
    cprint("                              '..'  ':::'     * /\ *     .'/.\'.   '            ", attrs=['blink'])
    cprint("                                  *            *..*         :                   ", attrs=['blink'])
    cprint("                                   *                                            ", attrs=['blink'])
    cprint("                                    *                                           ", attrs=['blink'])



def help_menu():
    print("\n\nBlue Team has first move")
    print("On start of turn you will be promted to choose a player to activate")
    print("To move players type: N, NE, E, SE, S, SW, W, NW, or ")
    print("type an action: PASS, TAP, SHOOT, HIT, or POKE")
    print("If you still have movement or an action and want to end your turn, type STOP")
    print("Every time you move you will be prompted for an action")
    print("After your player has finished movement/actions your other players are able to move and will be prompted to move in this order:")
    print("C, LW, RW, LD, RD\n")
    print("Problems with program:")
    print("-Players can get into same space as other players")
    print("-If a player moves outside the rink, the game will quit with an error\n\n\n")


def print_rink(rink):
    for i in range(20):
        for j in range(9):
            rink[i][j] = "."

    for player in red_team:
        rink[red_team[player]["y"]][red_team[player]["x"]] = red_team[player]["icon"]
    for player in blue_team:
        rink[blue_team[player]["y"]][blue_team[player]["x"]] = blue_team[player]["icon"]

    cprint("blue: ", "blue", end="")
    cprint(goals["blue_goal"], "white", end=" ")
    cprint("\t\t     " + str(goals["red_goal"]), "white", end="")
    cprint(" :red", "red")
    print("___________________________________")
    for i in range(20):
        for j in range(9):
            if((j == 3 or j == 6) and (i == 1 or i == 19 or i == 0 or i == 18)):
                print("|", end=' ')

            else:
                print(" ", end=' ')
            if((j > 2 and j < 6) and (i == 0 or i == 19)):
                print(" ", end=' ')
            else:
                if(rink[i][j] != "."):
                    if(rink[i][j][-1] == "P"):
                        cprint( rink[i][j][1], "white", end=' ')
                    elif(rink[i][j][0] == "R"):
                        cprint( rink[i][j][1], "red", end=' ')
                    elif(rink[i][j][0] == "B"):
                        cprint( rink[i][j][1], "blue", end=' ')
                else:
                    print(rink[i][j], end=' ')
        if(i == 1 or i == 17 or i == 9):
            print("\n-----------------------------------")
        elif(i == 0 or i == 18):
            print("\n            -------------")
        elif(i == 5 or i == 13):
            print("\n- - - - - - - - - - - - - - - - - - ")
        else:
            print("\n")
    print("___________________________________")


def move_team(turn, player):
    if(turn == "blue"):
        for blue in blue_team:
            if(blue != player):
                i = 0
                while i < 2:
                    if(blue.find("right") != -1):
                        right = blue.find("right")
                        direction = input("\nMove right "+blue[right+5:]+": ")
                    elif(blue.find("left") != -1):
                        right = blue.find("left")
                        direction = input("\nMove left "+blue[right+4:]+": ")
                    else:
                        direction = input("\nMove "+blue+": ")
                    direction = direction.lower()
                    if(direction == "stop" or direction == "n" or direction == "s" or direction == "e" or direction == "w" or direction == "nw" or direction == "ne" or direction == "sw" or direction == "se"):
                        if(direction != "stop"):
                            move_player(turn, blue, direction)
                            print_rink(rink)
                            i += 1
                        else:
                            break;

    if(turn == "red"):
        for red in red_team:
            if(red != player):
                i = 0
                while i < 2:
                    if(red.find("right") != -1):
                        right = red.find("right")
                        direction = input("\nMove right "+red[right+5:]+": ")
                    elif(red.find("left") != -1):
                        right = red.find("left")
                        direction = input("\nMove left "+red[right+4:]+": ")
                    else:
                        direction = input("\nMove "+red+": ")
                    direction = direction.lower()
                    if(direction == "stop" or direction == "n" or direction == "s" or direction == "e" or direction == "w" or direction == "nw" or direction == "ne" or direction == "sw" or direction == "se" ):
                        if(direction != "stop"):
                            move_player(turn, red, direction)
                            print_rink(rink)
                            i += 1
                        else:
                            break;

def move_check(x, y):
    if((x > 8 or x < 0) and (y > 19 or y < 0)): #out of bounds
        return -1
    else:
        return 0;

def move_player(turn, player, direction):
    if(direction.lower() == "n"):
        if(turn == "blue"):
            blue_team[player]["y"] -= 1
        else:
            red_team[player]["y"] -= 1
    if(direction.lower() == "s"):
        if(turn == "blue"):
            print(player)
            blue_team[player]["y"] += 1
        else:
            red_team[player]["y"] += 1
    if(direction.lower() == "w"):
        if(turn == "blue"):
            blue_team[player]["x"] -= 1
        else:
            red_team[player]["x"] -= 1
    if(direction.lower() == "e"):
        if(turn == "blue"):
            blue_team[player]["x"] += 1
        else:
            red_team[player]["x"] += 1
    if(direction.lower() == "ne"):
        if(turn == "blue"):
            blue_team[player]["y"] -= 1
            blue_team[player]["x"] += 1
        else:
            red_team[player]["y"] -= 1
            red_team[player]["x"] += 1
    if(direction.lower() == "nw"):
        if(turn == "blue"):
            blue_team[player]["y"] -= 1
            blue_team[player]["x"] -= 1
        else:
            red_team[player]["y"] -= 1
            red_team[player]["x"] -= 1
    if(direction.lower() == "se"):
        if(turn == "blue"):
            blue_team[player]["y"] += 1
            blue_team[player]["x"] += 1
        else:
            red_team[player]["y"] += 1
            red_team[player]["x"] += 1
    if(direction.lower() == "sw"):
        if(turn == "blue"):
            blue_team[player]["y"] += 1
            blue_team[player]["x"] -= 1
        else:
            red_team[player]["y"] += 1
            red_team[player]["x"] -= 1




def puck_swap(x, y, x2, y2, turn, action):
    if(action == "hit" or action == "poke" or action == "shoot"):
        blue_player = ''
        red_player = ''
        if(turn == "blue"):
            for blue in blue_team:
                if(blue_team[blue]["x"] == x and blue_team[blue]["y"] == y):
                    blue_player = blue
            for red in red_team:
                if(red_team[red]["x"] == x2 and red_team[red]["y"] == y2):
                    red_player = red
            red_team[red_player]["icon"] = red_team[red_player]["icon"][:-1]
            blue_team[blue_player]["icon"] = blue_team[blue_player]["icon"] + "P"
            return red_player #returns the opposing player (for their location)
        else:
            for blue in blue_team:
                if(blue_team[blue]["x"] == x2 and blue_team[blue]["y"] == y2):
                    blue_player = blue
            for red in red_team:
                if(red_team[red]["x"] == x and red_team[red]["y"] == y):
                    red_player = red
            red_team[red_player]["icon"] = red_team[red_player]["icon"] + "P"
            blue_team[blue_player]["icon"] = blue_team[blue_player]["icon"][:-1]
            return blue_player #returns the oppsing player (for their location)

    elif(action == "pass" or action == "tap"):
        passing_player = ''
        receiving_player = ''
        if(turn == "blue"):
            for blue in blue_team:
                if(blue_team[blue]["x"] == x and blue_team[blue]["y"] == y):
                    passing_player = blue
                if(blue_team[blue]["x"] == x2 and blue_team[blue]["y"] == y2):
                    receiving_player = blue
            blue_team[passing_player]["icon"] = blue_team[passing_player]["icon"][:-1]
            blue_team[receiving_player]["icon"] = blue_team[receiving_player]["icon"] + "P"
            return receiving_player #returns the opposing player (for their location)
        elif(turn == "red"):
            for red in red_team:
                if(red_team[red]["x"] == x and red_team[red]["y"] == y):
                    passing_player = red
                if(red_team[red]["x"] == x2 and red_team[red]["y"] == y2):
                    receiving_player = red
            red_team[passing_player]["icon"] = red_team[passing_player]["icon"][:-1]
            red_team[receiving_player]["icon"] = red_team[receiving_player]["icon"] + "P"
            return receiving_player #returns the opposing player (for their location)


def hit(turn, player, player_stat):
    x2 = -1
    y2 = -1
    opposing_player = ""
    if(turn == "blue"):
        x = blue_team[player]["x"]
        y = blue_team[player]["y"]
        for i in range(y-1, y+2):
            for j in range(x-1, x+2):
                if(rink[i][j][-1] == "P" and rink[i][j][0] == "R"):
                    x2 = j
                    y2 = i
    else:
        x = red_team[player]["x"]
        y = red_team[player]["y"]
        for i in range(y-1, y+2):
            for j in range(x-1, x+2):
                if(rink[i][j][-1] == "P" and rink[i][j][0] == "B"):
                    x2 = j
                    y2 = i

    if(x2 != -1 and y2 != -1):

        if(rink[y2][x2][1] == "W"):
            opposing_player = "winger"
        elif(rink[y2][x2][1] == "D"):
            opposing_player = "defenseman"
        elif(rink[y2][x2][1] == "C"):
            opposing_player = "center"
        else:
            opposing_player = "center"

        modifier = stats[player_stat]["strength"] - stats[opposing_player]["toughness"]

        if(random.randint(1, 6) - modifier >= 4):

            opposing = puck_swap(x, y, x2, y2, turn, "hit")

            dx = x2 - x
            dy = y2 - y
            if(turn == "blue"):
                blue_team[player]["x"] = x + dx
                blue_team[player]["y"] = y + dy
                red_team[opposing]["x"] = x2 + dx
                red_team[opposing]["y"] = y2 + dy
            else:
                red_team[player]["x"] = x + dx
                red_team[player]["y"] = y + dy
                blue_team[opposing]["x"] = x2 + dx
                blue_team[opposing]["y"] = y2 + dy


            print("Hit Successful!")

        else:
            print("Hit Failed!")

        return 1
    else:
        print("No one to Hit!\n")
        return 0



def poke(turn, player, player_stat):
    x2 = -1
    y2 = -1
    opposing_player = ""
    if(turn == "blue"):
        x = blue_team[player]["x"]
        y = blue_team[player]["y"]
        for i in range(y-1, y+2):
            for j in range(x-1, x+2):
                if(rink[i][j][-1] == "P" and rink[i][j][0] == "R"):
                    x2 = j
                    y2 = i
    else:
        x = red_team[player]["x"]
        y = red_team[player]["y"]
        for i in range(y-1, y+2):
            for j in range(x-1, x+2):
                if(rink[i][j][-1] == "P" and rink[i][j][0] == "B"):
                    x2 = j
                    y2 = i

    if(x2 != -1 and y2 != -1):

        if(rink[y2][x2][1] == "W"):
            opposing_player = "winger"
        elif(rink[y2][x2][1] == "D"):
            opposing_player = "defenseman"
        elif(rink[y2][x2][1] == "C"):
            opposing_player = "center"
        else:
            opposing_player = "center"

        modifier =  stats[player_stat]["talent"] - stats[opposing_player]["creativity"]

        if(random.randint(1, 6) - modifier >= 4):

            puck_swap(x, y, x2, y2, turn, "poke")
            print_rink(rink)
            print("Poke Successful!")
            return 1
        else:
            print("Poke Failed!")
            return 1
    else:
        print("No one to Poke!\n")
        return 0




def puck_pass(turn, passing_player, player_stat):
    x2 = -1
    y2 = -1
    player = ''
    while(player.lower() != "c" and player.lower() != "lw" and player.lower() != "rw" and player.lower() != "ld" and player.lower() != "rd" ):
        player = input("\nSelect a player to pass to: C, RW, LW, RD, LD: ")
    specific_player = ""
    if(player.lower() == "rw" or player.lower() == "lw"):
        player_stat = "winger"
        if(player.lower() == "rw"):
            specific_player = "rightwinger"
        else:
            specific_player = "leftwinger"
    elif(player.lower() == "rd" or player.lower() == "ld"):
        player_stat = "defenseman"
        if(player.lower() == "rd"):
            specific_player = "rightdefenseman"
        else:
            specific_player = "leftdefenseman"
    elif(player.lower() == "c"):
        player_stat = "center"
        specific_player = "center"

    if(turn == "blue"):
        x = blue_team[passing_player]["x"]
        y = blue_team[passing_player]["y"]
        x2 = blue_team[specific_player]["x"]
        y2 = blue_team[specific_player]["y"]
    else:
        x = red_team[passing_player]["x"]
        y = red_team[passing_player]["y"]
        x2 = red_team[specific_player]["x"]
        y2 = red_team[specific_player]["y"]

    puck_swap(x, y, x2, y2, turn, "pass")
    print_rink(rink)
    print("Puck passed!")
    return 1



def tap(turn, receiving_player, player_stat):
    x2 = '-1'
    y2 = '-1'
    if(turn == "blue"):
        x = blue_team[receiving_player]['x']
        y = blue_team[receiving_player]['y']
        for blue in blue_team:
            if(blue_team[blue]["icon"][-1] == "P"):
                x2 = blue_team[blue]["x"]
                y2 = blue_team[blue]["y"]
    if(turn == "red"):
        x = red_team[receiving_player]['x']
        y = red_team[receiving_player]['y']
        for red in red_team:
            if(red_team[red]["icon"][-1] == "P"):
                x2 = red_team[red]["x"]
                y2 = red_team[red]["y"]
    puck_swap(x2, y2, x, y, turn, "tap")
    print_rink(rink)
    print("Puck received!")
    return 1



def players_reset(turn):
    blue_team['center']['x'] = 4
    blue_team['center']['y'] = 10
    blue_team['rightwinger']['x'] = 6
    blue_team['rightwinger']['y'] =  10
    blue_team['leftwinger']['x'] = 2
    blue_team['leftwinger']['y'] =  10
    blue_team['rightdefenseman']['x'] = 5
    blue_team['rightdefenseman']['y'] =  11
    blue_team['leftdefenseman']['x'] = 3
    blue_team['leftdefenseman']['y'] = 11
    blue_team['goalie']['x'] = 4
    blue_team['goalie']['y'] =  18

    red_team['center']['x'] = 4
    red_team['center']['y'] = 9
    red_team['rightwinger']['x'] = 6
    red_team['rightwinger']['y'] =  9
    red_team['leftwinger']['x'] = 2
    red_team['leftwinger']['y'] =  9
    red_team['rightdefenseman']['x'] =5
    red_team['rightdefenseman']['y'] = 8
    red_team['leftdefenseman']['x'] = 3
    red_team['leftdefenseman']['y'] = 8
    red_team['goalie']['x'] = 4
    red_team['goalie']['y'] = 1

    if(turn == "blue"):
        for blue in blue_team:
            if(blue_team[blue]["icon"][-1] == "P"):
                blue_team[blue]["icon"] = blue_team[blue]["icon"][:-1]
        red_team["center"]["icon"] += "P"
    else:
        for red in red_team:
            if(red_team[red]["icon"][-1] == "P"):
                red_team[red]["icon"] = red_team[red]["icon"][:-1]
        blue_team["center"]["icon"] += "P"



def shoot(turn, player, player_stat):
    if(turn == "blue"):
        x = blue_team[player]['x']
        y = blue_team[player]['y']
        talent = stats[player_stat]["talent"]
        if ((x>2 and x<6) and (y<6 and y>1) or (((x<5 and y<6) and (x+y<6 and x+y>2)) or ((x>4 and y<6) and (x-y<6 and x-y>2) ) )):
            #straight on and can attempt a shot
            modifier = talent - 4
            if(random.randint(1, 6) - modifier >= 4):
                goals["blue_goal"] += 1
                players_reset(turn)
                clear()
                print_goal()
                time.sleep(3)
                print_rink(rink)
                return -2
            else:
                print_rink(rink)
                print("Shot Failed")
                return 1
        else:
            print("Can't shoot from this angle")
            return 0

    if(turn == "red"):
        x = red_team[player]['x']
        y = red_team[player]['y']
        talent = stats[player_stat]["talent"]
        y = abs(19-y)
        if ((x>2 and x<6) and (y<6 and y>1) or (((x<5 and y<6) and (x+y<6 and x+y>2)) or ((x>4 and y<6) and (x-y<6 and x-y>2) ) )):

            modifier = talent - 4
            if(random.randint(1, 6) - modifier >= 4):
                goals["red_goal"] += 1
                players_reset(turn)
                clear()
                print_goal()
                time.sleep(3)
                print_rink(rink)
                print("Shot Successful")
                return -2
            else:
                print_rink(rink)
                print("Shot Failed")
                return 1
        else:
            print("Can't shoot from this angle")
            return 0




def player_action(turn, player, action, player_stat):
    puck = False
    if(turn == "blue"):
        if(blue_team[player]["icon"][-1] == "P"):
            puck = True
    else:
        if(red_team[player]["icon"][-1] == "P"):
            puck = True

    if(puck == True and (action == "hit" or action == "poke" or action == "tap")):
        print("You have puck possession, so you cannot "+action+"\n")
        return 0
    if(puck == False and (action == "shoot" or action == "pass")):
        print("You don't have puck possession, so you cannot "+action+"\n")
        return 0

    if(action == "poke"):
        return poke(turn, player, player_stat)
    elif(action == "pass"):
        return puck_pass(turn, player, player_stat)
    elif(action == "hit"):
        return hit(turn, player, player_stat)
    elif(action == "tap"):
        return tap(turn, player, player_stat)
    elif(action == "shoot"):
        return shoot(turn, player, player_stat)
    else:
        print("Not sure how this happened")



def turn_start(turn):
    print_rink(rink)
    player = ""
    cprint("\n\n------------"+ turn.upper() +" TURN!-------------", turn, attrs=['blink'])
    while(player.lower() != "c" and player.lower() != "lw" and player.lower() != "rw" and player.lower() != "ld" and player.lower() != "rd" ):
        player = input("\nSelect a player to activate: C, RW, LW, RD, LD: ")
    specific_player = ""
    if(player.lower() == "rw" or player.lower() == "lw"):
        player_stat = "winger"
        if(player.lower() == "rw"):
            specific_player = "rightwinger"
        else:
            specific_player = "leftwinger"
    elif(player.lower() == "rd" or player.lower() == "ld"):
        player_stat = "defenseman"
        if(player.lower() == "rd"):
            specific_player = "rightdefenseman"
        else:
            specific_player = "leftdefenseman"
    elif(player.lower() == "c"):
        player_stat = "center"
        specific_player = "center"

    action = 0
    i = 0
    while i < (stats[player_stat]["speed"] + 1):
        print(stats[player_stat]["speed"]-i, "movement left")
        print(1-action, "action left\n")
        direction = input("Move or Action: ")
        direction = direction.lower()
        if((direction == "n" or direction == "s" or direction == "e" or direction == "w" or direction == "nw" or direction == "ne" or direction == "sw" or direction == "se") and i<stats[player_stat]["speed"] ):
            #i += move_player(turn, specific_player, direction)
            move_player(turn, specific_player, direction)
            print_rink(rink)
            i += 1
        elif((direction == "hit" or direction == "poke" or direction == "pass" or direction == "shoot" or direction == "tap") and action == 0):
            action = player_action(turn, specific_player, direction, player_stat)
        elif(direction == "stop"):
            move_team(turn, specific_player)
            break
        else:
            print("Invalid move, you probably moved too much")
        if(action < 0):
            break
        if(action > 0 and i == stats[player_stat]["speed"]):
            move_team(turn, specific_player)
            break


def main():
    while(True):
        help = print_menu()
        if(help.lower() == "h" or help.lower() == "help"):
            help_menu()
        else:
            break;

    while(True):
        turn_start("blue")
        turn_start("red")



if __name__ == '__main__':
    main()
