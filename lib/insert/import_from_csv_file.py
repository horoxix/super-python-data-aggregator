import pandas as pd
import uuid
from lib.insert.insert_into_table import insert_results_into_table
from lib.helper.get_table_type import get_table


# gathers data from csv file and calls 'insert_results_into_table' with information
def insert_data_from_csv(csv_file, database, table):
    csv_data = pd.read_csv(csv_file)
    sh_uuid = update_suite_history_table(csv_data, database)
    csv_data.drop([0])
    arg_list = []
    row_total = 0
    for row in csv_data.itertuples(index=False):
        for col in range(1, get_table(table).column_count, 1):
            arg_list.append(row[col])
        arg_list.append(sh_uuid)
        insert_results_into_table(get_table(table), database, *arg_list)
        row_total += 1
        arg_list.clear()
    print("Inserted " + str(row_total) + " rows into the database.")


# updates suite_history_table with entire run information, once per import.
def update_suite_history_table(csv_data, database):
    suite_history_uuid = uuid.uuid4().hex
    suite_history_args = [suite_history_uuid,
                          int(csv_data['avgResponseTime'].iloc[0]),
                          int(csv_data['samples'].iloc[0]),
                          int(csv_data['errorsRate'].iloc[0]),
                          int(csv_data['errorsCount'].iloc[0])]
    insert_results_into_table(get_table('suite_run_history'), database, *suite_history_args)
    print("Inserted suite_id " + str(suite_history_uuid) + " into the database.")
    return suite_history_uuid
