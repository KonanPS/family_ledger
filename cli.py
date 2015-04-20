# insert data via comand line 

import sqlite3

def add_expense_to_db(string):
	""" Get data for expense table 
		Date, Total summ, Total discount 
		as a string with space as separator

		Connects to db and inserts data to expense table
		commit changes and close connection
	"""
	data = string.split()
	print(data)

	connection = sqlite3.connect('expenses_by_category.db')
	cursor = connection.cursor()
	cursor.execute("""INSERT INTO expense (expense_date, total_sum, total_discount, category_id) VALUES (?,?,?,?)""", data)
	connection.commit()
	connection.close()

def list_expenses():
	''' Print list with records in expense table'''

	connection = sqlite3.connect('expenses_by_category.db')
	cursor = connection.cursor()
	cursor.execute("""SELECT * FROM expense""")
	res = cursor.fetchall()
	for r in res:
		print(r)
	connection.close()

def delete_expense(ex_id):
	''' Delete expense from db via expense_id'''
	connection = sqlite3.connect('expenses_by_category.db')
	cursor = connection.cursor()
	cursor.execute('''DELETE FROM expense WHERE expense_id = ?''', ex_id)
	connection.commit()
	connection.close()

def update_expense(ex_id,d_str):
	'''Updates expense via expense_id and new data'''

	data = d_str.split()
	data.append(ex_id)

	connection = sqlite3.connect('expenses_by_category.db')
	cur = connection.cursor()
	cur.execute('UPDATE expense SET expense_date = ?, total_sum = ?, total_discount = ?, category_id = ? WHERE expense_id = ?', data)
	connection.commit()
	connection.close()

def read_expese(ex_id_string):
	""" Select expense record via expense_id """

	connection = sqlite3.connect('expenses_by_category.db')
	cur = connection.cursor()
	cur.execute("SELECT * FROM expense WHERE expense_id = ?",ex_id_string)
	r = cur.fetchall()
	print(r)
	connection.close()

def print_menu():
	''' Printing menu '''
	print('''
	---------------------------------
	|            Menu               |
	---------------------------------
	         1. Add expence
	         2. List expenses
	         3. Delete expense
	         4. Update expense 
	         5. Display expense
	         ----------------
	         m. Menu
	         q. Exit
	''')


print_menu()

while True:

	action = input('Choose action> ')

	if action == 'q':
		break
	elif action == '1':
		a = input('Enter: expense_date total_sum total_discount category_id> ')
		add_expense_to_db(a)
	elif action == '2':
		list_expenses()
	elif action == '3':
		a = input('Enter expense id> ')
		delete_expense(a)
	elif action == '4':
		ex_id_string = int(input('Enter expens id> '))
		a = input('Enter: expense_date total_sum total_discount category_id> ')
		update_expense(ex_id_string,a)
	elif action == '5':
		a = input('Enter expense id> ')
		read_expese(a)
	elif action == 'm':
		print_menu()
