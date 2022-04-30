def displayInventory():
    num = 0
    print("Inventory:")
    for k, v in inventory.items():
        print(v, k)
        num += v
    print("Total number of items:", num)


def addToInventory(inv, addedItems):
    newInv = inv
    for item in addedItems:
        if item in inv.keys():
            newInv[item] = newInv[item] + 1
        else:
            newInv[item] = 1

    return newInv


inventory = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inventory = addToInventory(inventory, dragonLoot)
displayInventory()
