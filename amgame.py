
class AMGame():
    
    def __init__(self, opp, mins, mr, dribatt, dribcomp, oppbeat, goals, expgoals, shotatt, sot, asts, expasts, tackatt, tackwon):
        self.opp = opp
        self.mins = int(mins)
        self.mr = float(mr)
        self.dribatt = int(dribatt)
        self.dribcomp = int(dribcomp)
        self.oppbeat = int(oppbeat)
        self.goals = int(goals)
        self.expgoals = float(expgoals)
        self.shotatt = int(shotatt)
        self.sot = int(sot)
        self.asts = int(asts)
        self.expasts = float(expasts)
        self.tackatt = int(tackatt)
        self.tackwon = int(tackwon)
        self.next = None
        self.prev = None
        
    def to_string(self):
        return str(self.opp) + "\n\tminutes: " + str(self.mins) + "\n\tmatch rating: " + str(self.mr) + "\n\tdribble attempts: " + str(self.dribatt) + "\n\tdribbles completed: " + str(self.dribcomp) + "\n\topponents beat: " + str(self.oppbeat) + "\n\tgoals: " + str(self.goals) + "\n\texpected goals: " + str(self.expgoals) + "\n\tshot attempts: " + str(self.shotatt) + "\n\tshots on target: " + str(self.sot) + "\n\tassists: " + str(self.asts) + "\n\texpected assists: " + str(self.expasts) + "\n\ttackle attempts: " + str(self.tackatt) + "\n\ttackles completed: " + str(self.tackwon)