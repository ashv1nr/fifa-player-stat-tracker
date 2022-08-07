
class CMGame():
    
    def __init__(self, opp, mins, mr, dribatt, dribcomp, oppbeat, goals, expgoals, asts, expasts, passatt, passcomp, tackatt, tackwon, intcep, bbo):
        self.opp = opp
        self.mins = int(mins)
        self.mr = float(mr)
        self.dribatt = int(dribatt)
        self.dribcomp = int(dribcomp)
        self.oppbeat = int(oppbeat)
        self.goals = int(goals)
        self.expgoals = float(expgoals)
        self.asts = int(asts)
        self.expasts = float(expasts)
        self.passatt = int(passatt)
        self.passcomp = int(passcomp)
        self.tackatt = int(tackatt)
        self.tackwon = int(tackwon)
        self.intcep = int(intcep)
        self.bbo = int(bbo)
        self.next = None
        self.prev = None
        
    def to_string(self):
        return str(self.opp) + "\n\tminutes: " + str(self.mins) + "\n\tmacth rating: " + str(self.mr) + "\n\tdribble attempts: " + str(self.dribatt) + "\n\tdribbles completed: " + str(self.dribcomp) + "\n\topponents beat: " + str(self.oppbeat) + "\n\tgoals: " + str(self.goals) + "\n\texpected goals: " + str(self.expgoals) + "\n\tassists: " + str(self.asts) + "\n\texpected assists: " + str(self.expasts) + "\n\tpass attempts: " + str(self.passatt) +"\n\tpassess completed: " + str(self.passcomp) + "\n\ttackle attempts: " + str(self.tackatt) + "\n\ttackles won: " + str(self.tackwon) + "\n\tinterceptions: " + str(self.intcep) + "\n\ttimes beaten by opponent: " + str(self.bbo)