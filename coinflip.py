#PYCOINFLIP

#Initialisation
import random
def lineBreak(): print("----------")

#Title
print("PYCOINFLIP")
print("A coinflip generator by Droidge")
lineBreak()

#Initial variables
heads = 0
tails = 0
doneFlip = 0

#Number of flips are set here
needFlip = int(raw_input("Please enter the number of flips to simulate: "))
print(str(needFlip) + " flips it is.")
lineBreak()

#User confirmation
confirm = raw_input("Please press Enter to start the process.")
lineBreak()

#Calculation process
while doneFlip < needFlip:
    #Deciding whether result is heads or tails
    coin = random.random()
    if coin < 0.5:
        heads = heads + 1
        print("Flip #" + str(doneFlip) + ": Heads.")
    else:
        tails = tails + 1
        print("Flip #" + str(doneFlip) + ": Tails.")
    doneFlip = doneFlip + 1
lineBreak()

#Display results
print("Result:")
print(str(heads) + " heads.")
print(str(tails) + " tails.")
lineBreak()

        
    




