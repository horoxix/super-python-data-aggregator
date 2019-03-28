import mysql.connector
import psycopg2


class DatabaseType:
    db_type = ""
    connection = None


class MySQL(DatabaseType):
    db_type = "MySQL"
    index = 0
    connection = mysql.connector


class PostgreSQL(DatabaseType):
    db_type = "PostgreSQL"
    index = 1
    connection = psycopg2


options_dict = {
    'MySQL': MySQL,
    'PostgreSQL': PostgreSQL,
    'NULL': 'null'
}


def get_database_type(string):
    try:
        return options_dict.get(string, 'null')
    except KeyError:
        return options_dict.get('NULL', 'null')
