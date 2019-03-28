import mysql.connector
from lib.helper import get_db_info as dbci, get_db_type


def create_database():
    database = get_db_type.MySQL
    connection_config_dict = dbci.get_values_from_json(True, database.db_type)
    connection = mysql.connector.connect(**connection_config_dict)

    cursor = connection.cursor()

    cursor.execute("CREATE DATABASE spyda")


def drop_database():
    database = get_db_type.MySQL
    connection_config_dict = dbci.get_values_from_json(True, database.db_type)
    connection = mysql.connector.connect(**connection_config_dict)

    cursor = connection.cursor()

    cursor.execute("DROP DATABASE spyda")


if __name__ == '__main__':
    create_database()
