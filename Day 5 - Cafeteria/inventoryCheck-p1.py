# Read the puzzle input and split it by the '\n'
freshDateTemp = open('Day 5 - Cafeteria/freshDate.txt').read().split('\n')
freshDate = [x.split('-') for x in freshDateTemp]

# Read the puzzle input and split it by the '\n'
checkedItem = open('Day 5 - Cafeteria/checkedItem.txt').read().split('\n')

fresh = 0

for items in checkedItem:
    for freshRange in freshDate:
        if int(items) > int(freshRange[0]) and int(items) < int(freshRange[1]):
            fresh += 1
            break

print(f"Still fresh items: {fresh}")