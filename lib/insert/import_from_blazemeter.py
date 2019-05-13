import requests
import uuid
from lib.insert.insert_into_table import insert_results_into_table
from lib.helper.get_table_type import get_table


# gets aggregate stats from blazemeter taurus reports for v1 endpoint
def get_aggregate(session_id):
    return requests.get('https://a.blazemeter.com/api/v4/sessions/{0}/reports/main/summary'.format(session_id),
                        auth=('e87fec7f258b03a9ad26319f',
                              '1ad08a3c6713d8a74d3fa6e053ee8bd84e11805cccf48751462398df8bb15e9b88bf84bf'))


# gets aggregate stats from blazemeter taurus reports for new v4 endpoint
def get_aggregate_v4(master_id):
    return requests.get('https://a.blazemeter.com/api/v4/masters/{0}/reports/aggregatereport/data'.format(master_id),
                        auth=('e87fec7f258b03a9ad26319f',
                              '1ad08a3c6713d8a74d3fa6e053ee8bd84e11805cccf48751462398df8bb15e9b88bf84bf'))


# inserts aggregate results from blazemeter taurus for v1 endpoint
def insert_results_from_blazemeter(session_id, database, table):
    rs = get_aggregate(session_id)
    rs_json = rs.json()
    sh_uuid = update_suite_history_table(rs_json, database)
    arg_list = []
    row_total = 0
    for result in rs_json['result']['summary']:
        for row in result:
            arg_list.append(row)
        arg_list.append(sh_uuid)
        insert_results_into_table(get_table(table), database, *arg_list)
        row_total += 1
        arg_list.clear()
    print("Inserted " + str(row_total) + " rows into the database.")


# inserts aggregate results from blazemeter taurus for new v4 endpoint
def insert_results_from_blazemeter_v4(master_id, database, table):
    rs = get_aggregate_v4(master_id)
    rs_json = rs.json()
    sh_uuid = update_suite_history_table(rs_json, database)
    arg_list = []
    row_total = 0
    for result in rs_json["result"]:
        for row in result:
            if row != 'labelId':
                arg_list.append(rs_json["result"][row_total][row])
        arg_list.append(sh_uuid)
        insert_results_into_table(get_table(table), database, *arg_list)
        row_total += 1
        arg_list.clear()
    print("Inserted " + str(row_total) + " rows into the database.")


# updates suite_history_table with entire run information, once per import.
def update_suite_history_table(json_data, database):
    suite_history_uuid = uuid.uuid4().hex
    suite_history_args = [suite_history_uuid,
                          int(json_data["result"][0]["avgResponseTime"]),
                          int(json_data["result"][0]["samples"]),
                          int(json_data["result"][0]["errorsRate"]),
                          int(json_data["result"][0]["errorsCount"])]
    insert_results_into_table(get_table('suite_run_history'), database, *suite_history_args)
    print("Inserted suite_id " + str(suite_history_uuid) + " into the database.")
    return suite_history_uuid
