from python_capstone import Occurence, Inventory, Item, Character

inv = Inventory()
inv.get_item(Character("You"))


inv.list_inventory()

loss = Occurence(inv)
loss.depression()
