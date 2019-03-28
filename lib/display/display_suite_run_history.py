import pandas as pd
import plotly
import plotly.graph_objs as go
from lib.helper import get_db_info, table
from mysql.connector import Error


def get_display_suite_run_history(database):
    connection_config_dict = get_db_info.get_values_from_json(False, database.db_type)
    connection = None
    cursor = None
    try:
        connect_string = database.connection
        connection = connect_string.connect(**connection_config_dict)
        cursor = connection.cursor()
        display_query = table.SuiteHistoryTable.display_query

        cursor.execute(display_query)
        rows = cursor.fetchall()
        df = pd.DataFrame([[ij for ij in i] for i in rows])
        df.rename(columns={0: 'key', 1: 'id', 2: 'date', 3: 'avg', 4: 'total', 5: 'error_rate', 6: 'error_count'},
                  inplace=True)
        df = df.sort_values(['date'], ascending=[1])

        trace1 = go.Scatter(
            x=df['date'],
            y=df['avg'],
            mode='lines+markers',
            name='Scatter'
        )

        layout = go.Layout(
            title='Suite History',
            xaxis=dict(title='Date'),
            yaxis=dict(title='Average Response Time'),
        )
        data = [trace1]
        fig = go.Figure(data=data, layout=layout)
        # connection.commit()
        plotly.offline.plot(fig, filename='suite_run_history_chart.html')

    except Error as error:
        connection.rollback()

    finally:
        # closing database connection.
        if connection is not None:
            cursor.close()
            connection.close()
