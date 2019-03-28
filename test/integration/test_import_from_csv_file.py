import unittest
from unittest import mock
from io import StringIO


class TestCSVImport(unittest.TestCase):
    def setUp(self):
        self.csv_file = StringIO("labelId,labelName,samples,avgResponseTime,90line,95line,99line,minResponseTime, "
                                 "maxResponseTime,avgLatency,geoMeanResponseTime,stDev,duration,avgBytes,"
                                 "avgThroughput,medianResponseTime,errorsCount,errorsRate,hasLabelPassedThresholds\n"
                                 "ALL,ALL,6695,578,1193,1592,2965,0,60063,537,0,0,225,41.295,29.756,0,126,1.882\n"
                                 "7030fd862d4481cea1508d42f437b4fa,CAS GET Ticket Info,232,203,390,525,729,31,764,189,"
                                 "0,0,225,1.396,1.031,0,0,0\n"
                                 )

    def test_update_suite_run_history_table(self):
        with mock.patch('ui.import_from_csv_file.update_suite_history_table') as mocked_id:
            self.assertIsNotNone(mocked_id)
