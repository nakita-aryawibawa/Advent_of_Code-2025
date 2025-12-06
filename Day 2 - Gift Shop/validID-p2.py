# Read the puzzle input and split it by the ','
availableRange = open('Day 2 - Gift SHop/idRange.txt').read().split(',')

# Continue splitting to get a list of list of range
availableRange = [x.split('-') for x in availableRange]

output = 0

for idRange in availableRange:
    print(f"Current Range: {idRange[0]}-{idRange[1]}")
    similar = 0
    for employeeId in range(int(idRange[0]), int(idRange[1])+1):
        stringified = str(employeeId)

        # Exclude single digits
        if len(stringified) == 1:
            continue

        # Check if employeeId consist of one number
        if len(set(stringified)) == 1:
            output += employeeId
            similar += 1
            continue

        # Check if employeeId can be fully erased by replace
        for length in range(2,(len(stringified)//2)+1):
            temp = stringified
            eraser = temp[:length]
            if temp.replace(eraser, "") == "":
                output += employeeId
                similar += 1
                break
    print(similar)

print(output)