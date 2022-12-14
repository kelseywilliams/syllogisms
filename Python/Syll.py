# Kelsey Williams 10-4-2022
'''
Creates a valid syllogism from a mood.  For example, AAA1 where a is A is the letter pertaining to
a statement such as All M are P and 1 is the figure of the syllogism. 
Example use:
syll = Syll(["a","a","a",1])

@param mood  A list containg three characters that are also elements of CatSchema.STATEMENT 
and one integer between 1 and 4 corresponding to the syllogisms figure.

Methods:
valid()     returns true if the syllogism passes all rules.  Takes no arguments
check_rule(rule)  returns true if the syllogism passes the rule.  Takes an integer 1 through 4
return_mood() returns the mood of the syllogism as a list.  Takes no arguments.
'''
from CatSchema import CatSchema
class Syll:
    STATEMENT = CatSchema.STATEMENT
    # Set distribution reference constant
    DIST_REF = {"a":(5,1),"p":(4,1),"t":(3,1),"k":(2,1),"i":(1,1),"e":(5,5),"b":(4,5),"d":(3,5),"g":(2,5),"o":(1,5)}
    def __init__(self, mood):
        # Unpack object arguments
        if len(mood) != 4:
            raise Exception("Too few elements passed to Syll::constructor().  mood must be a list of length 4.")
        self.premise1_statement = mood[0]
        self.premise2_statement = mood[1]
        self.conc_statement = mood[2]
        self.cs_premise1 = CatSchema(self.premise1_statement)
        self.cs_premise2 = CatSchema(self.premise2_statement)
        self.cs_conc = CatSchema(self.conc_statement)
        self.fig = mood[3]
        # Declare a tuple of weights distributed according to the quantity and quality of the statement
        self.weights = (Syll.DIST_REF[self.premise1_statement], Syll.DIST_REF[self.premise2_statement], Syll.DIST_REF[self.conc_statement])
        # Unpack the tuple of weights
        self.major, self.minor, self.conc = self.weights
        # Declare terms and predicate
        self.m1 = self.m2 = self.p1 = self.p2 = self.s1 = self.s2 = 0
        self.predicate1 = self.predicate2 = self.predicate_c = 0
        self._set_fig()

    def _first_fig(self):
        self.m1, self.p1 = self.major
        self.cs_premise1.update_terms("M","P")
        self.s1, self.m2 = self.minor
        self.cs_premise2.update_terms("S","M")
        self.s2, self.p2 = self.conc

        self.predicate1 = self.p1
        self.predicate2 = self.m2
        self.predicate_c = self.p2

    def _second_fig(self):
        self.p1, self.m1 = self.major
        self.cs_premise1.update_terms("P","M")
        self.s1, self.m2 = self.minor
        self.cs_premise2.update_terms("S","M")
        self.s2, self.p2 = self.conc

        self.predicate1 = self.m1
        self.predicate2 = self.m2
        self.predicate_c = self.p2
    
    def _third_fig(self):
        self.m1, self.p1 = self.major
        self.cs_premise1.update_terms("M","P")
        self.m2, self.s1 = self.minor
        self.cs_premise2.update_terms("M","S")
        self.s2, self.p2 = self.conc

        self.predicate1 = self.p1
        self.predicate2 = self.s1
        self.predicate_c = self.p2

    def _fourth_fig(self):
        self.p1, self.m1 = self.major
        self.cs_premise1.update_terms("P","M")
        self.m2, self.s1 = self.minor
        self.cs_premise2.update_terms("M","S")
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
        return [self.premise1_statement, self.premise2_statement, self.conc_statement, self.fig]
    
    def construct_schema(self):
        premise1 = self.cs_premise1.construct()
        premise2 = self.cs_premise2.construct()
        conc = self.cs_conc.construct()
        return [premise1,premise2,conc]
    
    def print_schema(self):
        props = self.construct_schema()
        for prop in props:
            print(prop)
