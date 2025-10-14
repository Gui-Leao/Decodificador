
from math import log10

def binary_to_ascii(file_path:str) -> str:
    
    with open(file_path, "r") as f:
        bits = f.read() 

    message = ''.join([chr(int(b,2)) for b in bits.split()])

    return message

def show_caesar_cipher(message:str) -> None:

    for i in range(1,27):
        for letter in  message:
    
            ascii_code = ord(letter)
            if ascii_code != 32:

                alpha_position_new_letter = (ascii_code-65+i)%26
                new_letter = chr(alpha_position_new_letter+65)

                print(new_letter,end='')

        print("=="*80)

class ngram_score(object):
    def __init__(self,ngramfile,sep=' '):
        ''' load a file containing ngrams and counts, calculate log probabilities '''
        self.ngrams = {}
        for line in open(ngramfile).readlines():
            key,count = line.split(sep) 
            self.ngrams[key] = int(count)
        self.L = len(key)
        self.N = sum(self.ngrams.values())
        #calculate log probabilities
        for key in self.ngrams.keys():
            self.ngrams[key] = log10(float(self.ngrams[key])/self.N)
        self.floor = log10(0.01/self.N)

    def score(self,text):
        ''' compute the score of text '''
        score = 0
        ngrams = self.ngrams.__getitem__
        for i in range(len(text)-self.L+1):
            if text[i:i+self.L] in self.ngrams: score += ngrams(text[i:i+self.L])
            else: score += self.floor          
        return score
       




if __name__ == "__main__":
    main()