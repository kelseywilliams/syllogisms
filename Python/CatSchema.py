class CatSchema:
    STATEMENT = ["a","p","t","k","i","e","b","d","g","o"]
    def __init__(self, statement, s="S", p="P"):
        if statement not in CatSchema.STATEMENT:
            raise Exception("Invalid statment given")
        self.statement = statement
        self.s = s
        self.p = p
        
    def obversion(self):
        index = CatSchema.STATEMENT.index(self.statement)
        if index >= 5:
            self.statement = CatSchema.STATEMENT[0:4][index - 5]
        else:
            self.statement = CatSchema.STATEMENT[5:10][index]
        self.compliment(1)
    
    def compliment(self, term):
        if term:
            self.p = "non-" + self.p
        else:
            self.s = "non-" + self.s
    
    def construct(self):
        categorical_propositions = {"a": f"All {self.s} are {self.p}.","p": f"Almost all {self.s} are {self.p}.","t": f"Most {self.s} are {self.p}.","k": f"Many {self.s} are {self.p}.","i": f"Some {self.s} are {self.p}.","e": f"No {self.s} are {self.p}.","b": f"Few {self.s} are {self.p}.","d": f"Most {self.s} are not {self.p}.","g": f"Many {self.s} are not {self.p}.","o": f"Some {self.s} are not {self.p}."}
        print(categorical_propositions[self.statement])