# Read the puzzle input and split it by the '\n'
batteryBanks = open('Day 3 - Lobby/batteryBanks.txt').read().split('\n')

def largestPossible(batteryCell):
    print(batteryCell)
    bigNumber = list((sorted(set(batteryCell),reverse=True)))
    
    for i in bigNumber:
        allIindex = [ind for ind,v in enumerate(batteryCell) if v == i]
        for j in bigNumber:
            if i == j:
                if len(allIindex) > 1:
                    print(f"Biggest number: {int(i+i)}, Largest digit: {bigNumber[0]}")
                    return int(i+i)
            for indexOfi in allIindex:
                try:
                    res = batteryCell.index(str(j), indexOfi)
                    if res > indexOfi:
                        print(f"Biggest number: {int(i+j)}, Largest digit: {bigNumber[0]}")
                        return int(i+j)
                except:
                    continue

result = list(map(largestPossible,batteryBanks))
print(sum(result))