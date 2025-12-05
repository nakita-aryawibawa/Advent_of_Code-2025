# Read the puzzle input and split it by the '\n'
doorSequence = open('Day 1 - Secret Entrance/puzzleInput.txt').read().split('\n')

# Change input from L R to - +
def strToint(x):
    if x.startswith('R'):
        return int(x[1:])
    elif x.startswith('L'):
        return -int(x[1:])
    
directionalCode = [strToint(x) for x in doorSequence]

# Neutral state of dial
dial = 50

# Number of time dial land on 0 - RESULT
zeroOccurence = 0

for rotation in directionalCode:
    '''
    Limit so that the dial won't go above one full rotation
    Since 0 to 99 is a 100 number, the limit is 100
    '''
    if rotation <= -100:
        while rotation <= -100:
            rotation += 100
    elif rotation >= 100:
        while rotation >= 100:
            rotation -= 100
    
    tempdial = dial
    dial += rotation

    if dial > 99:
        dial -= 100
        
    elif dial < 0:
        dial = 100 + dial

    print(f"Previous: {tempdial}, Rotation: {rotation}, Now: {dial}")

    if dial == 0:
        zeroOccurence +=1

print("Key:", zeroOccurence)