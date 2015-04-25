# insert data via comand line 

import sqlite3
import os.path
import datetime
import time

db_name = 'expenses_by_category.db'
path_to_db = os.path.dirname(os.path.abspath(__file__)) + '/db/' + db_name
print('path to db: ', path_to_db)

def connect_to_db(path_to_db):
	'''
	Create connection to db. 
	Create cursor for SQL queries with name 'cursor'.
	Enable foreign keys.
	'''
	global connection, cursor 
	connection = sqlite3.connect(path_to_db)
	cursor = connection.cursor()
	
	cursor.execute('''PRAGMA foreign_keys = ON''') # enable foreign keys
	
def add_expense_to_db(string, cursor):
	''' Get data for expense table 
		Date, Total summ, Total discount 
		as a string with space as separator

		Connects to db and inserts data to expense table
		commit changes and close connection

		Convert expense date to unix timestamp with respect to local timezone
	'''

	data = string.split()
	data[0] = time.mktime(datetime.datetime.strptime(data[0],'%d-%m-%Y').timetuple())
	try:
		cursor.execute("""INSERT INTO expense (expense_date, total_sum, total_discount, category_id) VALUES (?,?,?,?)""", data)
		connection.commit()
	except sqlite3.IntegrityError:
		print('No such category. Please add it')


def list_expenses(cursor):
	''' Print records in expense table'''

	cursor.execute("""SELECT * FROM expense""")
	res = cursor.fetchall()
	for r in res:
		print(r)

def delete_expense(ex_id,cursor):
	''' Delete expense from db via expense_id'''

	cursor.execute('''DELETE FROM expense WHERE expense_id = ?''', ex_id)
	connection.commit()

def update_expense(ex_id,d_str,cursor):
	'''Updates expense via expense_id and new data'''

	data = d_str.split()
	data.append(ex_id)

	cursor.execute('UPDATE expense SET expense_date = ?, total_sum = ?, total_discount = ?, category_id = ? WHERE expense_id = ?', data)
	connection.commit()

def read_expese(ex_id_string,cursor):
	''' Select expense record via expense_id '''

	cursor.execute("SELECT * FROM expense WHERE expense_id = ?",ex_id_string)
	r = cursor.fetchall()
	print(r)

def add_category(data_str,cursor):
	''' Add category'''

	data = data_str.split()
	cursor.execute('''INSERT INTO categories (name, parent_category_id) VALUES (?, ?)''', data)
	connection.commit()

def list_categories(cursor):
	''' Print records in categories table'''

	cursor.execute("""SELECT * FROM categories""")
	res = cursor.fetchall()
	for r in res:
		print(r)

def delete_category(cat_id,cursor):
	''' Delete record from categories table via category_id'''

	cursor.execute('''DELETE FROM categories WHERE category_id = ?''', cat_id)
	connection.commit()

def update_category(cat_id, d_str,cursor):
	'''Updates category via category_id and new data'''

	data = d_str.split()
	data.append(cat_id)

	cur.execute('UPDATE categories SET name = ?, parent_category_id = ? WHERE category_id = ?', data)
	connection.commit()

def print_menu():
	''' Printing menu '''
	print('''
	---------------------------------
	|            Menu               |
	---------------------------------
	    1. Expenses
	         11. Add expence
	         12. List expenses
	         13. Delete expense
	         14. Update expense 
	         15. Display expense

	    2. Categories
	    	 21. Add category
	    	 22. List categories
	    	 23. Delete category
	    	 24. Update categories
	         ----------------
	         m. Menu
	         q. Exit
	''')


print_menu()
connect_to_db(path_to_db)

while True:

	action = input('Choose action> ')

	if action == 'q':
		connection.close()
		break

	elif action == '11':
		a = input('Enter: expense_date total_sum total_discount category_id> ')
		add_expense_to_db(a,cursor)

	elif action == '12':
		list_expenses(cursor)

	elif action == '13':
		a = input('Enter expense id> ')
		delete_expense(a,cursor)

	elif action == '14':
		ex_id_string = input('Enter expens id> ')
		a = input('Enter: expense_date total_sum total_discount category_id> ')
		update_expense(ex_id_string,a,cursor)

	elif action == '15':
		a = input('Enter expense id> ')
		read_expese(a,cursor)

	elif action == '21':
		a = input('Enter: category_name parent_category_id> ')
		add_category(a,cursor)

	elif action == '22':
		list_categories(cursor)

	elif action == '23':
		a = input('Enter category_id> ')
		delete_category(a,cursor)

	elif action == '24':
		cat_id_string = input('Enter expens id> ')
		a = input('Enter: category_name parent_category_id> ')
		update_category(cat_id_string,a,cursor)

	elif action == 'm':
		print_menu()
