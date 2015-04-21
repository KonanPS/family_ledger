# insert data via comand line 

import sqlite3
import os.path

db_name = 'expenses_by_category.db'
path_to_db = os.path.dirname(os.path.abspath(__file__)) + '/db/' + db_name
print('path to db: ', path_to_db)

def add_expense_to_db(string):
	''' Get data for expense table 
		Date, Total summ, Total discount 
		as a string with space as separator

		Connects to db and inserts data to expense table
		commit changes and close connection'''

	data = string.split()
	try:
		connection = sqlite3.connect(path_to_db)
		cursor = connection.cursor()
		cursor.execute('''PRAGMA foreign_keys = ON''') # enable foreign keys
		cursor.execute("""INSERT INTO expense (expense_date, total_sum, total_discount, category_id) VALUES (?,?,?,?)""", data)
		connection.commit()
		connection.close()
	except sqlite3.IntegrityError:
		print('No such category. Please add it')


def list_expenses():
	''' Print records in expense table'''

	connection = sqlite3.connect(path_to_db)
	cursor = connection.cursor()
	cursor.execute('''PRAGMA foreign_keys = ON''') # enable foreign keys
	cursor.execute("""SELECT * FROM expense""")
	res = cursor.fetchall()
	for r in res:
		print(r)
	connection.close()

def delete_expense(ex_id):
	''' Delete expense from db via expense_id'''

	connection = sqlite3.connect(path_to_db)
	cursor = connection.cursor()
	cursor.execute('''PRAGMA foreign_keys = ON''') # enable foreign keys
	cursor.execute('''DELETE FROM expense WHERE expense_id = ?''', ex_id)
	connection.commit()
	connection.close()

def update_expense(ex_id,d_str):
	'''Updates expense via expense_id and new data'''

	data = d_str.split()
	data.append(ex_id)

	connection = sqlite3.connect(path_to_db)
	cur = connection.cursor()
	cur.execute('''PRAGMA foreign_keys = ON''') # enable foreign keys
	cur.execute('UPDATE expense SET expense_date = ?, total_sum = ?, total_discount = ?, category_id = ? WHERE expense_id = ?', data)
	connection.commit()
	connection.close()

def read_expese(ex_id_string):
	''' Select expense record via expense_id '''

	connection = sqlite3.connect(path_to_db)
	cur = connection.cursor()
	cur.execute('''PRAGMA foreign_keys = ON''') # enable foreign keys
	cur.execute("SELECT * FROM expense WHERE expense_id = ?",ex_id_string)
	r = cur.fetchall()
	print(r)
	connection.close()

def add_category(data_str):
	''' Add category'''

	data = data_str.split()
	connection = sqlite3.connect(path_to_db)
	cur = connection.cursor()
	cur.execute('''PRAGMA foreign_keys = ON''') # enable foreign keys
	cur.execute('''INSERT INTO categories (name, parent_category_id) VALUES (?, ?)''', data)
	connection.commit()
	connection.close()

def list_categories():
	''' Print records in categories table'''

	connection = sqlite3.connect(path_to_db)
	cursor = connection.cursor()
	cursor.execute('''PRAGMA foreign_keys = ON''') # enable foreign keys
	cursor.execute("""SELECT * FROM categories""")
	res = cursor.fetchall()
	for r in res:
		print(r)
	connection.close()

def delete_category(cat_id):
	''' Delete record from categories table via category_id'''

	connection = sqlite3.connect(path_to_db)
	cursor = connection.cursor()
	cursor.execute('''PRAGMA foreign_keys = ON''') # enable foreign keys
	cursor.execute('''DELETE FROM categories WHERE category_id = ?''', cat_id)
	connection.commit()
	connection.close()

def update_category(cat_id, d_str):
	'''Updates category via category_id and new data'''

	data = d_str.split()
	data.append(cat_id)

	connection = sqlite3.connect(path_to_db)
	cur = connection.cursor()
	cur.execute('''PRAGMA foreign_keys = ON''') # enable foreign keys
	cur.execute('UPDATE categories SET name = ?, parent_category_id = ? WHERE category_id = ?', data)
	connection.commit()
	connection.close()

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

while True:

	action = input('Choose action> ')

	if action == 'q':
		break

	elif action == '11':
		a = input('Enter: expense_date total_sum total_discount category_id> ')
		add_expense_to_db(a)

	elif action == '12':
		list_expenses()

	elif action == '13':
		a = input('Enter expense id> ')
		delete_expense(a)

	elif action == '14':
		ex_id_string = input('Enter expens id> ')
		a = input('Enter: expense_date total_sum total_discount category_id> ')
		update_expense(ex_id_string,a)

	elif action == '15':
		a = input('Enter expense id> ')
		read_expese(a)

	elif action == '21':
		a = input('Enter: category_name parent_category_id> ')
		add_category(a)

	elif action == '22':
		list_categories()

	elif action == '23':
		a = input('Enter category_id> ')
		delete_category(a)

	elif action == '24':
		cat_id_string = input('Enter expens id> ')
		a = input('Enter: category_name parent_category_id> ')
		update_category(cat_id_string,a)

	elif action == 'm':
		print_menu()
