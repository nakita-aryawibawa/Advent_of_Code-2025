# Read the puzzle input and split it by the '\n'
paperWarehouseTemp = open('Day 4- Printing Department/paperWarehouse.txt').read().split('\n')

# Turn every row into a list and split the string into individual character
paperWarehouse = [list(x) for x in paperWarehouseTemp]

# How many roll can be moved - RESULT
canBeMoved = 0
for indRow, rowValue in enumerate(paperWarehouse):
    for indCol, columnValue in enumerate(rowValue):
        # Skip empty spot
        if columnValue == ".":
            continue

        # Grid position outside current index
        gridTop = indRow-1
        gridBot = indRow+1
        gridLeft = indCol-1
        gridRight = indCol+1

        rows = [gridTop, indRow, gridBot]
        columns = [gridLeft, indCol, gridRight]

        neighbor = []
        for row in rows:
            if row < 0 or row >= len(paperWarehouse):
                continue
            else:
                for column in columns:
                    if (column < 0 or column >= len(rowValue)) or (row == indRow and column == indCol):
                        continue
                    else:
                        neighbor.append(paperWarehouse[row][column])

        if neighbor.count("@") < 4:
            print(sorted(neighbor, reverse=True))
            canBeMoved += 1

print(f"Paper roll that can be moved: {canBeMoved}")