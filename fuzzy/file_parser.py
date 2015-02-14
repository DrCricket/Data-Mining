import re

class parser:

    def __init__(self,fname):
        
        self.file = open(fname,"r+")
        self.str = ""
        for i in self.file:
            self.str = self.str + i
        self.tokens = self.str.split()
        #print tokens
        self.tokens = [re.sub(r'[^A-Za-z0-9]+', '', x) for x in self.tokens]
        #print self.tokens
        
    def sentence_avg(self): # Average length of sentences in terms of number of words
        
        end = re.compile('[.!?]')
        lst = end.split(self.str)
        sm=0.0
        for i in lst:
            sm = sm + len(i.split())
        sm = sm/len(lst)
        return sm
        
        
    def word_avg(self): # Average length of a word in an article in terms of the number of characters

        sum = 0.0
        for i in self.tokens:
            sum = sum + len(i)
        sum = sum/len(self.tokens)
        return sum




#p = parser("C:\Users\Chinka\Desktop\input.txt")
#print p.word_avg()
#print p.sentence_avg()
