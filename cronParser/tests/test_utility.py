#!/usr/bin/python3

import unittest
from cronParser.utility import Utility


class TestUtility(unittest.TestCase):
    '''Testing the Utility file'''

    def setUp(self):
        self.utility_obj = Utility()

    def test_handle_last(self):
        days = [
            'SUN', 'MON', 'TUE',
            'WED', 'THU', 'FRI',
            'SAT'
        ]
        output_string = self.utility_obj.handle_last("2L", "week", days )
        self.assertEqual("Last MON of the Month", output_string)

    def test_handle_range_nums(self):
        days = [
            'SUN', 'MON', 'TUE',
            'WED', 'THU', 'FRI',
            'SAT'
        ]
        output_string = self.utility_obj.handle_range("5-15", days, "days")
        self.assertEqual("5 6 7 8 9 10 11 12 13 14 15", output_string)

    def test_handle_range_strings(self):
        days = [
            'SUN', 'MON', 'TUE',
            'WED', 'THU', 'FRI',
            'SAT'
        ]
        output_string = self.utility_obj.handle_range("SUN-WED", days, "days")
        self.assertEqual("SUN MON TUE WED", output_string)


    def test_handle_intervals_with_star(self):
        days = [i for i in range(1, 32)]
        output_string = self.utility_obj.handle_intervals("*/2", days, "day")
        self.assertEqual("2 4 6 8 10 12 14 16 18 20 22 24 26 28 30", output_string)

    def test_handle_intervals_with_integers(self):
        days = [i for i in range(1, 32)]
        output_string = self.utility_obj.handle_intervals("1/10", days, "day")
        self.assertEqual("10 20 30", output_string)

    def test_handle_weekday(self):
        output_string = self.utility_obj.handle_weekday("5W", "day")
        self.assertEqual("Nearest weekday to day 5 of the month", output_string)

    def test_handle_lists(self):
        days = [i for i in range(1, 32)]
        output_string = self.utility_obj.handle_lists("14,18", days, "day")
        self.assertEqual("14 18", output_string)

    def test_handle_lists(self):
        days = [
            'SUN', 'MON', 'TUE',
            'WED', 'THU', 'FRI',
            'SAT'
        ]
        output_string = self.utility_obj.handle_lists("SUN,WED", days, "day", days)
        self.assertEqual("SUN WED", output_string)

if __name__ == '__main__':
    unittest.main()
