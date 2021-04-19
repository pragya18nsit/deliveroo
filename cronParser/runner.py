from cronParser.utility import Utility


class Runner(object):
    def __init__(self):
        self.cron_str = ""

    def describe_cron(self, cron_str):
        """
        INPUT: cron_str = The input string containing the entire cron string from
        the user.
        OUTPUT: A formatted string containing the minute, hour, day, month,
        weekday and command that will run.
        """

        minute, hour, day, month, week, cmd = cron_str.split(" ")
        utility_obj = Utility()

        return '\n'.join([
            "Minutes: {}".format(utility_obj.define_string(minute, 'minute')),
            "Hours: {}".format(utility_obj.define_string(hour, 'hour')),
            "Day of month: {}".format(utility_obj.define_string(day, 'day')),
            "Month: {}".format(utility_obj.define_string(month, 'month')),
            "Day of Week: {}".format(utility_obj.define_string(week, 'week')),
            "Command: {}".format(cmd)
        ])
