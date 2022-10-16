# Kelsey Williams 10-4-2022
'''
Creates a valid syllogism from a mood.  For example, AAA1 where a is A is the letter pertaining to
a statement such as All M are P and 1 is the figure. When creating an instance of Syll, use one of
the letters listed in the Syll.STATEMENT constant and a number between 1 and 4.
Example use:
syll = Syll("a","a","a",1)

Methods:
valid()     returns true if the syllogism passes all rules.  Takes no arguments
check_rule(rule)  returns true if the syllogism passes the rule.  Takes an integer 1 through 4
return_mood() returns the mood of the syllogism as a string.  Takes no arguments.
'''
from CatSchema import CatSchema
class Syll:
    STATEMENT = CatSchema.STATEMENT
    # Set distribution reference constant
    DIST_REF = {"a":(5,1),"p":(4,1),"t":(3,1),"k":(2,1),"i":(1,1),"e":(5,5),"b":(4,5),"d":(3,5),"g":(2,5),"o":(1,5)}
    def __init__(self, premise1_statement, premise2_statement, conc_statement, fig):
        # Unpack object arguments
        self.premise1_statement = premise1_statement
        self.premise2_statement = premise2_statement
        self.conc_statement = conc_statement
        self.fig = fig
        # Declare a tuple of weights distributed according to the quantity and quality of the statement
        self.weights = (Syll.DIST_REF[premise1_statement], Syll.DIST_REF[premise2_statement], Syll.DIST_REF[conc_statement])
        # Unpack the tuple of weights
        self.major, self.minor, self.conc = self.weights
        # Declare terms and predicate
        self.m1 = self.m2 = self.p1 = self.p2 = self.s1 = self.s2 = 0
        self.predicate1 = self.predicate2 = self.predicate_c = 0
        self._set_fig()

    def _first_fig(self):
        self.m1, self.p1 = self.major
        self.s1, self.m2 = self.minor
        self.s2, self.p2 = self.conc

        self.predicate1 = self.p1
        self.predicate2 = self.m2
        self.predicate_c = self.p2

    def _second_fig(self):
        self.p1, self.m1 = self.major
        self.s1, self.m2 = self.minor
        self.s2, self.p2 = self.conc

        self.predicate1 = self.m1
        self.predicate2 = self.m2
        self.predicate_c = self.p2
    
    def _third_fig(self):
        self.m1, self.p1 = self.major
        self.m2, self.s1 = self.minor
        self.s2, self.p2 = self.conc

        self.predicate1 = self.p1
        self.predicate2 = self.s1
        self.predicate_c = self.p2

    def _fourth_fig(self):
        self.p1, self.m1 = self.major
        self.m2, self.s1 = self.minor
        self.s2, self.p2 = self.conc

        self.predicate1 = self.m1
        self.predicate2 = self.s1
        self.predicate_c = self.p2

    # Set the weights of the major, middle, and minor terms based on the figure
    def _set_fig(self):
        if(self.fig == 1):
            return self._first_fig()
        if(self.fig == 2):
            return self._second_fig()
        if(self.fig == 3):
            return self._third_fig()
        if(self.fig == 4):
            return self._fourth_fig()
        else:
            raise Exception("Error in Syll:_set_fig(): Invalid figure.  Please choose a number between 1 and 4")

    # Returns true if the syllogism breaks no rules, false if the syllogism breaks 1 or more rules.
    def valid(self):
        for i in range(4):
            if(self.check_rule(i+1) == False):
                return False
            elif(i == 3):
                return True
        return False
  
    def check_rule(self, rule):
        if(rule == 1 and self.m1 + self.m2 > 5):
            return True
        if(rule == 2 and self.s1 >= self.s2):
            return True
        if(rule == 3 and self.p1 >= self.p2):
            return True
        if(rule == 4 and (self.predicate1 + self.predicate2) == self.predicate_c + 1):
            return True
        return False
    
    # Returns the mood of the syllogism as a string
    def return_mood(self):
        return f"{self.premise1_statement}{self.premise2_statement}{self.conc_statement}{self.fig}"
    
    def construct_schema(self):
        premise1 = CatSchema(self.premise1_statement)
        premise2 = CatSchema(self.premise2_statement)
        conc = CatSchema(self.conc_statement)
        print(f"{premise1}\n{premise2}\n{conc}")
