
from player import Player

class Mid(Player):
    
    def __init__(self, fname, lname, pos):
        if pos == "cdm":
            super().__init__(fname, lname, "cdm")
        elif pos == "cm":
            super().__init__(fname, lname, "cm")
        else:
            super().__init__(fname, lname, "cam")
            
    def add_game(self, opp):
        print("Enter " + self._get_fullname() + "\'s stats v. " + opp)
        print()
        mr = input("match rating: ")
        mins = input("minutes played: ")
        dribatt = input("dribble attempts: ")
        dribcomp = input("dribbles completed: ")
        if self._pos_abrv == "cm" or self._pos_abrv == "cam":
            oppbeat = input("opponents beaten: ")
            goals = input("goals: ")
            expgoals = input("expected goals: ")
        if self._pos_abrv == "cam":
            shotatt = input("shot attempts: ")
            sot = input("shots on target: ")
        if self._pos_abrv == "cm" or self._pos_abrv == "cam":
            asts = input("assists: ")
            expasts = input("expected asists: ")
        if self._pos_abrv == "cdm" or self._pos_abrv == "cm":
            passatt = input("pass attempts: ")
            passcomp = input("passes completed: ")
        tackatt = input("tackle attempts: ")
        tackwon = input("tackles won: ")
        if self._pos_abrv == "cdm" or self._pos_abrv == "cm":
            intcep = input("interceptions: ")
        if self._pos_abrv == "cdm":
            blk = input("blocks: ")
            adw = input("aerial duels won: ")
        if self._pos_abrv == "cdm" or self._pos_abrv == "cm":
            bbo = input("times beaten by opponent: ")
        if self._pos_abrv == "cdm":
            cleshe = input("clean sheet?(\"1\" for yes, \"0\" for no) ")
            while cleshe != "1" and cleshe != "0":
                print("invalid input")
                cleshe = input("clean sheet?(\"1\" for yes, \"2\" for no) ")
        print()
        print("1) confirm stats")
        print("2) renter info")
        choice = int(input())
        print()
        if choice == 2:
            self.add_game(opp)
        else:
            if self._pos_abrv == "cdm":
                self._print_game_to_file(opp, mins, mr, dribatt, dribcomp, passatt, passcomp, tackatt, tackwon, intcep, blk, adw, bbo, cleshe)
            elif self._pos_abrv == "cm":
                self._print_game_to_file(opp, mins, mr, dribatt, dribcomp, oppbeat, goals, expgoals, asts, expasts, passatt, passcomp, tackatt, tackwon, intcep, bbo)
            else:
                self._print_game_to_file(opp, mins, mr, dribatt, dribcomp, oppbeat, goals, expgoals, shotatt, sot, asts, expasts, tackatt, tackwon)
    
    def calc_stats(self, nextmet):
        mins = 0
        mr = 0.0
        dribatt = 0
        dribcomp = 0
        if self._pos_abrv == "cm" or self._pos_abrv == "cam":
            oppbeat = 0
            goals = 0
            expgoals = 0.0
        if self._pos_abrv == "cam":
            shotatt = 0
            sot = 0
        if self._pos_abrv == "cm" or self._pos_abrv == "cam":
            asts = 0
            expasts = 0.0
        if self._pos_abrv == "cdm" or self._pos_abrv == "cm":
            passatt = 0
            passcomp = 0
        tackatt = 0
        tackwon = 0
        if self._pos_abrv == "cdm" or self._pos_abrv == "cm":
            intcep = 0
        if self._pos_abrv == "cdm":
            blk = 0
            adw = 0
        if self._pos_abrv == "cdm" or self._pos_abrv == "cm":
            bbo = 0
        if self._pos_abrv == "cdm":
            cleshe = 0
        temp = self._head
        while temp != None:
            mins = mins + temp.mins
            mr = mr + temp.mr
            dribatt = dribatt + temp.dribatt
            dribcomp = dribcomp + temp.dribcomp
            if self._pos_abrv == "cm" or self._pos_abrv == "cam":
                oppbeat = oppbeat + temp.oppbeat
                goals = goals + temp.goals
                expgoals = expgoals + temp.expgoals
            if self._pos_abrv == "cam":
                shotatt = shotatt + temp.shotatt
                sot = sot + temp.sot
            if self._pos_abrv == "cm" or self._pos_abrv == "cam":
                asts = asts + temp.asts
                expasts = expasts + temp.expasts
            if self._pos_abrv == "cdm" or self._pos_abrv == "cm":
                passatt = passatt + temp.passatt
                passcomp = passcomp + temp.passcomp
            tackatt = tackatt + temp.tackatt
            tackwon = tackwon + temp.tackwon
            if self._pos_abrv == "cdm" or self._pos_abrv == "cm":
                intcep = intcep + temp.intcep
            if self._pos_abrv == "cdm":
                blk = blk + temp.blk
                adw = adw + temp.adw
            if self._pos_abrv == "cdm" or self._pos_abrv == "cm":
                bbo = bbo + temp.bbo
            if self._pos_abrv == "cdm":
                cleshe = cleshe + temp.cleshe
            temp = temp.next  
        if dribatt == 0:
            dribpct = 0.00
        else:
            dribpct = round(((dribcomp/dribatt)*100), 2)
        if self._pos_abrv == "cam":
            if shotatt == 0:
                shotpct = 0.00
            else:
                shotpct = round(((sot/shotatt)*100), 2)
        if self._pos_abrv == "cdm" or self._pos_abrv == "cm":
            if passatt == 0:
                passpct = 0.00
            else:
                passpct = round(((passcomp/passatt)*100), 2)
        if tackatt == 0:
            tackpct = 0.00
        else:
            tackpct = round(((tackwon/tackatt)*100), 2)
        if nextmet == "totals":
            if self._pos_abrv == "cdm":
                self.__print_totals(mins, mr, dribatt, dribcomp, dribpct, passatt, passcomp, passpct, tackatt, tackwon, tackpct, intcep, blk, adw, bbo, cleshe)
            elif self._pos_abrv == "cm":
                self.__print_totals(mins, mr, dribatt, dribcomp, dribpct, oppbeat, goals, expgoals, asts, expasts, passatt, passcomp, passpct, tackatt, tackwon, tackpct, intcep, bbo)
            else:
                self.__print_totals(mins, mr, dribatt, dribcomp, dribpct, oppbeat, goals, expgoals, shotatt, sot, shotpct, asts, expasts, tackatt, tackwon, tackpct)
        elif nextmet == "avgs":
            games = mins/90.0
            mr = round((mr/self._ll_size),2)
            dribatt = round((dribatt/games),2)
            dribcomp = round((dribcomp/games),2)
            if self._pos_abrv == "cm" or self._pos_abrv == "cam":
                oppbeat = round((oppbeat/games),2)
                goals = round((goals/games),2)
                expgoals = round((expgoals/games),2)
            if self._pos_abrv == "cam":
                shotatt = round((shotatt/games),2)
                sot = round((sot/games),2)
            if self._pos_abrv == "cm" or self._pos_abrv == "cam":
                asts = round((asts/games),2)
                expasts = round((expasts/games),2)
            if self._pos_abrv == "cdm" or self._pos_abrv == "cm":
                passatt = round((passatt/games),2)
                passcomp = round((passcomp/games),2)
            tackatt = round((tackatt/games),2)
            tackwon = round((tackwon/games),2)
            if self._pos_abrv == "cdm" or self._pos_abrv == "cm":
                intcep = round((intcep/games),2)
            if self._pos_abrv == "cdm":
                blk = round((blk/games),2)
                adw = round((adw/games),2)
            if self._pos_abrv == "cdm" or self._pos_abrv == "cm":
                bbo = round((bbo/games),2)
            if self._pos_abrv == "cdm":
                cleshe = round((cleshe/self._ll_size),2)
            if dribatt == 0:
                dribpct = 0.00
            else:
                dribpct = round(((dribcomp/dribatt)*100), 2)
            if self._pos_abrv == "cam":
                if shotatt == 0:
                    shotpct = 0.00
                else:
                    shotpct = round(((sot/shotatt)*100), 2)
            if self._pos_abrv == "cdm" or self._pos_abrv == "cm":
                if passatt == 0:
                    passpct = 0.00
                else:
                    passpct = round(((passcomp/passatt)*100), 2)
            if tackatt == 0:
                tackpct = 0.00
            else:
                tackpct = round(((tackwon/tackatt)*100), 2)
            if self._pos_abrv == "cdm":
                self.__print_avgs(games, mr, dribatt, dribcomp, dribpct, passatt, passcomp, passpct, tackatt, tackwon, tackpct, intcep, blk, adw, bbo, cleshe)
            elif self._pos_abrv == "cm":
                self.__print_avgs(games, mr, dribatt, dribcomp, dribpct, oppbeat, goals, expgoals, asts, expasts, passatt, passcomp, passpct, tackatt, tackwon, tackpct, intcep, bbo)
            else:
                self.__print_avgs(games, mr, dribatt, dribcomp, dribpct, oppbeat, goals, expgoals, shotatt, sot, shotpct, asts, expasts, tackatt, tackwon, tackpct)
        else:
            pass
    
    def __print_avgs(self, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q = -1, r = -1): 
        print(" over " + str(round(a,2)) + " games:") 
        if self._pos_abrv == "cdm":
            print("\tmatch rating: " + str(b) + "\n\tdribble attempts: " + str(c) + "\n\tdribbles completed: " + str(d) + "\n\tdribble success rate: " + str(e) + "%" + "\n\tpass attempts: " + str(f) + "\n\tpasses completed: " + str(g) + "\n\tpass completion rate: " + str(h) + "%" + "\n\ttackle attempts: " + str(i) + "\n\ttackles won: " + str(j) + "\n\ttackle success rate: " + str(k) + "%" + "\n\tinterceptions: " + str(l) + "\n\tblocks: " + str(m) + "\n\taerial duels won: " + str(n) + "\n\ttimes beaten by opponent: " + str(o) + "\n\tclean sheets: " + str(p))
        elif self._pos_abrv == "cm":
            print("\tmatch rating: " + str(b) + "\n\tdribble attempts: " + str(c) + "\n\tdribbles completed: " + str(d) + "\n\tdribble success rate: " + str(e) + "%" + "\n\topponents beat: " + str(f) + "\n\tgoals: " + str(g) + "\n\texpected goals: " + str(h) + "%" + "\n\tassists: " + str(i) + "\n\texpected assists: " + str(j) + "\n\tpass attempts: " + str(k) + "\n\tpasses completed: " + str(l) + "\n\tpass completion rate: " + str(m) + "%" + "\n\ttackle attempts: " + str(n) + "\n\ttackles won: " + str(o) + "\n\ttackle sucess rate: " + str(p) + "%" + "\n\tinterceptions: " + str(q) + "\n\ttimes beaten by opponent: " + str(r))
        else:
            print("\tmatch rating: " + str(b) + "\n\tdribble attempts: " + str(c) + "\n\tdribbles completed: " + str(d) + "\n\tdribble success rate: " + str(e) + "%" + "\n\topponents beat: " + str(f) + "\n\tgoals: " + str(g) + "\n\texpected goals: " + str(h) + "%" + "\n\tshot attempts: " + str(i) + "\n\tshots on target: " + str(j) + "\n\tshot accuracy: " + str(k) + "%" + "\n\tassists: " + str(l) + "\n\texpected assists: " + str(m) + "\n\ttackle attempts: " + str(n) + "\n\ttackles won: " + str(o) + "\n\ttackle sucess rate: " + str(p) + "%")
    
    def __print_totals(self, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q = -1, r = -1):  
        if self._pos_abrv == "cdm":
            print("\tminutes: " + str(a) + "\n\tmatch ratings: " + str(round(b,2)) + "\n\tdribble attempts: " + str(c) + "\n\tdribbles completed: " + str(d) + "\n\tdribble success rate: " + str(e) + "%" + "\n\tpass attempts: " + str(f) + "\n\tpasses completed: " + str(g) + "\n\tpass completion rate: " + str(h) + "%" + "\n\ttackle attempts: " + str(i) + "\n\ttackles won: " + str(j) + "\n\ttackle success rate: " + str(k) + "%" + "\n\tinterceptions: " + str(l) + "\n\tblocks: " + str(m) + "\n\taerial duels won: " + str(n) + "\n\ttimes beaten by opponent: " + str(o) + "\n\tclean sheets: " + str(p))
        elif self._pos_abrv == "cm":
            print("\tminutes: " + str(a) + "\n\tmatch ratings: " + str(round(b,2)) + "\n\tdribble attempts: " + str(c) + "\n\tdribbles completed: " + str(d) + "\n\tdribble success rate: " + str(e) + "%" + "\n\topponents beat: " + str(f) + "\n\tgoals: " + str(g) + "\n\texpected goals: " + str(h) + "%" + "\n\tassists: " + str(i) + "\n\texpected assists: " + str(j) + "\n\tpass attempts: " + str(k) + "\n\tpasses completed: " + str(l) + "\n\tpass completion rate: " + str(m) + "%" + "\n\ttackle attempts: " + str(n) + "\n\ttackles won: " + str(o) + "\n\ttackle sucess rate: " + str(p) + "%" + "\n\tinterceptions: " + str(q) + "\n\ttimes beaten by opponent: " + str(r))
        else:
            print("\tminutes: " + str(a) + "\n\tmatch ratings: " + str(round(b,2)) + "\n\tdribble attempts: " + str(c) + "\n\tdribbles completed: " + str(d) + "\n\tdribble success rate: " + str(e) + "%" + "\n\topponents beat: " + str(f) + "\n\tgoals: " + str(g) + "\n\texpected goals: " + str(h) + "%" + "\n\tshot attempts: " + str(i) + "\n\tshots on target: " + str(j) + "\n\tshot accuracy: " + str(k) + "%" + "\n\tassists: " + str(l) + "\n\texpected assists: " + str(m) + "\n\ttackle attempts: " + str(n) + "\n\ttackles won: " + str(o) + "\n\ttackle sucess rate: " + str(p) + "%")