from datetime import datetime
from time import time
import json
#now = datetime.now()


pool_tables = []

class PoolTable: 
    def __init__(self, table_number):
        self.table_number = table_number
        self.is_available = "Unoccupied"
        self.start_time = datetime.now()
        self.end_time = datetime.now()

    def checkout(self):
        self.is_available = "Occupied"
        self.start_time = datetime.now()
    
    def closeout(self):
        self.is_available = "Unoccupied"
        self.end_time = datetime.now()



for index in range(1,13):
    pool_table = PoolTable(index)
    pool_tables.append(pool_table)

def close_out_tab():
        try:
            choice = int(input('Which table would you like to close? '))
            pool_table = pool_tables[choice-1]
            pool_table.closeout()
            difference = pool_table.end_time - pool_table.start_time
            table_json = [{'tableNumber': pool_table.table_number}, {'Start time': str(pool_table.start_time)},{'End time': str(pool_table.end_time)}, {'Elasped time': str(difference)}]

            with open('pooltables1.json','w') as file_object:
                json.dump(table_json, file_object)
            
            print(f"Table number {pool_table.table_number} Elasped Time: {difference}")
        except ValueError:
             print('Please enter a number and not a letter')
        except IndexError:
            print('Please enter a table number')
            print(main_menu())


def reserve_table():
        try:
            see_tables()
            choice = int(input('Which table would you like to reserve? '))
            pool_table = pool_tables[choice-1]
            while pool_table.is_available == 'Unoccupied':
                pool_table.checkout()
                print(f"Table One {pool_table.table_number} {pool_table.is_available} {pool_table.start_time}")
            else:
                print('Please select an unoccupied table')
        except ValueError:
             print('Please enter a number and not a letter')
        except IndexError:
            print('Please enter a table number')


def see_tables():
   for table in pool_tables:
       print(f" Table number {table.table_number} {table.is_available}")

def main_menu():
    print('To reserve a table press 1')
    print('To close a table press 2')
    print('To view status of tables press 3')
    print('To quit program completely press Q')
    

main_menu()

user_input = ''
while user_input != 'q':
    user_input= input('Enter your choice: ')
    if user_input == '1':
        reserve_table()
    elif user_input == '2':
        see_tables()
        close_out_tab()
    elif user_input == '3':
        see_tables()

