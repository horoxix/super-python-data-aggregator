from lib.helper.table import *

options_dict = {
    'call_statistics': CallStatisticsTable,
    'suite_run_history': SuiteHistoryTable,
    'NULL': 'null'
}


def get_table(string):
    try:
        return options_dict.get(string, 'null')
    except KeyError:
        return options_dict.get('NULL', 'null')

