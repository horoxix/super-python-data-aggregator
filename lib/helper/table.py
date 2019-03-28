class Table:
    table_name = 'Table'
    column_count = 0


class CallStatisticsTable(Table):
    table_name = "call_statistics"
    column_count = 18
    insert_string = """ INSERT INTO call_statistics
                                  (label,samples,average_response_time,ninety_percent,ninety_five_percent,
                                  ninety_nine_percent,minimum_response_time,maximum_response_time,
                                  average_latency,geo_mean_response_time,standard_deviation,duration_ms,
                                  average_bytes,average_throughput,median_response_time,error_count,error_rate,
                                   suite_run_history_id) 
                                  VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    display_query = """ SELECT label, samples, average_response_time, error_count, error_rate, suite_run_history_id
                                    FROM call_statistics
                                    LIMIT 42
                            """


class SuiteHistoryTable(Table):
    table_name = "suite_run_history"
    column_count = 5
    insert_string = """ INSERT INTO SUITE_RUN_HISTORY
                                  (suite_run_history_id,average_response_time,total_samples,error_rate,error_count) 
                                  VALUES (%s,%s,%s,%s,%s)"""
    display_query = """ SELECT * FROM suite_run_history
                            """