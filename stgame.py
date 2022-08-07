
class STGame():

    def __init__(self, opp, mins, mr, dribatt, dribcomp, goals, expgoals, shotatt, sot, passatt, passcomp):
        self.opp = opp
        self.mins = int(mins)
        self.mr = float(mr)
        self.dribatt = int(dribatt)
        self.dribcomp = int(dribcomp)
        self.goals = int(goals)
        self.expgoals = float(expgoals)
        self.shotatt = int(shotatt)
        self.sot = int(sot)
        self.passatt = int(passatt)
        self.passcomp = int(passcomp)
        self.next = None
        self.prev = None
        
    def to_string(self):
        return str(self.opp) + "\n\tminutes: " + str(self.mins) + "\n\tmatch rating: " + str(self.mr) + "\n\tdribble attempts: " + str(self.dribatt) + "\n\tdribbles completed: " + str(self.dribcomp) + "\n\tgoals: " + str(self.goals) + "\n\texpected goals: " + str(self.expgoals) + "\n\tshot attempts: " + str(self.shotatt) + "\n\tshots on target: " + str(self.sot) + "\n\tpass attempts: " + str(self.passatt) + "\n\tpasses completed: " + str(self.passcomp)