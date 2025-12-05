# Read the puzzle input and split it by the ','
availableRange = open('Day 2 - Gift SHop/idRange.txt').read().split(',')
availableRange = [x.split('-') for x in availableRange]

output = 0

for idRange in availableRange:
    print(f"Current Range: {idRange[0]}-{idRange[1]}")
    for employeeId in range(int(idRange[0]), int(idRange[1])+1):
        temp = str(employeeId)
        if len(temp)%2 != 0:
            continue
        if temp[:len(temp)//2] == temp[len(temp)//2:]:
            output += employeeId

print(output)