import psycopg2
from lib.helper import get_db_info as dbci, get_db_type


def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """ CREATE TABLE suite_run_history (
                suite_run_history_key SERIAL PRIMARY KEY,
                suite_run_history_id character varying(50) COLLATE pg_catalog."default" NOT NULL,
                run_date timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
                average_response_time integer,
                total_samples integer,
                error_rate double precision,
                error_count integer,
                CONSTRAINT "suite_run_history_id UNIQUE" UNIQUE (suite_run_history_id)
                )
        """,
        """
           CREATE TABLE call_statistics (
                call_statistics_key SERIAL PRIMARY KEY,
                date timestamp with time zone NOT NULL DEFAULT CURRENT_TIMESTAMP,
                label text COLLATE pg_catalog."default",
                samples integer,
                average_response_time integer,
                ninety_percent integer,
                ninety_five_percent integer,
                ninety_nine_percent integer,
                minimum_response_time integer,
                maximum_response_time integer,
                average_latency double precision,
                geo_mean_response_time smallint,
                standard_deviation smallint,
                duration_ms integer,
                average_bytes double precision,
                average_throughput double precision,
                median_response_time integer,
                error_count integer,
                error_rate double precision,
                has_passed_thresholds bit(1) DEFAULT NULL::"bit",
                suite_run_history_id character varying(50) COLLATE pg_catalog."default" NOT NULL,
                CONSTRAINT suite_run_history_id FOREIGN KEY (suite_run_history_id)
                    REFERENCES public.suite_run_history (suite_run_history_id) MATCH SIMPLE
                    ON UPDATE RESTRICT
                    ON DELETE RESTRICT
                )
        """)
    conn = None
    try:
        # gathers the connection parameters
        database = get_db_type.PostgreSQL
        connection_config_dict = dbci.get_values_from_json(False, database.db_type)
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**connection_config_dict)
        conn.autocommit = True
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
            conn.commit()
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_tables()
