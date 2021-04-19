#!/usr/bin/python3

import unittest

from cronParser.configuration import Configuration


class TestConfiguration(unittest.TestCase):
    '''Testing the Main file'''
    def setUp(self):
        self.config_obj = Configuration()

    def test_config_define_values_map(self):

        output_string = self.config_obj.define_values_map()
        self.assertEqual(7, len(output_string['week']))
        self.assertEqual(12, len(output_string['month']))
        self.assertEqual(24, len(output_string['hour']))
        self.assertEqual(31, len(output_string['day']))
        self.assertEqual(60, len(output_string['minute']))

    def test_config_define_months_list(self):
        output_string = self.config_obj.define_months_list()
        expected_output = [
            'JAN', 'FEB', 'MAR',
            'APR', 'MAY', 'JUN',
            'JUL', 'AUG', 'SEP',
            'OCT', 'NOV', 'DEC'
        ]
        self.assertEqual(expected_output, output_string)

    def test_config_define_days_list(self):
        output_string = self.config_obj.define_days_list()
        expected_output = [
            'SUN', 'MON', 'TUE',
            'WED', 'THU', 'FRI',
            'SAT'
        ]
        self.assertEqual(expected_output, output_string)


if __name__ == '__main__':
    unittest.main()
