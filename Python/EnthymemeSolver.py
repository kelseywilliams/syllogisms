'''
Solves an enthymeme.  
Example use:
es = EnthymemeSolver(["a","a"],True)
es = EnthymemeSolver(["e","a",1],True)

@param props  A list containing to characters that are elements of CatSchema.STATEMENT.  These two
character stand for the given propositions.  An optional figure indicator may be added to props,
an integer between 1 and 4.
@param s  Boolean flag indicating the proposition being solved for.  Set s to False to solve for
a premise and True to solve for a conclusion.
'''
from Syll import Syll
from SyllBuilder import SyllBuilder
class EnthymemeSolver:
    def __init__(self, props, s):
        self.statement1 = props[0]
        self.statement2 = props[1]
        self.fig = None
        if len(props) == 3:
            self.fig = props[2]
        self.s = s
    
    def solve(self):
        solutions = []
        sylls = SyllBuilder().return_all_valid()
        for syll in sylls:
            mood = syll.return_mood()
            if self.fig != None and mood[3] != self.fig: 
                continue
            if self.s:
                if mood[0] == self.statement1 and mood[1] == self.statement2:
                    if self.fig != None and mood[3] == self.fig:
                        solutions.append(mood)
                    elif self.fig == None:
                        solutions.append(mood)
            else:
                if mood[1] == self.statement1 and mood[2] == self.statement2:
                    solutions.append(mood)
                if mood[0] == self.statement1 and mood[2] == self.statement2:
                    solutions.append(mood)
        return solutions
    
    def strongest_arg(self):
        l = self.solve()
        if len(l) == 0:
            return []
        if self.s:
            return self.solve()[0]
        else:
            return self.solve()[len(self.solve())-1]
