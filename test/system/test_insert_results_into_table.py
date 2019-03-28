import unittest
from unittest import mock
from lib.insert import insert_into_table as insert
from lib.helper import get_db_type as db, table as table


class TestInsertResultsIntoTable(unittest.TestCase):
    def setUp(self):
        self.ARGS = ["CAS GET Ticket Info", 232, 203, 390, 525, 729, 31, 764,
                     189, 0, 0, 225, 1.396, 1.031, 0, 0, 0]
        self.DATABASE = db.MySQL
        self.TABLE = table.CallStatisticsTable

    @mock.patch('ui.insert_into_table.mysql.connector.connect')
    def test_insert_results_into_table(self, mock_connect):
        insert.insert_results_into_table(self.TABLE, self.DATABASE, self.ARGS)
        mock_connect.assert_called()
        mock_connect.assert_called_with(
            autocommit='True',
            database='spyda',
            host='127.0.0.1',
            password='spydapassword',
            pool_size=5,
            user='root'
            )
