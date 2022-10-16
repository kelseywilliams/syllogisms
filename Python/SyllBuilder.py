'''
Creates lists of Syll objects.
'''
from Syll import Syll
from CatSchema import CatSchema
class SyllBuilder:
    # Returns a list of Syll objects
    def return_all_sylls(self):
        sylls = []
        for i in range(10):
            for j in range(10):
                for k in range(10):
                    for l in range(4):
                        mood = [CatSchema.STATEMENT[i], CatSchema.STATEMENT[j], CatSchema.STATEMENT[k],l+1]
                        syll = Syll(mood)
                        sylls.append(syll)
        return sylls
    
    def return_all_valid(self):
        all_sylls = self.return_all_sylls()
        valid_sylls = []
        for syll in all_sylls:
            if syll.valid():
                valid_sylls.append(syll)
        return valid_sylls


    # Prints all 4000 possible syllogisms
    def print_all_sylls(self):
        for syll in self.return_all_sylls():
            print(syll.return_mood())