
import os
from player import Player
from defe import Defe
from mid import Mid
from att import Att

class Main:
    
    @staticmethod
    def menu():
        Main.__load_full_db()
        run = True
        while run == True:
            print("Select the number of one of the below options:")
            print("\t1) add a new player to the datbase")
            print("\t2) delete a player from the database")
            print("\t3) add a new game for the team")
            print("\t4) view player stats")
            print("\t5) view players in the database")
            print("\t6) quit program")
            choice = int(input())
            print()
            if choice == 1:
                Main.__add_player()
            elif choice == 2:
                Player.remove_player()
            elif choice == 3:
                Player.add_game()
            elif choice == 4:
                Player.show_ply_opts()
            elif choice == 5:
                Player.print_db()
            else:
                run = False
    
    @staticmethod
    def __add_player():
        name = input("enter the player's name: ")
        n = -1
        name = name.casefold()
        name = name[0:1].upper() + name[1:]
        for i in range(len(name)):
            if name[i:i+1] == " ":
                if n == -1:
                    n = i
                name = name[0:i+1] + name[i+1:i+2].upper() + name[i+2:]
        pos = input("enter " + name + "\'s position: (cb, fb, cdm, cm, cam, wing, st): ")
        while pos != "cb" and pos != "fb" and pos != "cdm" and pos != "cm" and pos != "cam" and pos != "wing" and pos != "st":
            print("invalid position")
            pos = input("enter the player's position(cb, fb, cdm, cm, cam, wing, st): ")
        if n == -1:
            with open('players/' + name + '.txt', 'x') as f:
                f.write(name + "-None" + "-" + pos)
        else:
            with open('players/' + name + '.txt', 'x') as f:
                f.write(name[0:n] + "-" + name[n+1:] + "-" + pos)
        with open('players/' + name + '.txt', 'r') as f:
            Main.__upload_player_to_db(f)
        print()
    
    @staticmethod        
    def __print_player_files():
        for file in os.listdir("players"):
            with open(f"players/{file}", 'r') as f:
                print(f.read())
    
    @staticmethod
    def __load_full_db():
        Player.create_db_arr()
        fline = ""
        for file in os.listdir("players"):
            with open(f"players/{file}", 'r') as f:
                Main.__upload_player_to_db(f)
    
    @staticmethod
    def __upload_player_to_db(f):
        fline = f.readline()
        i = len(fline)
        if fline[i-1:] == "\n":
            fline = fline[:i-1] 
        fline_arr = fline.split("-")
        if fline_arr[2] == "cb" or fline_arr[2] == "fb":
            d = Defe(fline_arr[0], fline_arr[1] ,fline_arr[2])
            d.load_all_games(f)
        elif fline_arr[2] == "cdm" or fline_arr[2] == "cm" or fline_arr[2] == "cam":
            m = Mid(fline_arr[0], fline_arr[1], fline_arr[2])
            m.load_all_games(f)
        else:
            a = Att(fline_arr[0], fline_arr[1], fline_arr[2])
            a.load_all_games(f)
            
if __name__ == "__main__":
    Main.menu() 