from Syll import Syll
'''
Creates lists of Syll objects.
'''
class SyllBuilder:
    # Returns a list of Syll objects
    def return_all_sylls(self):
        sylls = []
        for i in range(10):
            for j in range(10):
                for k in range(10):
                    for l in range(4):
                        syll = Syll(Syll.STATEMENT[i], Syll.STATEMENT[j], Syll.STATEMENT[k], l+1)
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