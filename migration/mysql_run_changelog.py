from pyquibase.pyquibase import Pyquibase
from lib.helper import get_db_info, get_db_type
import os


def run_liquibase_setup():
    pyquibase = Pyquibase.mysql(
        host=get_db_info.get_value_from_json(get_db_type.MySQL, 'connection_info', 'host'),
        port=get_db_info.get_value_from_json(get_db_type.MySQL, 'connection_info', 'port'),
        db_name=get_db_info.get_value_from_json(get_db_type.MySQL, 'connection_info', 'database'),
        username=get_db_info.get_value_from_json(get_db_type.MySQL, 'connection_info', 'user'),
        password=get_db_info.get_value_from_json(get_db_type.MySQL, 'connection_info', 'password'),
        change_log_file=str(os.path.dirname(__file__) + "\\" + str(get_db_info.get_value_from_json(get_db_type.MySQL,
                                                                                                   'config',
                                                                                                   'changelog')))
    )
    pyquibase.update()


if __name__ == '__main__':
    run_liquibase_setup()
