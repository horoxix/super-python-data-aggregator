from pyquibase.pyquibase import Pyquibase
from lib.helper import get_db_info, get_db_type
import sys


def run_liquibase_setup():
    pyquibase = Pyquibase.postgresql(
        host=get_db_info.get_value_from_json(get_db_type.PostgreSQL, 'connection_info', 'host'),
        port=get_db_info.get_value_from_json(get_db_type.PostgreSQL, 'connection_info', 'port'),
        db_name=get_db_info.get_value_from_json(get_db_type.PostgreSQL, 'connection_info', 'database'),
        username=get_db_info.get_value_from_json(get_db_type.PostgreSQL, 'connection_info', 'user'),
        password=get_db_info.get_value_from_json(get_db_type.PostgreSQL, 'connection_info', 'password'),
        change_log_file=sys.path[0] + '\\' + get_db_info.get_value_from_json(get_db_type.PostgreSQL, 'config',
                                                                             'changelog')
    )
    pyquibase.update()


if __name__ == '__main__':
    run_liquibase_setup()

