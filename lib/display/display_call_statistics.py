import pandas as pd
import plotly
import plotly.graph_objs as go
from lib.helper import get_db_info, table
from mysql.connector import Error


def get_display_latest_call_statistics(database):
    connection_config_dict = get_db_info.get_values_from_json(False, database.db_type)
    connection = None
    cursor = None
    try:
        connect_string = database.connection
        connection = connect_string.connect(**connection_config_dict)
        cursor = connection.cursor()
        display_query = table.CallStatisticsTable.display_query

        cursor.execute(display_query)
        rows = cursor.fetchall()
        df = pd.DataFrame([[ij for ij in i] for i in rows])
        df.rename(columns={0: 'label', 1: 'average', 2: 'response_time', 3: 'error_count', 4: 'error_rate',
                           5: 'suite_run_history_id'},
                  inplace=True)
        df = df.sort_values(['error_rate'], ascending=[1])

        trace1 = go.Bar(
            x=df['label'],
            y=df['error_rate'],
            name='Bar'
        )

        layout = go.Layout(
            title='Call Statistics History',
            xaxis=dict(title='Call Label'),
            yaxis=dict(title='Error Rate'),
        )
        data = [trace1]
        fig = go.Figure(data=data, layout=layout)
        # connection.commit()
        plotly.offline.plot(fig, filename='call_statistics_chart.html')

    except Error as error:
        connection.rollback()

    finally:
        # closing database connection.
        if connection is not None:
            cursor.close()
            connection.close()
