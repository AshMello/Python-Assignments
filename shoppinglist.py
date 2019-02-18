stores = []
class ShoppingList:
    def __init__(self, name):
        self.name = name
        self.items_to_buy = []
    def __repr__(self):
        return self.name

class ItemChoice:
    def __init__(self, item, price, quantity):
        self.item = item
        self.price = int(price)
        self.quantity = int(quantity) 
    def __repr__(self):
        return self.item
    

def add_store():
    name = input('Select a store ')
    store_name = ShoppingList(name)
    stores.append(store_name)

def view_all():
    for (store) in stores:
         print(f"{stores.index(store)+1} . {store.name}")

def add_item():
    view_all()
    choice = int(input('What store number would you like to add an item to? '))
    index = choice
    store_choice = stores[index-1]
    item = input('What item would you like to add? ')
    price = int(input('What price is the item? '))
    quantity = int(input('What is the item quantity? '))
    new_item = ItemChoice(item, price, quantity)

    store_choice.items_to_buy.append(new_item)
    for store in stores:
        print(f"{stores.index(store)+1} . {store.name} . {store.items_to_buy}")

def view_menu():
    print('Press 1 to add store')
    print('Press 2 to add item')
    print('Press 3 to delete item')
    print('Press 4 to view list')
    print('Press x to exit')

user_input = ""
view_menu()
while user_input != 'x':
    user_input = input('Enter your choice ')
    if user_input == '1':
        add_store()
    if user_input == '2':
        add_item()
    if user_input == '3':
        del_item()
    if user_input == '4':
        view_all()

