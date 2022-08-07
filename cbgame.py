
class CBGame():

    def __init__(self, opp, mins, mr, passatt, passcomp, tackatt, tackwon, intcep, blk, adw, bbo, cleshe):
        self.opp = opp
        self.mins = int(mins)
        self.mr = float(mr)
        self.passatt = int(passatt)
        self.passcomp = int(passcomp)
        self.tackatt = int(tackatt)
        self.tackwon = int(tackwon)
        self.intcep = int(intcep)
        self.blk = int(blk)
        self.adw = int(adw)
        self.bbo = int(bbo)
        self.cleshe = int(cleshe)
        self.next = None
        self.prev = None
        
    def to_string(self):
        if self.cleshe == 1:
            cs = "yes"
        else:
            cs = "no"
        return str(self.opp) + ":\n\tminutes: " + str(self.mins) + "\n\tmatch rating: " + str(self.mr) + "\n\tpass attempts: " + str(self.passatt) + "\n\tpasses completed: " + str(self.passcomp) + "\n\ttackle attempts: " + str(self.tackatt) + "\n\ttackles won: " + str(self.tackwon) + "\n\tinterceptions: " + str(self.intcep) + "\n\tblocks: " + str(self.blk) + "\n\taerial duels won: " + str(self.adw) + "\n\ttimes beaten by opponent: " + str(self.bbo) + "\n\tclean sheet: " + cs