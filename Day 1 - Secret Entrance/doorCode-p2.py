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

test = [strToint(x) for x in ['R1000','L1000','L50','R1','L1','L1','R1','R100','R1']]

for rotation in directionalCode:
    '''
    Limit so that the dial won't go above one full rotation
    Since 0 to 99 is a 100 number, the limit is 100
    '''
    if rotation <= -100:
        while rotation <= -100:
            rotation += 100
            # Additional line for part 2
            zeroOccurence += 1

    elif rotation >= 100:
        while rotation >= 100:
            rotation -= 100
            # Additional line for part 2
            zeroOccurence += 1
    
    tempdial = dial
    dial += rotation

    if dial > 99:
        dial -= 100
        # Additional line for part 2 - prevent registered double
        if dial != 0 and tempdial != 0:
            zeroOccurence += 1
    elif dial < 0:
        dial = 100 + dial
        # Additional line for part 2 - prevent registered double
        if dial != 0 and tempdial != 0:
            zeroOccurence += 1
    if dial == 0 and tempdial != 0:
        zeroOccurence +=1

    print(f"Previous: {tempdial}, Rotation: {rotation}, Now: {dial}, Zero: {zeroOccurence}")

print("Key:", zeroOccurence)
