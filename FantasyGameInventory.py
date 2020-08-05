def displayInventory(inventory):
    print('Inventory:')
    totalCount = 0
    for item, count in inventory.items():
        print(str(count) + ' ' + item)
        totalCount += count
    print('Total number of items: ' + str(totalCount))

def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory

exampleInventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
displayInventory(exampleInventory)

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(exampleInventory, dragonLoot)
displayInventory(inv)