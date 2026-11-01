inventory = {"pen": 10, "notebook": 5} 
same_inventory = inventory 
copied_inventory = inventory.copy() 
same_inventory["pen"] += 2 
copied_inventory["notebook"] += 3 
print("inventory:", inventory) 
print("same_inventory:", same_inventory) 
print("copied_inventory:", copied_inventory)