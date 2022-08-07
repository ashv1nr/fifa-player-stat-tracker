
from player import Player

class Att(Player):

    def __init__(self, fname, lname, pos):
        if pos == "wing":
            super().__init__(fname, lname, "wing")
        else:
            super().__init__(fname, lname, "st")
    
    def add_game(self, opp):
        print("Enter " + self._get_fullname() + "\'s stats v. " + opp)
        print()
        mr = input("match rating: ")
        mins = input("minutes played: ")
        dribatt = input("dribble attempts: ")
        dribcomp = input("dribbles completed: ")
        if self._pos_abrv == "wing":
            oppbeat = input("opponents beaten: ")
        goals = input("goals: ")
        expgoals = input("expected goals: ")
        shotatt = input("shot attempts: ")
        sot = input("shots on target: ")
        if self._pos_abrv == "wing":
            asts = input("assists: ")
            expasts = input("expected asists: ")
        if self._pos_abrv == "st":
            passatt = input("pass attempts: ")
            passcomp = input("passes completed: ")
        print()
        print("1) confirm stats")
        print("2) renter info")
        choice = int(input())
        print()
        if choice == 2:
            self.add_game(opp)
        else:
            if self._pos_abrv == "wing":
                self._print_game_to_file(opp, mins, mr, dribatt, dribcomp, oppbeat, goals, expgoals, shotatt, sot, asts, expasts)
            else:
                self._print_game_to_file(opp, mins, mr, dribatt, dribcomp, goals, expgoals, shotatt, sot, passatt, passcomp)
        
    def calc_stats(self, nextmet):
        mins = 0
        mr = 0.0
        dribatt = 0
        dribcomp = 0
        if self._pos_abrv == "wing":
            oppbeat = 0
        goals = 0
        expgoals = 0.0
        shotatt = 0
        sot = 0
        if self._pos_abrv == "wing":
            asts = 0
            expasts = 0.0
        if self._pos_abrv == "st":
            passatt = 0
            passcomp = 0
        temp = self._head   
        while temp != None:
            mins = mins + temp.mins
            mr = mr + temp.mr
            dribatt = dribatt + temp.dribatt
            dribcomp = dribcomp + temp.dribcomp
            if self._pos_abrv == "wing":
                oppbeat = oppbeat + temp.oppbeat
            goals = goals + temp.goals
            expgoals = expgoals + temp.expgoals
            shotatt = shotatt + temp.shotatt
            sot = sot + temp.sot
            if self._pos_abrv == "wing":
                asts = asts + temp.asts
                expasts = expasts + temp.expasts
            if self._pos_abrv == "st":
                passatt = passatt + temp.passatt
                passcomp = passcomp + temp.passcomp
            temp = temp.next
        if dribatt == 0:
            dribpct = 0.00
        else:
            dribpct = round(((dribcomp/dribatt)*100), 2)   
        if shotatt == 0:
            shotpct = 0.00
        else:
            shotpct = round(((sot/shotatt)*100), 2)
        if self._pos_abrv == "st":
            passpct = round(((passcomp/passatt)*100), 2)
        if nextmet == "totals":
            if self._pos_abrv == "wing":
                self.__print_totals(mins, mr, dribatt, dribcomp, dribpct, oppbeat, goals, expgoals, shotatt, sot, shotpct, asts, expasts)
            else:
                self.__print_totals(mins, mr, dribatt, dribcomp, dribpct, goals, expgoals, shotatt, sot, shotpct, passatt, passcomp, passpct)
        elif nextmet == "avgs":
            games = mins/90.0
            mr = round((mr/gself._ll_size),2)
            dribatt = round((dribatt/games),2)
            dribcomp = round((dribcomp/games),2)
            if self._pos_abrv == "wing":
                oppbeat = round((oppbeat/games),2)
            goals = round((goals/games),2)
            expgoals = round((expgoals/games),2)
            shotatt = round((shotatt/games),2)
            sot = round((sot/games),2)
            if self._pos_abrv == "wing":
                asts = round((asts/games),2)
                expasts = round((expasts/games),2)
            if self._pos_abrv == "st":
                passatt = round((passatt/games),2)
                passcomp = round((passcomp/games),2)
            if dribatt == 0:
                dribpct = 0.00
            else:
                dribpct = round(((dribcomp/dribatt)*100), 2)   
            if shotatt == 0:
                shotpct = 0.00
            else:
                shotpct = round(((sot/shotatt)*100), 2)
            if self._pos_abrv == "st":
                passpct = round(((passcomp/passatt)*100), 2)
            if self._pos_abrv == "wing":
                self.__print_avgs(games, mr, dribatt, dribcomp, dribpct, oppbeat, goals, expgoals, shotatt, sot, shotpct, asts, expasts)
            else:
                self.__print_avgs(games, mr, dribatt, dribcomp, dribpct, goals, expgoals, shotatt, sot, shotpct, passatt, passcomp, passpct)
        else:
            pass
    
    def __print_avgs(self, a, b, c, d, e, f, g, h, i, j, k , l, m):
        print(" over " + str(round(a,2)) + " games:")
        if self._pos_abrv == "wing":
            print("\tmatch rating: " + str(b) + "\n\tdribble attempts: " + str(c) + "\n\tdribbles completed: " + str(d) + "\n\tdribble success rate: " + str(e) + "%" + "\n\topponents beat: " + str(f) + "\n\tgoals: " + str(g) + "\n\texpected goals: " + str(h) + "\n\tshot attempts: " + str(i) + "\n\tshots on target: " + str(j) + "\n\tshot accuracy: " + str(k) + "%" + "\n\tassists: " + str(l) + "\n\texpected assists: " + str(m))
        else:
            print("\tmatch rating: " + str(b) + "\n\tdribble attempts: " + str(c) + "\n\tdribbles completed: " + str(d) + "\n\tdribble success rate: " + str(e) + "%" + "\n\tgoals: " + str(f) + "\n\texpected goals: " + str(g) + "\n\tshot attempts: " + str(h) + "\n\tshots on target: " + str(i) + "\n\tshot accuracy: " + str(j) + "%" + "\n\tpass attempts: " + str(k) + "\n\tpassess completed: " + str(l) + "\n\tpass completion rate: " + str(m) + "%")
    
    def __print_totals(self, a, b, c, d, e, f, g, h, i, j, k , l, m):
        if self._pos_abrv == "wing":
            print("\tminutes: " + str(a) + "\n\tmatch ratings: " + str(round(b,2)) + "\n\tdribble attempts: " + str(c) + "\n\tdribbles completed: " + str(d) + "\n\tdribble success rate: " + str(e) + "%" + "\n\topponents beat: " + str(f) + "\n\tgoals: " + str(g) + "\n\texpected goals: " + str(h) + "\n\tshot attempts: " + str(i) + "\n\tshots on target: " + str(j) + "\n\tshot accuracy: " + str(k) + "%" + "\n\tassists: " + str(l) + "\n\texpected assists: " + str(m))
        else:
            print("\tminutes: " + str(a) + "\n\tmatch ratings: " + str(round(b,2)) + "\n\tdribble attempts: " + str(c) + "\n\tdribbles completed: " + str(d) + "\n\tdribble success rate: " + str(e) + "%" + "\n\tgoals: " + str(f) + "\n\texpected goals: " + str(g) + "\n\tshot attempts: " + str(h) + "\n\tshots on target: " + str(i) + "\n\tshot accuracy: " + str(j) + "%" + "\n\tpass attempts: " + str(k) + "\n\tpassess completed: " + str(l) + "\n\tpass completion rate: " + str(m) + "%")