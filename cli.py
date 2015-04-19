# insert data via comand line 

import sqlite3

def add_expence_to_db(string):
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

	
# printing menu
print('''
---------------------------------
|            Menu               |
---------------------------------
         1. Add expence
         2. List expenses
         ----------------
         q. Exit
''')

while True:

	action = input('Choose action> ')
	if action == 'q':
		break
	elif action == '1':
		a = input('enter: expense_date total_sum total_discount category_id> ')
		add_expence_to_db(a)
	elif action == '2':
		list_expenses()