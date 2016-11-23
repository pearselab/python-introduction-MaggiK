# Python Intro Programming for Biologists
# fall 2016
# Algorithms
#Maggi Kraft

#Bubble Sort
#use Will's swap function to swap places
#buble sort: where is some list of numbers
def bubbles(S):
    for L in range(len(S)-1,0,-1):    
        for i in range(L):
            if S[i]>S[i+1]:
                tmp = S[i]
                S[i] = S[i+1]
                S[i+1] =tmp

S=[4,9,15,2,3,22,6,15,19]
bubbles(S)     
print(S)
