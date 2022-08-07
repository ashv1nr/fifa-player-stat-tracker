
from player import Player

class Defe(Player):

    def __init__(self, fname, lname, pos):
        if pos == "cb":
            super().__init__(fname, lname, "cb")
        else:
            super().__init__(fname, lname, "fb")
    
    def add_game(self, opp):
        print("Enter " + self._get_fullname() + "\'s stats v. " + opp)
        print()
        mr = input("match rating: ")
        mins = input("minutes played: ")
        if self._pos_abrv == "fb":
            asts = input("assists: ")
            expasts = input("expected asists: ")
        if self._pos_abrv == "cb":
            passatt = input("pass attempts: ")
            passcomp = input("passes completd: ")
        tackatt = input("tackle attempts: ")
        tackwon = input("tackles won: ")
        intcep = input("interceptions: ")
        if self._pos_abrv == "cb":
            blk = input("blocks: ")
            adw = input("aerial duels won: ")
        bbo = input("times beaten by opponent: ")
        cleshe = input("clean sheet?(\"1\" for yes, \"0\" for no) ")
        while cleshe != "1" and cleshe != "0":
            print("invalid input")
            cleshe = input("clean sheet?(\"1\" for yes, \"0\" for no) ")
        print()
        print("1) confirm stats")
        print("2) renter info")
        choice = int(input())
        print()
        if choice == 2:
            self.add_game(opp)
        else:
            if self._pos_abrv == "cb":
                self._print_game_to_file(opp, mins, mr, passatt, passcomp, tackatt, tackwon, intcep, blk, adw, bbo, cleshe)
            else:
                self._print_game_to_file(opp, mins, mr, asts, expasts, tackatt, tackwon, intcep, bbo, cleshe) 
    
    def calc_stats(self, nextmet):
        mins = 0
        mr = 0.0
        if self._pos_abrv == "fb":
            asts = 0
            expasts = 0.0
        if self._pos_abrv == "cb":
            passatt = 0
            passcomp = 0
        tackatt = 0
        tackwon = 0
        intcep = 0
        if self._pos_abrv == "cb":
            blk = 0
            adw = 0
        bbo = 0
        cleshe = 0
        temp = self._head
        while temp != None:
            mins = mins + temp.mins
            mr = mr + temp.mr
            if self._pos_abrv == "fb":
                asts = asts + temp.asts
                expasts = expasts + temp.expasts
            if self._pos_abrv == "cb":
                passatt = passatt + temp.passatt
                passcomp = passcomp + temp.passcomp
            tackatt = tackatt + temp.tackatt
            tackwon = tackwon + temp.tackwon
            intcep = intcep + temp.intcep
            if self._pos_abrv == "cb":
                blk = blk + temp.blk
                adw = adw + temp.adw
            bbo = bbo + temp.bbo
            cleshe = cleshe + temp.cleshe
            temp = temp.next
        if self._pos_abrv == "cb":
            if passatt == 0:
                passpct = 0.00
            else:
                passpct = round(((passcomp/passatt)*100), 2)
        if tackatt == 0:
            tackpct = 0.00
        else:
            tackpct = round(((tackwon/tackatt)*100), 2)
        if nextmet == "totals":
            if self._pos_abrv == "cb":
                self.__print_totals(mins, mr, passatt, passcomp, passpct, tackatt, tackwon, tackpct, intcep, blk, adw, bbo, cleshe)
            else:
                self.__print_totals(mins, mr, asts, expasts, tackatt, tackwon, tackpct, intcep, bbo, cleshe)
        elif nextmet == "avgs":
            games = mins/90.0
            mr = round((mr/self._ll_size),2)
            if self._pos_abrv == "fb":
                asts = round((asts/games),2)
                expasts = round((expasts/games),2)
            if self._pos_abrv == "cb":
                passatt = round((passatt/games),2)
                passcomp = round((passcomp/games),2)
            tackatt = round((tackatt/games),2)
            tackwon = round((tackwon/games),2)
            intcep = round((intcep/games),2)
            if self._pos_abrv == "cb":
                blk = round((blk/games),2)
                adw = round((adw/games),2)
            bbo = round((bbo/games),2)
            cleshe = round((cleshe/self._ll_size),2)
            if self._pos_abrv == "cb":
                if passatt == 0:
                    passpct = 0.00
                else:
                    passpct = round(((passcomp/passatt)*100), 2)
            if tackatt == 0:
                tackpct = 0.00
            else:
                tackpct = round(((tackwon/tackatt)*100), 2)
            if self._pos_abrv == "cb":
                self.__print_avgs(games, mr, passatt, passcomp, passpct, tackatt, tackwon, tackpct, intcep, blk, adw, bbo, cleshe)
            else:
                self.__print_avgs(games, mr, asts, expasts, tackatt, tackwon, tackpct, intcep, bbo, cleshe)
        else:
            pass
    
    def __print_avgs(self, a, b, c, d, e, f, g, h, i, j, k = -1, l = -1, m = -1):
        print(" over " + str(round(a,2)) + " games:")
        if self._pos_abrv == "cb":
            print("\tmatch rating: " + str(b) + "\n\tpass attempts: " + str(c) + "\n\tpasses completed: " + str(d) + "\n\tpass completion rate: " + str(e) + "%" + "\n\ttackle attempts: " + str(f) + "\n\ttackles won: " + str(g) + "\n\ttackle success rate: " + str(h) + "%" + "\n\tinterceptions: " + str(i) + "\n\tblocks: " + str(j) + "\n\taerial duels won: " + str(k) + "\n\ttimes beaten by opponent: " + str(l) + "\n\tclean sheets: " + str(m))
        else:
            print("\tmatch rating: " + str(b) + "\n\tassists: " + str(c) + "\n\texpected assists: " + str(d) + "\n\ttackle attempts: " + str(e) + "\n\ttackles won: " + str(f) + "\n\ttackle success rate: " + str(g) + "%" + "\n\tinterceptions: " + str(h) + "\n\ttimes beaten by opponent: " + str(i) + "\n\tclean sheets: " + str(j))
    
    def __print_totals(self, a, b, c, d, e, f, g, h, i, j, k = -1, l = -1, m = -1):   
        if self._pos_abrv == "cb":
            print("\tminutes: " + str(a) + "\n\tmatch ratings: " + str(round(b,2)) + "\n\tpass attempts: " + str(c) + "\n\tpasses completed: " + str(d) + "\n\tpass completion rate: " + str(e) + "%" + "\n\ttackle attempts: " + str(f) + "\n\ttackles won: " + str(g) + "\n\ttackle success rate: " + str(h) + "%" + "\n\tinterceptions: " + str(i) + "\n\tblocks: " + str(j) + "\n\taerial duels won: " + str(k) + "\n\ttimes beaten by opponent: " + str(l) + "\n\tclean sheets: " + str(m))
        else:
            print("\tminutes: " + str(a) + "\n\tmatch ratings: " + str(round(b,2)) + "\n\tassists: " + str(c) + "\n\texpected assists: " + str(d) + "\n\ttackle attempts: " + str(e) + "\n\ttackles won: " + str(f) + "\n\ttackle success rate: " + str(g) + "%" + "\n\tinterceptions: " + str(h) + "\n\ttimes beaten by opponent: " + str(i) + "\n\tclean sheets: " + str(j))