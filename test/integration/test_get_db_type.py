import unittest
from lib.helper import get_db_type


class TestGetTable(unittest.TestCase):
    def setUp(self):
        self.DB = get_db_type.MySQL
        self.STRING = "MySQL"

    def test_get_db_type(self):
        self.assertEqual(get_db_type.get_database_type(self.STRING), self.DB)

    def test_get_invalid_db_type(self):
        self.assertEqual(get_db_type.get_database_type("NONE"), 'null')

    def test_db_data(self):
        test_db = get_db_type.get_database_type(self.STRING)
        self.assertEqual(test_db.db_type,  self.DB.db_type)
        self.assertEqual(test_db.connection,  self.DB.connection)
        self.assertEqual(test_db.index,  self.DB.index)
        self.assertNotEqual(test_db.db_type, 'PostgreSQL')
