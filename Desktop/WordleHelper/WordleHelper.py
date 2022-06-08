
from msilib.schema import SelfReg
from turtle import clear


class wordle:
    def __init__(self, L1 = None, L2 = None, L3 = None, L4 = None):
        self.letter1 = L1
        self.letter2 = L2
        self.letter3 = L3
        self.letter4 = L4
        self.words = []
        with open('5 letter words.txt','r') as f:
            strip_lines = [line.strip() for line in f]
            self.words = strip_lines
            self.words.sort()
    
    def getletter1(self):
        return self.letter1
    def getletter2(self):
        return self.letter2
    def getletter3(self):
        return self.letter3
    def getletter4(self):
        return self.letter4

    def lettersContained(self):
        champions = []
        
        if((self.letter1 != None) and (self.letter2 != None) and (self.letter3 != None) and (self.letter4 != None)):  #4 letters
            for word in self.words:
                if (self.letter1 in word) and (self.letter2 in word) and (self.letter3 in word) and (self.letter4 in word):
                    champions.append(word)
            return champions
        
        elif((self.letter1 != None) and (self.letter2 != None) and (self.letter3 != None)):   #3 letters
            for word in self.words:
                if (self.letter1 in word) and (self.letter2 in word) and (self.letter3 in word):
                    champions.append(word)
            return champions

        elif((self.letter1 != None) and (self.letter2 != None)):   #2 letters
            for word in self.words:
                if (self.letter1 in word) and (self.letter2 in word):
                    champions.append(word)
            return champions

        elif(self.letter1 != None):   #1 letter 
            for word in self.words:
                if self.letter1 in word:
                    champions.append(word)
            return champions

"""game1 = wordle("s","a")
game1.getletter1()
game1.getletter2()
game1.lettersContained()"""
