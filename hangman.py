#game
print("this is palyer1 time")
realword=input("enter the word wants to be guess:").lower()
length=len(realword)
hanglist=['-' for dash in range(length)]
print(hanglist)
print("this is player2 time")
count=1
while count==1:
    guessword=input("enter the guessing word:").lower()
    if guessword in realword:
        index=realword.index(guessword)
        print(index)
        

        
    

    
