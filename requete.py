import sqlite3

database_name = "base.db"

def execution_SQL(requete):

	connection = sqlite3.connect(database_name)
	cursor = connection.cursor()

	result = cursor.execute(requete)

	connection.commit()
	cursor.close()

	return result

def SELECT_SQL(requete):

	connection = sqlite3.connect(database_name)
	cursor = connection.cursor()

	result = cursor.execute(requete)
	result = cursor.fetchall() # pour les requetes select

	connection.commit()
	cursor.close()

	return result
