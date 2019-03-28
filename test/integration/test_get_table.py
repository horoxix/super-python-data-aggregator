import unittest
from lib.helper import get_table_type, table


class TestGetTable(unittest.TestCase):
    def setUp(self):
        self.TABLE = table.CallStatisticsTable
        self.STRING = "call_statistics"

    def test_get_table(self):
        self.assertEqual(get_table_type.get_table(self.STRING), self.TABLE)

    def test_get_invalid_table(self):
        self.assertEqual(get_table_type.get_table("NONE"), 'null')

    def test_table_data(self):
        test_table = get_table_type.get_table(self.STRING)
        self.assertEqual(test_table.column_count,  self.TABLE.column_count)
        self.assertEqual(test_table.insert_string,  self.TABLE.insert_string)
        self.assertEqual(test_table.table_name,  self.TABLE.table_name)
