import sqlite3
import os.path

db_name = 'expenses_by_category.db'
path_to_db = os.path.dirname(os.path.abspath(__file__)) + '/' + db_name

#sql statements
foreign_key_availavle = '''PRAGMA foreign_keys = ON'''

expense_table = '''CREATE TABLE IF NOT EXISTS expense 
	(expense_id INTEGER PRIMARY KEY, 
	expense_date INTEGER,
	total_sum INTEGER,
	total_discount INTEGER,
	category_id INTEGER,
	FOREIGN KEY (category_id) REFERENCES categories(category_id))'''

items_table = '''CREATE TABLE IF NOT EXISTS items
	(item_ id INTEGER PRIMARY KEY, 
	expense_id INTEGER,
	category_id INTEGER,
	total_price INTEGER,
	FOREIGN KEY (expense_id) REFERENCES expense(expense_id),
	FOREIGN KEY (category_id) REFERENCES categories(category_id))'''

category_table = '''CREATE TABLE IF NOT EXISTS categories 
	(category_id INTEGER PRIMARY KEY, 
	name TEXT, 
	parent_category_id INTEGER,
	FOREIGN KEY (parent_category_id) REFERENCES categories(category_id))'''

connection = sqlite3.connect(path_to_db)

cursor = connection.cursor()

cursor.execute(foreign_key_availavle)

cursor.execute(expense_table)

cursor.execute(items_table)

cursor.execute(category_table)

connection.commit()

connection.close()