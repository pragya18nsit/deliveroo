class Configuration(object):
    def __init__(self):
        self.values = dict()

    def define_values_map(self):
        """
        INPUT: string = Value of parameter, datatype = Type of the parameter.
        OUTPUT: String indicating the matching time period for that parameter
        (e.g. which minutes the command will run).
        """
        # ranges for the different parameter values

        values = {
            'week': [i for i in range(1, 8)],
            'month': [i for i in range(1, 13)],
            'hour': [i for i in range(0, 24)],
            'day': [i for i in range(1, 32)],
            'minute': [i for i in range(0, 60)]
        }
        print (values)
        return values

    def define_months_list(self):
        # word conversions for months of the year
        months = [
            'JAN', 'FEB', 'MAR',
            'APR', 'MAY', 'JUN',
            'JUL', 'AUG', 'SEP',
            'OCT', 'NOV', 'DEC'
        ]
        return months

    def define_days_list(self):
        # word conversions for days of the week
        days = [
            'SUN', 'MON', 'TUE',
            'WED', 'THU', 'FRI',
            'SAT'
        ]
        return days
