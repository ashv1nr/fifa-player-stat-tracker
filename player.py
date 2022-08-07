
import os
from cbgame import CBGame
from fbgame import FBGame
from dmgame import DMGame
from cmgame import CMGame
from amgame import AMGame
from wigame import WIGame
from stgame import STGame

class Player:
    
    _db_size = 3
    _def_arr_size = 2
    _mid_arr_size = 3
    _att_arr_size = 2
    _def_ind = 0
    _mid_ind = 1
    _att_ind = 2
    _cb_ind = 0
    _fb_ind = 1
    _cdm_ind = 0
    _cm_ind = 1
    _cam_ind = 2
    _wing_ind = 0
    _st_ind = 1
    _db = [[[] for j in range(0)]for k in range(0)]
    
    def __init__(self, fname, lname, pos):
        self._fname = fname
        self._lname = lname
        if pos == "cb":
            Player._db[Player._def_ind][Player._cb_ind] = self.__sort_arr_by_lname(Player._db[Player._def_ind][Player._cb_ind])
            self._pos = "Centerback"
        elif pos == "fb":
            Player._db[Player._def_ind][Player._fb_ind] = self.__sort_arr_by_lname(Player._db[Player._def_ind][Player._fb_ind])
            self._pos = "Fullback"
        elif pos == "cdm":
            Player._db[Player._mid_ind][Player._cdm_ind] = self.__sort_arr_by_lname(Player._db[Player._mid_ind][Player._cdm_ind])
            self._pos = "Defensive Midfielder"
        elif pos == "cm":
            Player._db[Player._mid_ind][Player._cm_ind] = self.__sort_arr_by_lname(Player._db[Player._mid_ind][Player._cm_ind])
            self._pos = "Central Midfielder"
        elif pos == "cam":
            Player._db[Player._mid_ind][Player._cam_ind] = self.__sort_arr_by_lname(Player._db[Player._mid_ind][Player._cam_ind])
            self._pos = "Central Attacking Midfielder"
        elif pos == "wing":
            Player._db[Player._att_ind][Player._wing_ind] = self.__sort_arr_by_lname(Player._db[Player._att_ind][Player._wing_ind])
            self._pos = "Winger"
        else:
            Player._db[Player._att_ind][Player._st_ind] = self.__sort_arr_by_lname(Player._db[Player._att_ind][Player._st_ind])
            self._pos = "Striker"
        self._pos_abrv = pos
        self._head = None
        self._tail = None
        self._ll_size = 0
            
    @staticmethod
    def add_game():
        Player.print_db()
        opp = input("enter the opposing team: ")
        opp = Player._string_capitalizer_formatter(opp)
        ply_codes = input("enter the the three digit code of all players involved v. " + opp + " sepearted by \", \": ")
        ply_code_arr = ply_codes.split(", ")
        while len(ply_code_arr) < 11 or len(ply_code_arr) > 16:
            print("invalid number of players involved")
            ply_codes = input("enter the the three digit code of all players involved v. " + opp + " sepearted by \", \": ")
            ply_code_arr = ply_codes.split(", ")
        print()
        for i in ply_code_arr:
            z = int(i)%10
            y = int((int(i)/10))%10
            x = int(int((int(i)/10)/10))%10
            Player._db[x][y][z].add_game(opp)
    
    def __add_last(self, node):
        if self._head == None:
            self._head = node
            self._tail = node
        elif self._ll_size == 1:
            node.prev = self._head
            self._head.next = node
            self._tail = node
        else:
            node.prev = self._tail
            self._tail.next = node
            self._tail = node
        self._ll_size = self._ll_size + 1
    
    @staticmethod
    def create_db_arr():
        for s in range(Player._db_size):
            Player._db.append([])
        for d in range(Player._def_arr_size):
            Player._db[Player._def_ind].append([])
        for m in range(Player._mid_arr_size):
            Player._db[Player._mid_ind].append([])
        for a in range(Player._att_arr_size):
            Player._db[Player._att_ind].append([])
    
    def _get_fullname(self):
        if self._lname == "None":
            return self._fname
        return self._fname + ' ' + self._lname
    
    @staticmethod
    def __get_num2():
        print("Select the number of one of the below options:")
        print("\t1) minutes")
        print("\t2) match rating")
        print("\t3) dribble attempts")
        print("\t4) dribbles completed")
        print("\t5) dribble success rate")
        print("\t6) opponents beat")
        print("\t7) goals")
        print("\t8) expectd goals")
        print("\t9) shot attempts")
        print("\t10) shots on target")
        print("\t11) shot accuracy")
        print("\t12) assists")
        print("\t13) expected assists")
        print("\t14) pass attempts")
        print("\t15) passes completed")
        print("\t16) pass completion rate")
        print("\t17) tackle attempts")
        print("\t18) tackles wons")
        print("\t19) tackle success rate")
        print("\t20) interceptions")
        print("\t21) blocks")
        print("\t22) aerial duels won")
        print("\t23) times beaten by opponent")
        print("\t24) clean sheets")
        num2 = int(input())
        return num2
    
    @staticmethod
    def __get_ply_code_arr():
        Player.print_db()
        code = input("enter the the three digit code of a player: ")
        print()
        while len(code) != 3:
            print("invalid code")
            code = input("Enter the three digit code of the player: ")
        z = int(code)%10
        y = int((int(code)/10))%10
        x = int(int((int(code)/10)/10))%10
        print("\n")
        arr = [x, y, z]
        return arr
    
    def load_all_games(self, f):
        for fline in f:
            self.__load_one_game(fline, f)
        
    def __load_one_game(self, fline, f):
        i = len(fline)
        if fline[i-1:] == "\n":
            fline = fline[:i-1] 
        fline_arr = fline.split("-")
        if self._pos_abrv == "cb":
            cbg = CBGame(fline_arr[0], fline_arr[1] ,fline_arr[2], fline_arr[3], fline_arr[4], fline_arr[5], fline_arr[6] ,fline_arr[7], fline_arr[8], fline_arr[9], fline_arr[10], fline_arr[11])
            self.__add_last(cbg)
        elif self._pos_abrv == "fb":
            fbg = FBGame(fline_arr[0], fline_arr[1] ,fline_arr[2], fline_arr[3], fline_arr[4], fline_arr[5], fline_arr[6] ,fline_arr[7], fline_arr[8], fline_arr[9])
            self.__add_last(fbg) 
        elif self._pos_abrv == "cdm":
            dmg = DMGame(fline_arr[0], fline_arr[1] ,fline_arr[2], fline_arr[3], fline_arr[4], fline_arr[5], fline_arr[6] ,fline_arr[7], fline_arr[8], fline_arr[9], fline_arr[10], fline_arr[11], fline_arr[12], fline_arr[13])
            self.__add_last(dmg)
        elif self._pos_abrv == "cm":
            cmg = CMGame(fline_arr[0], fline_arr[1] ,fline_arr[2], fline_arr[3], fline_arr[4], fline_arr[5], fline_arr[6] ,fline_arr[7], fline_arr[8], fline_arr[9], fline_arr[10], fline_arr[11], fline_arr[12], fline_arr[13], fline_arr[14], fline_arr[15])
            self.__add_last(cmg)
        elif self._pos_abrv == "cam":
            amg = AMGame(fline_arr[0], fline_arr[1] ,fline_arr[2], fline_arr[3], fline_arr[4], fline_arr[5], fline_arr[6] ,fline_arr[7], fline_arr[8], fline_arr[9], fline_arr[10], fline_arr[11], fline_arr[12], fline_arr[13])
            self.__add_last(amg)
        elif self._pos_abrv == "wing":
            wig = WIGame(fline_arr[0], fline_arr[1] ,fline_arr[2], fline_arr[3], fline_arr[4], fline_arr[5], fline_arr[6] ,fline_arr[7], fline_arr[8], fline_arr[9], fline_arr[10], fline_arr[11])
            self.__add_last(wig)
        else:
            stg = STGame(fline_arr[0], fline_arr[1] ,fline_arr[2], fline_arr[3], fline_arr[4], fline_arr[5], fline_arr[6] ,fline_arr[7], fline_arr[8], fline_arr[9], fline_arr[10])
            self.__add_last(stg)
    
    @staticmethod
    def print_db():
        for i in range(len(Player._db)):
            for j in range(len(Player._db[i])):
                print(Player._db[i][j][0]._pos + "\'s:")
                for k in range(len(Player._db[i][j])):
                    print( str(i) + str(j) + str(k) + ") " + Player._db[i][j][k]._get_fullname())
                print()
    
    def __print_games_stats(self):
        temp = self._head
        s = ""
        while temp != None:
            s = s + temp.to_string() + "\n"
            temp = temp.next
        print(s)
    
    def _print_game_to_file(self, a, b, c, d, e, f, g, h, i, j, k = "-1", l = "-1", m = "-1", n = "-1", o = "-1", p = "-1"):
        s = "\n" + a + "-" + b + "-" + c + "-" + d + "-" + e + "-" + f + "-" + g + "-" + h + "-" + i + "-" + j
        if k != "-1":
            s = s + "-" + k
        if l != "-1":
            s = s + "-" + l
        if m != "-1":
            s = s + "-" + m
        if n != "-1":
            s = s + "-" + n
        if o != "-1":
            s = s + "-" + o
        if p != "-1":
            s = s + "-" + p
        with open('players/' + self._get_fullname() + '.txt', 'a') as f:
            f.write(s)
            self.__load_one_game(s, f)
        
    @staticmethod
    def __print_sort_arr(arr1, arr2, s1, s2, p = -1):
        parr = []
        xarr = []
        while len(arr1) != 0:
            x = arr1[0]
            y = arr2[0]
            del arr1[0]
            del arr2[0]
            if len(xarr) == 0:
                xarr.append(x)
                parr.append(y)
            elif x < xarr[len(xarr)-1]:
                xarr.append(x)
                parr.append(y)
            else:
                for i in range(len(xarr)):
                    if x >= xarr[i]:
                        xarr.insert(i, x)
                        parr.insert(i, y)
                        break   
                    else:
                        continue
        print("Team leaders in " + s1 + " " + s2 )
        for i in range(len(parr)):
            if p == -1:
                print("\t" + parr[i]._get_fullname() + ": " + str(xarr[i]))
            else:
                print("\t" + parr[i]._get_fullname() + ": " + str(xarr[i]) + p)
        print("\n")
    
    @staticmethod
    def remove_player():
        Player.print_db()
        code = input("Enter the three digit code of the player you want to remove from the databse: ")
        while len(code) != 3:
            print("invalid code")
            code = input("Enter the three digit code of the player you want to remove from the databse: ")
        z = int(code)%10
        y = int((int(code)/10))%10
        x = int(int((int(code)/10)/10))%10
        print("1) confirm deletion of " + Player._db[x][y][z]._get_fullname() + "\'s complete statistcal record")
        print("2) cancel deletion")
        n = int(input())
        print()
        if n == 1:
            os.remove('players/' + Player._db[x][y][z]._get_fullname() + '.txt')
            del Player._db[x][y][z]
    
    @staticmethod
    def show_ply_opts():
        run = True
        while run == True:
            print("Select the number of one of the below options:")
            print("\t1) view a players totals on the season")
            print("\t2) view a player's per 90 averages on the season")
            print("\t3) view a player's stats from every game")
            print("\t4) view team leaders for statistcal categories")
            print("\t5) back to main menu")
            choice = int(input())
            print()
            if choice == 1:
                Player.__view_szn_totals()
            elif choice == 2:
                Player.__view_szn_avgs()
            elif choice == 3:
                Player.__view_each_games_stats()
            elif choice == 4:
                Player.__view_stat_leaders()
            else:
                run = False
    
    def __sort_arr_by_lname(self, arr):
        if len(arr) > 0:
            for i in range(len(arr)):
                if self._lname == "None" and arr[i]._lname == "None":
                    if self._fname < arr[i]._fname:
                        arr.insert(i, self)
                        return arr
                elif self._lname == "None":
                    if self._fname < arr[i]._lname:
                        arr.insert(i, self)
                        return arr
                elif arr[i]._lname == "None":
                    if self._lname < arr[i]._fname:
                        arr.insert(i, self)
                        return arr
                else:
                    if self._lname < arr[i]._lname:
                        arr.insert(i, self)
                        return arr
            arr.insert(len(arr), self)
            return arr
        else:
            arr.append(self)
            return arr
    
    @staticmethod
    def _string_capitalizer_formatter(s):
        s = s.casefold()
        s = s[0:1].upper() + s[1:]
        for i in range(len(s)):
            if s[i:i+1] == " ":
                s = s[0:i+1] + s[i+1:i+2].upper() + s[i+2:]
        return s
        
    @staticmethod
    def __view_each_games_stats():
        codearr = Player.__get_ply_code_arr()
        print(Player._db[codearr[0]][codearr[1]][codearr[2]]._get_fullname() + "\'s stats from every game\n")
        Player._db[codearr[0]][codearr[1]][codearr[2]].__print_games_stats()
    
    @staticmethod
    def __view_stat_leaders():
        num2 = Player.__get_num2()
        while num2 < 1 or num2 > 24:
            print("invalid input")
            num2 = Player.__get_num2()
        num1 = int(input("Select \"1\" for season leaders or \"2\" for per 90 leaders: "))
        while num1 != 1 and num1 != 2:
            print("invalid input")
            num1 = int(input("Select \"1\" for season leaders or \"2\" for per 90 leaders: "))
        if num1 == 1:
            s = "on the season"
        else:
            s = "per 90"
        print("\n")
        if num2 == 1:
            Player.__print_mn_leaders()
        if num2 == 2:
            Player.__print_mr_leaders(s)
        if num2 == 3:
            Player.__print_da_leaders(s)
        if num2 == 4:
            Player.__print_dc_leaders(s)
        if num2 == 5:
            Player.__print_dsr_leaders(s)
        if num2 == 6:
            Player.__print_ob_leaders(s)
        if num2 == 7:
            Player.__print_g_leaders(s)
        if num2 == 8:
            Player.__print_xg_leaders(s)
        if num2 == 9:
            Player.__print_sa_leaders(s)
        if num2 == 10:
            Player.__print_sot_leaders(s)
        if num2 == 11:
            Player.__print_shacc_leaders(s)
        if num2 == 12:
            Player.__print_a_leaders(s)
        if num2 == 13:
            Player.__print_xa_leaders(s)
        if num2 == 14:
            Player.__print_pa_leaders(s)
        if num2 == 15:
            Player.__print_pc_leaders(s)
        if num2 == 16:
            Player.__print_pcr_leaders(s)
        if num2 == 17:
            Player.__print_ta_leaders(s)
        if num2 == 18:
            Player.__print_tw_leaders(s)
        if num2 == 19:
            Player.__print_tsr_leaders(s)
        if num2 == 20:
            Player.__print_int_leaders(s)
        if num2 == 21:
            Player.__print_blk_leaders(s)
        if num2 == 22:
            Player.__print_adw_leaders(s)
        if num2 == 23:
            Player.__print_bbo_leaders(s)
        if num2 == 24:
            Player.__print_cs_leaders(s)
    
    @staticmethod
    def __view_szn_avgs():
        codearr = Player.__get_ply_code_arr()
        print(Player._db[codearr[0]][codearr[1]][codearr[2]]._get_fullname() + "\'s per 90 averages on the season", end='')
        if Player._db[codearr[0]][codearr[1]][codearr[2]]._ll_size > 0:
            Player._db[codearr[0]][codearr[1]][codearr[2]].calc_stats("avgs")
        print()
    
    @staticmethod
    def __view_szn_totals():
        codearr = Player.__get_ply_code_arr()
        print(Player._db[codearr[0]][codearr[1]][codearr[2]]._get_fullname() + "\'s totals on the season:")
        if Player._db[codearr[0]][codearr[1]][codearr[2]]._ll_size > 0:
            Player._db[codearr[0]][codearr[1]][codearr[2]].calc_stats("totals")
        print()
        
    @staticmethod
    def __print_mn_leaders():
        xarr = []
        parr = []
        for i in range(len(Player._db)):
            for j in range(len(Player._db[i])):
                for k in range(len(Player._db[i][j])):
                    x = 0
                    temp = Player._db[i][j][k]._head
                    while temp != None:
                        x = x + temp.mins
                        temp = temp.next
                    xarr.append(x)
                    parr.append(Player._db[i][j][k])
        Player.__print_sort_arr(xarr, parr, "minutes", "on the season")
        
    @staticmethod
    def __print_mr_leaders(s):
        xarr = []
        parr = []
        for i in range(len(Player._db)):
            for j in range(len(Player._db[i])):
                for k in range(len(Player._db[i][j])):
                    x = 0
                    temp = Player._db[i][j][k]._head
                    while temp != None:
                        x = x + temp.mr
                        temp = temp.next
                    if s == "on the season":
                        x = round(x,2)
                    else:
                        if Player._db[i][j][k]._ll_size == 0:
                            x = -1
                        else:
                            x = round((x/Player._db[i][j][k]._ll_size),2)
                    xarr.append(x)
                    parr.append(Player._db[i][j][k])            
        Player.__print_sort_arr(xarr, parr, "match ratings", s)
        
    @staticmethod
    def __print_da_leaders(s):
        xarr = []
        parr = []
        for i in range(Player._mid_ind, len(Player._db)):
            for j in range(len(Player._db[i])):
                for k in range(len(Player._db[i][j])):
                    x = 0
                    y = 0
                    temp = Player._db[i][j][k]._head
                    while temp != None:
                        x = x + temp.dribatt
                        y = y + temp.mins
                        temp = temp.next
                    if s == "per 90":
                        if Player._db[i][j][k]._ll_size == 0:
                            x = -1
                        else:
                            games = y/90.0
                            x = round((x/games),2)
                    xarr.append(x)
                    parr.append(Player._db[i][j][k])
        Player.__print_sort_arr(xarr, parr, "dribble attempts", s)
    
    @staticmethod
    def __print_dc_leaders(s):
        xarr = []
        parr = []
        for i in range(Player._mid_ind, len(Player._db)):
            for j in range(len(Player._db[i])):
                for k in range(len(Player._db[i][j])):
                    x = 0
                    y = 0
                    temp = Player._db[i][j][k]._head
                    while temp != None:
                        x = x + temp.dribcomp
                        y = y + temp.mins
                        temp = temp.next
                    if s == "per 90":
                        if Player._db[i][j][k]._ll_size == 0:
                            x = -1
                        else:
                            games = y/90.0
                            x = round((x/games),2)
                    xarr.append(x)
                    parr.append(Player._db[i][j][k])
        Player.__print_sort_arr(xarr, parr, "dribbles completed", s)
        
    @staticmethod
    def __print_dsr_leaders(s):
        xarr = []
        parr = []
        for i in range(Player._mid_ind, len(Player._db)):
            for j in range(len(Player._db[i])):
                for k in range(len(Player._db[i][j])):
                    x = 0
                    y = 0
                    m = 0
                    temp = Player._db[i][j][k]._head
                    while temp != None:
                        x = x + temp.dribatt
                        y = y + temp.dribcomp
                        m = m + temp.mins
                        temp = temp.next
                    if s == "per 90":
                        if Player._db[i][j][k]._ll_size == 0:
                            x = -1
                        else:
                            games = m/90.0
                            x = round((x/games),2)
                            y = round((y/games),2)
                    if x == 0:
                        z = 0.00
                    elif x == -1:
                        z = -1
                    else:
                        z = round(((y/x)*100), 2)
                    xarr.append(z)
                    parr.append(Player._db[i][j][k])
        Player.__print_sort_arr(xarr, parr, "dribble success rate", s, "%")
           
    @staticmethod
    def __print_ob_leaders(s):
        xarr = []
        parr = []
        for i in range(Player._mid_ind, len(Player._db)):
            for j in range(len(Player._db[i])):
                for k in range(len(Player._db[i][j])):
                    if Player._db[i][j][k]._pos_abrv != "cdm" and Player._db[i][j][k]._pos_abrv != "st":
                        x = 0
                        y = 0
                        temp = Player._db[i][j][k]._head
                        while temp != None:
                            x = x + temp.oppbeat
                            y = y + temp.mins
                            temp = temp.next
                        if s == "per 90":
                            if Player._db[i][j][k]._ll_size == 0:
                                x = -1
                            else:
                                games = y/90.0
                                x = round((x/games),2)
                        xarr.append(x)
                        parr.append(Player._db[i][j][k])
        Player.__print_sort_arr(xarr, parr, "opponents beat", s)
        
    @staticmethod
    def __print_g_leaders(s):
        xarr = []
        parr = []
        for i in range(Player._mid_ind, len(Player._db)):
            for j in range(len(Player._db[i])):
                for k in range(len(Player._db[i][j])):
                    if Player._db[i][j][k]._pos_abrv != "cdm":
                        x = 0
                        y = 0
                        temp = Player._db[i][j][k]._head
                        while temp != None:
                            x = x + temp.goals
                            y = y + temp.mins
                            temp = temp.next
                        if s == "per 90":
                            if Player._db[i][j][k]._ll_size == 0:
                                x = -1
                            else:
                                games = y/90.0
                                x = round((x/games),2)
                        xarr.append(x)
                        parr.append(Player._db[i][j][k])
        Player.__print_sort_arr(xarr, parr, "goals", s)
        
    @staticmethod
    def __print_xg_leaders(s):
        xarr = []
        parr = []
        for i in range(Player._mid_ind, len(Player._db)):
            for j in range(len(Player._db[i])):
                for k in range(len(Player._db[i][j])):
                    if Player._db[i][j][k]._pos_abrv != "cdm":
                        x = 0
                        y = 0
                        temp = Player._db[i][j][k]._head
                        while temp != None:
                            x = x + temp.expgoals
                            y = y + temp.mins
                            temp = temp.next
                        if s == "per 90":
                            if Player._db[i][j][k]._ll_size == 0:
                                x = -1
                            else:
                                games = y/90.0
                                x = round((x/games),2)
                        xarr.append(x)
                        parr.append(Player._db[i][j][k])
        Player.__print_sort_arr(xarr, parr, "expected goals", s)
        
    @staticmethod
    def __print_sa_leaders(s):
        xarr = []
        parr = []
        for i in range(Player._mid_ind, len(Player._db)):
            for j in range(len(Player._db[i])):
                for k in range(len(Player._db[i][j])):
                    if Player._db[i][j][k]._pos_abrv != "cdm" and Player._db[i][j][k]._pos_abrv != "cm":
                        x = 0
                        y = 0
                        temp = Player._db[i][j][k]._head
                        while temp != None:
                            x = x + temp.shotatt
                            y = y + temp.mins
                            temp = temp.next
                        if s == "per 90":
                            if Player._db[i][j][k]._ll_size == 0:
                                x = -1
                            else:
                                games = y/90.0
                                x = round((x/games),2)
                        xarr.append(x)
                        parr.append(Player._db[i][j][k])
        Player.__print_sort_arr(xarr, parr, "shot attempts", s)
        
    @staticmethod
    def __print_sot_leaders(s):
        xarr = []
        parr = []
        for i in range(Player._mid_ind, len(Player._db)):
            for j in range(len(Player._db[i])):
                for k in range(len(Player._db[i][j])):
                    if Player._db[i][j][k]._pos_abrv != "cdm" and Player._db[i][j][k]._pos_abrv != "cm":
                        x = 0
                        y = 0
                        temp = Player._db[i][j][k]._head
                        while temp != None:
                            x = x + temp.sot
                            y = y + temp.mins
                            temp = temp.next
                        if s == "per 90":
                            if Player._db[i][j][k]._ll_size == 0:
                                x = -1
                            else:
                                games = y/90.0
                                x = round((x/games),2)
                        xarr.append(x)
                        parr.append(Player._db[i][j][k])
        Player.__print_sort_arr(xarr, parr, "shots on target", s)
        
    @staticmethod
    def __print_shacc_leaders(s):
        xarr = []
        parr = []
        for i in range(Player._mid_ind, len(Player._db)):
            for j in range(len(Player._db[i])):
                for k in range(len(Player._db[i][j])):
                    if Player._db[i][j][k]._pos_abrv != "cdm" and Player._db[i][j][k]._pos_abrv != "cm":
                        x = 0
                        y = 0
                        m = 0
                        temp = Player._db[i][j][k]._head
                        while temp != None:
                            x = x + temp.shotatt
                            y = y + temp.sot
                            m = m + temp.mins
                            temp = temp.next
                        if s == "per 90":
                            if Player._db[i][j][k]._ll_size == 0:
                                x = -1
                            else:
                                games = m/90.0
                                x = round((x/games),2)
                                y = round((y/games),2)
                        if x == 0:
                            z = 0.00
                        elif x == -1:
                            z = -1
                        else:
                            z = round(((y/x)*100), 2)
                        xarr.append(z)
                        parr.append(Player._db[i][j][k])
        Player.__print_sort_arr(xarr, parr, "shot accuracy", s, "%")
        
    @staticmethod
    def __print_a_leaders(s):
        xarr = []
        parr = []
        for i in range(len(Player._db)):
            for j in range(len(Player._db[i])):
                for k in range(len(Player._db[i][j])):
                    if Player._db[i][j][k]._pos_abrv != "cb" and Player._db[i][j][k]._pos_abrv != "cdm" and Player._db[i][j][k]._pos_abrv != "st" :
                        x = 0
                        y = 0
                        temp = Player._db[i][j][k]._head
                        while temp != None:
                            x = x + temp.asts
                            y = y + temp.mins
                            temp = temp.next
                        if s == "per 90":
                            if Player._db[i][j][k]._ll_size == 0:
                                x = -1
                            else:
                                games = y/90.0
                                x = round((x/games),2)
                        xarr.append(x)
                        parr.append(Player._db[i][j][k])
        Player.__print_sort_arr(xarr, parr, "assists", s)
        
    @staticmethod
    def __print_xa_leaders(s):
        xarr = []
        parr = []
        for i in range(len(Player._db)):
            for j in range(len(Player._db[i])):
                for k in range(len(Player._db[i][j])):
                    if Player._db[i][j][k]._pos_abrv != "cb" and Player._db[i][j][k]._pos_abrv != "cdm" and Player._db[i][j][k]._pos_abrv != "st" :
                        x = 0
                        y = 0
                        temp = Player._db[i][j][k]._head
                        while temp != None:
                            x = x + temp.expasts
                            y = y + temp.mins
                            temp = temp.next
                        if s == "per 90":
                            if Player._db[i][j][k]._ll_size == 0:
                                x = -1
                            else:
                                games = y/90.0
                                x = round((x/games),2)
                        xarr.append(x)
                        parr.append(Player._db[i][j][k])
        Player.__print_sort_arr(xarr, parr, "expected assists", s)
        
    @staticmethod
    def __print_pa_leaders(s):
        xarr = []
        parr = []
        for i in range(len(Player._db)):
            for j in range(len(Player._db[i])):
                for k in range(len(Player._db[i][j])):
                    if Player._db[i][j][k]._pos_abrv != "fb" and Player._db[i][j][k]._pos_abrv != "cam" and Player._db[i][j][k]._pos_abrv != "wing" :
                        x = 0
                        y = 0
                        temp = Player._db[i][j][k]._head
                        while temp != None:
                            x = x + temp.passatt
                            y = y + temp.mins
                            temp = temp.next
                        if s == "per 90":
                            if Player._db[i][j][k]._ll_size == 0:
                                x = -1
                            else:
                                games = y/90.0
                                x = round((x/games),2)
                        xarr.append(x)
                        parr.append(Player._db[i][j][k])
        Player.__print_sort_arr(xarr, parr, "pass attempts", s)
        
    @staticmethod
    def __print_pc_leaders(s):
        xarr = []
        parr = []
        for i in range(len(Player._db)):
            for j in range(len(Player._db[i])):
                for k in range(len(Player._db[i][j])):
                    if Player._db[i][j][k]._pos_abrv != "fb" and Player._db[i][j][k]._pos_abrv != "cam" and Player._db[i][j][k]._pos_abrv != "wing" :
                        x = 0
                        y = 0
                        temp = Player._db[i][j][k]._head
                        while temp != None:
                            x = x + temp.passcomp
                            y = y + temp.mins
                            temp = temp.next
                        if s == "per 90":
                            if Player._db[i][j][k]._ll_size == 0:
                                x = -1
                            else:
                                games = y/90.0
                                x = round((x/games),2)
                        xarr.append(x)
                        parr.append(Player._db[i][j][k])
        Player.__print_sort_arr(xarr, parr, "passess completed", s)
        
    @staticmethod
    def __print_pcr_leaders(s):
        xarr = []
        parr = []
        for i in range(len(Player._db)):
            for j in range(len(Player._db[i])):
                for k in range(len(Player._db[i][j])):
                    if Player._db[i][j][k]._pos_abrv != "fb" and Player._db[i][j][k]._pos_abrv != "cam" and Player._db[i][j][k]._pos_abrv != "wing" :
                        x = 0
                        y = 0
                        m = 0
                        temp = Player._db[i][j][k]._head
                        while temp != None:
                            x = x + temp.passatt
                            y = y + temp.passcomp
                            m = m + temp.mins
                            temp = temp.next
                        if s == "per 90":
                            if Player._db[i][j][k]._ll_size == 0:
                                x = -1
                            else:
                                games = m/90.0
                                x = round((x/games),2)
                                y = round((y/games),2)
                        if x == 0:
                            z = 0.00
                        elif x == -1:
                            z == -1
                        else:
                            z = round(((y/x)*100), 2)
                            xarr.append(z)
                            parr.append(Player._db[i][j][k])
        Player.__print_sort_arr(xarr, parr, "pass completion rate", s, "%")
        
    @staticmethod
    def __print_ta_leaders(s):
        xarr = []
        parr = []
        for i in range(Player._att_ind):
            for j in range(len(Player._db[i])):
                for k in range(len(Player._db[i][j])):
                    x = 0
                    y = 0
                    temp = Player._db[i][j][k]._head
                    while temp != None:
                        x = x + temp.tackatt
                        y = y + temp.mins
                        temp = temp.next
                    if s == "per 90":
                        if Player._db[i][j][k]._ll_size == 0:
                            x = -1
                        else:
                            games = y/90.0
                            x = round((x/games),2)
                    xarr.append(x)
                    parr.append(Player._db[i][j][k])
        Player.__print_sort_arr(xarr, parr, "tackle attempts", s)
        
    @staticmethod
    def __print_tw_leaders(s):
        xarr = []
        parr = []
        for i in range(Player._att_ind):
            for j in range(len(Player._db[i])):
                for k in range(len(Player._db[i][j])):
                    x = 0
                    y = 0
                    temp = Player._db[i][j][k]._head
                    while temp != None:
                        x = x + temp.tackwon
                        y = y + temp.mins
                        temp = temp.next
                    if s == "per 90":
                        if Player._db[i][j][k]._ll_size == 0:
                            x = -1
                        else:
                            games = y/90.0
                            x = round((x/games),2)
                    xarr.append(x)
                    parr.append(Player._db[i][j][k])
        Player.__print_sort_arr(xarr, parr, "tackles won", s)
        
    @staticmethod
    def __print_tsr_leaders(s):
        xarr = []
        parr = []
        for i in range(Player._att_ind):
            for j in range(len(Player._db[i])):
                for k in range(len(Player._db[i][j])):
                    x = 0
                    y = 0
                    m = 0
                    temp = Player._db[i][j][k]._head
                    while temp != None:
                        x = x + temp.tackatt
                        y = y + temp.tackwon
                        m = m + temp.mins
                        temp = temp.next
                    if s == "per 90":
                        if Player._db[i][j][k]._ll_size == 0:
                            x = -1
                        else:
                            games = m/90.0
                            x = round((x/games),2)
                            y = round((y/games),2)
                    if x == 0:
                        z = 0.00
                    elif x == -1:
                        z = -1
                    else:
                        z = round(((y/x)*100), 2)
                    xarr.append(z)
                    parr.append(Player._db[i][j][k])
        Player.__print_sort_arr(xarr, parr, "tackle success rate", s, "%")
    
    @staticmethod
    def __print_int_leaders(s):
        xarr = []
        parr = []
        for i in range(Player._att_ind):
            for j in range(len(Player._db[i])):
                for k in range(len(Player._db[i][j])):
                    if Player._db[i][j][k]._pos_abrv != "cam":
                        x = 0
                        y = 0
                        temp = Player._db[i][j][k]._head
                        while temp != None:
                            x = x + temp.intcep
                            y = y + temp.mins
                            temp = temp.next
                        if s == "per 90":
                            if Player._db[i][j][k]._ll_size == 0:
                                x = -1
                            else:
                                games = y/90.0
                                x = round((x/games),2)
                        xarr.append(x)
                        parr.append(Player._db[i][j][k])
        Player.__print_sort_arr(xarr, parr, "interceptions", s)  
        
    @staticmethod
    def __print_blk_leaders(s):
        xarr = []
        parr = []
        for i in range(Player._att_ind):
            for j in range(len(Player._db[i])):
                for k in range(len(Player._db[i][j])):
                    if Player._db[i][j][k]._pos_abrv != "fb" and Player._db[i][j][k]._pos_abrv != "cm" and Player._db[i][j][k]._pos_abrv != "cam":
                        x = 0
                        y = 0
                        temp = Player._db[i][j][k]._head
                        while temp != None:
                            x = x + temp.blk
                            y = y + temp.mins
                            temp = temp.next
                        if s == "per 90":
                            if Player._db[i][j][k]._ll_size == 0:
                                x = -1
                            else:
                                games = y/90.0
                                x = round((x/games),2)
                        xarr.append(x)
                        parr.append(Player._db[i][j][k])
        Player.__print_sort_arr(xarr, parr, "blocks", s)
        
    @staticmethod
    def __print_adw_leaders(s):
        xarr = []
        parr = []
        for i in range(Player._att_ind):
            for j in range(len(Player._db[i])):
                for k in range(len(Player._db[i][j])):
                    if Player._db[i][j][k]._pos_abrv != "fb" and Player._db[i][j][k]._pos_abrv != "cm" and Player._db[i][j][k]._pos_abrv != "cam":
                        x = 0
                        y = 0
                        temp = Player._db[i][j][k]._head
                        while temp != None:
                            x = x + temp.adw
                            y = y + temp.mins
                            temp = temp.next
                        if s == "per 90":
                            if Player._db[i][j][k]._ll_size == 0:
                                x = -1
                            else:
                                games = y/90.0
                                x = round((x/games),2)
                        xarr.append(x)
                        parr.append(Player._db[i][j][k])
        Player.__print_sort_arr(xarr, parr, "aerial duels won", s)
        
    @staticmethod
    def __print_bbo_leaders(s):
        xarr = []
        parr = []
        for i in range(Player._att_ind):
            for j in range(len(Player._db[i])):
                for k in range(len(Player._db[i][j])):
                    if Player._db[i][j][k]._pos_abrv != "cam":
                        x = 0
                        y = 0
                        temp = Player._db[i][j][k]._head
                        while temp != None:
                            x = x + temp.bbo
                            y = y + temp.mins
                            temp = temp.next
                        if s == "per 90":
                            if Player._db[i][j][k]._ll_size == 0:
                                x = -1
                            else:
                                games = y/90.0
                                x = round((x/games),2)
                        xarr.append(x)
                        parr.append(Player._db[i][j][k])
        Player.__print_sort_arr(xarr, parr, "times beaten by opponent", s)
           
    @staticmethod
    def __print_cs_leaders(s):
        xarr = []
        parr = []
        for i in range(Player._att_ind):
            for j in range(len(Player._db[i])):
                for k in range(len(Player._db[i][j])):
                    if Player._db[i][j][k]._pos_abrv != "cm" and Player._db[i][j][k]._pos_abrv != "cam":
                        x = 0
                        temp = Player._db[i][j][k]._head
                        while temp != None:
                            x = x + temp.cleshe
                            temp = temp.next
                        if s == "per 90":
                            if Player._db[i][j][k]._ll_size == 0:
                                x = -1
                            else:
                                x = round((x/Player._db[i][j][k]._ll_size),2)
                        xarr.append(x)
                        parr.append(Player._db[i][j][k])
        Player.__print_sort_arr(xarr, parr, "clean sheets", s)