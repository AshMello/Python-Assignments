stores = []

from class1shoppinglist import *

def add_store():
    name = input('Select a store ')
    store_name = ShoppingList(name)
    stores.append(store_name)

def view_full_cart():
    for store in stores:
        print(f"{stores.index(store)+1} . {store.name}")
        for item in store.items_to_buy:
            print(f"{item.item} , {item.price} , {item.quantity}")

def view_all():
    for store in stores:
        print(f"{stores.index(store)+1} . {store.name}")

def add_item():
    while True:
        try:
            view_all()
            choice = int(input('What store number would you like to add an item to? '))
            index = choice
            store_choice = stores[index-1]
            item = input('What item would you like to add? ')
            price = float(input('What price is the item? '))
            quantity = int(input('What is the item quantity? '))
            new_item = ItemChoice(item, price, quantity)

            store_choice.items_to_buy.append(new_item)
            for store in stores:
                print(f"{stores.index(store)+1} . {store.name}")
            for item in store.items_to_buy:
                print(f"{item.item} , {item.price} , {item.quantity}")
            view_menu()
            break
        except ValueError:
            print('Please enter a number and not a letter')
        except IndexError:
            print('Please enter one of the numbers listed')

def total_amount():
    total = 0
    for store in stores:
        for item in store.items_to_buy:
            total += (item.price*item.quantity)
            print(total)
    
def view_menu():
    print('Press 1 to add store')
    print('Press 2 to add item')
    print('Press 3 to view cart items')
    print('Press 4 to view total')
    print('Press x to exit')

user_input = ""
view_menu()
while user_input != 'x':
    user_input = input('Enter your choice ')
    if user_input == '1':
        add_store()
    elif user_input == '2':
        add_item()
    elif user_input == '3':
        view_full_cart()
    elif user_input == '4':
        total_amount()

