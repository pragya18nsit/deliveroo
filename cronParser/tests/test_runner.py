#!/usr/bin/python3

import unittest
from cronParser.runner import Runner


class TestRunner(unittest.TestCase):
    '''Testing the Main file'''
    def setUp(self):
        self.runner_obj = Runner()

    def test_runner_describe_cron_success(self):
        output_string = self.runner_obj.describe_cron("*/15 0 1,15 * 1-5 /usr/bin/find")
        expected_output = "Minutes: 0 15 30 45\nHours: 0\nDay of month: 1 15\nMonth: 1 2 3 4 5 6 7 8 9 10 11 12\nDay of Week: 1 2 3 4 5\nCommand: /usr/bin/find"
        self.assertEqual(expected_output, output_string)

    def test_runner_describe_cron_fail(self):
        runner_obj = Runner()

        self.assertRaises(ValueError, runner_obj.describe_cron, "*/15 0 1,15 1-5 /usr/bin/find")


if __name__ == '__main__':
    unittest.main()
