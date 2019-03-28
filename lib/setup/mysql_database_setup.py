import mysql.connector
from lib.helper import get_db_info as dbci, get_db_type


def create_tables():
    """ create tables in the MySQL database"""
    commands = (
        """ CREATE TABLE `suite_run_history` (
                `suite_run_history_key` INT(11) NOT NULL AUTO_INCREMENT,
                `suite_run_history_id` VARCHAR(50) NOT NULL,
                `run_date` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
                `average_response_time` INT(64) NULL DEFAULT NULL,
                `total_samples` INT(64) NULL DEFAULT NULL,
                `error_rate` FLOAT NULL DEFAULT NULL,
                `error_count` INT(64) NULL DEFAULT NULL,
                PRIMARY KEY (`suite_run_history_key`),
                UNIQUE INDEX `ID` (`suite_run_history_id`)
                )
                COLLATE='utf8_general_ci'
                ENGINE=InnoDB
                AUTO_INCREMENT=1;
        """,
        """
           CREATE TABLE `call_statistics` (
                `call_statistics_key` INT(11) NOT NULL AUTO_INCREMENT,
                `date` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                `label` TEXT NULL,
                `samples` INT(11) NULL DEFAULT NULL,
                `average_response_time` INT(11) NULL DEFAULT NULL,
                `ninety_percent` INT(11) NULL DEFAULT NULL,
                `ninety_five_percent` INT(11) NULL DEFAULT NULL,
                `ninety_nine_percent` INT(11) NULL DEFAULT NULL,
                `minimum_response_time` INT(11) NULL DEFAULT NULL,
                `maximum_response_time` INT(11) NULL DEFAULT NULL,
                `average_latency` FLOAT NULL DEFAULT NULL,
                `geo_mean_response_time` SMALLINT(6) NULL DEFAULT NULL,
                `standard_deviation` SMALLINT(6) NULL DEFAULT NULL,
                `duration_ms` INT(11) NULL DEFAULT NULL,
                `average_bytes` FLOAT NULL DEFAULT NULL,
                `average_throughput` FLOAT NULL DEFAULT NULL,
                `median_response_time` INT(11) NULL DEFAULT NULL,
                `error_count` INT(11) NULL DEFAULT NULL,
                `error_rate` FLOAT NULL DEFAULT NULL,
                `has_passed_thresholds` BIT(1) NULL DEFAULT NULL,
                `suite_run_history_id` VARCHAR(50) NOT NULL,
                PRIMARY KEY (`call_statistics_key`),
                INDEX `suite_run_history_id` (`suite_run_history_id`),
                CONSTRAINT `call_statistics_ibfk_1` FOREIGN KEY (`suite_run_history_id`) REFERENCES `suite_run_history` 
                (`suite_run_history_id`)
                )
                COLLATE='utf8_general_ci'
                ENGINE=InnoDB
                AUTO_INCREMENT=1;
        """)
    conn = None
    try:
        # gathers connection parameters
        database = get_db_type.MySQL
        connection_config_dict = dbci.get_values_from_json(False, database.db_type)
        # connect to the MySQL server
        conn = mysql.connector.connect(**connection_config_dict)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
            conn.commit()
        # close communication with the database server
        cur.close()
        # commit any final changes
        conn.commit()
    except (Exception, mysql.connector.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_tables()
