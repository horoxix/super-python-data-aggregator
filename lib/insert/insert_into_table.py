from lib.helper import get_db_info
import mysql.connector


# inserts results into db table based on table, database type, and values
def insert_results_into_table(table, database, *args):
    connection_config_dict = get_db_info.get_values_from_json(False, database.db_type)
    connection = None
    cursor = None

    try:
        connect_string = database.connection
        connection = connect_string.connect(**connection_config_dict)
        cursor = connection.cursor()
        sql_insert_query = table.insert_string
        tuple_list = []

        for arg in args:
            tuple_list.append(arg)

        sql_tuple = tuple(tuple_list)

        cursor.execute(sql_insert_query, sql_tuple)
        connection.commit()
        print("Record inserted successfully into the " + table.table_name + " table")

    except Exception as error:
        connection.rollback()
        print("Failed to insert into " + table.table_name + " table {}".format(error))

    finally:
        # closing database connection.
        if connection is not None:
            cursor.close()
            connection.close()
