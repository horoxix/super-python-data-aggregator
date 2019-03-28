import json
from pathlib import Path

base_path = Path(__file__).parent
file_path = (base_path / "../db_info.json").resolve()


# gathers database connection information from db_info.json
def get_values_from_json(creating, db_type):
    with open(file_path) as dbci:
        data = json.load(dbci)
        connection_info = {}

        # 'creating' boolean is only used for the initial CREATE DATABASE query
        if creating:
            connection_info = {
                'host': data[db_type]["connection_info"]["host"],
                'user': data[db_type]["connection_info"]["user"],
                'password': data[db_type]["connection_info"]["password"]
            }
        else:
            for item in data[db_type]["connection_info"]:
                connection_info[item] = data[db_type]["connection_info"][item]
        return connection_info


# gets data from json for specific connection property
def get_value_from_json(db_type, key, value):
    with open(file_path) as dbci:
        data = json.load(dbci)
        return data[db_type.db_type][key][value]

