
class FBGame():

    def __init__(self, opp, mins, mr, asts, expasts, tackatt, tackwon, intcep, bbo, cleshe):
        self.opp = opp
        self.mins = int(mins)
        self.mr = float(mr)
        self.asts = int(asts)
        self.expasts = float(expasts)
        self.tackatt = int(tackatt)
        self.tackwon = int(tackwon)
        self.intcep = int(intcep)
        self.bbo = int(bbo)
        self.cleshe = int(cleshe)
        self.next = None
        self.prev = None
        
    def to_string(self):
        if self.cleshe == 1:
            cs = "yes"
        else:
            cs = "no"
        return str(self.opp) + ":\n\tminutes: " + str(self.mins) + "\n\tmatch rating: " + str(self.mr) + "\n\tassists: " + str(self.asts) + "\n\texpected assists: " + str(self.expasts) + "\n\ttackle attempts: " + str(self.tackatt) + "\n\ttackles won: " + str(self.tackwon) + "\n\tinterceptions: " + str(self.intcep) + "\n\ttimes beaten by opponent: " + str(self.bbo) + "\n\tclean sheet: " + cs