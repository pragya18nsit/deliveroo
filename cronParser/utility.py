from cronParser.configuration import Configuration


class Utility(object):
    def __init__(self):
        self.datatype = ""

    def define_string(self, string, datatype):
        """
        INPUT: string = Value of parameter, datatype = Type of the parameter.
        OUTPUT: String indicating the matching time period for that parameter
        (e.g. which minutes the command will run).
        """
        configuration_object = Configuration()
        values = configuration_object.define_values_map()
        days = configuration_object.define_days_list()
        months = configuration_object.define_months_list()

        # return all values in range if * selector is used
        if string == "*":
            return ' '.join(map(str, values[datatype]))

        if string == "?":
            return 'Not Specified'

        # handle last operator
        if "L" in string:
            return self.handle_last(string, datatype, days)


        # handle ranges
        if "-" in string:
            values = days if datatype == "week" else months
            return self.handle_range(string, values, datatype)

        # handle intervals
        if "/" in string:
            return self.handle_intervals(string, values[datatype], datatype)

        # handle lists
        if "," in string:
            if datatype == 'month' or datatype == 'week':
                sub = days if datatype == "week" else months
                return self.handle_lists(string, values[datatype], datatype, sub)
            else:
                return self.handle_lists(string, values[datatype], datatype)


        # handle weekday operator
        if "W" in string:
            return self.handle_weekday(string, datatype)

        return string

    def handle_range(self, string, values, datatype):
        """
        INPUT: string = Value of parameter, values = Array of possible values for
        parameter, datatype = Type of the parameter.
        OUTPUT: String of all values in the range given. If word form was used
        (e.g. JAN instead of 1), it returns a word-formatted range.
        """

        # 5-2
        # 1,2,5,6,7
        output = None
        start, end = string.split('-')
        try:
            start, end = int(start), int(end)
            end_value = values[-1]
            print(values.index(end_value))

            if start > end:
                startoutput = ' '.join(map(str, [i for i in range(1, end + 1)]))
                endoutput = ' '.join(map(str, [i for i in range(start, values.index(end_value) + 2)]))
                output = startoutput + ' '+ endoutput
                print(output)

        except ValueError:
            try:
                start, end = values.index(start), values.index(end)
                return ' '.join(values[start:end + 1])
            except ValueError:
                raise Exception(
                    '{} input combination is not valid. Please use either string or number syntax.'.format(datatype))

        if output is None:
            output = ' '.join(map(str, [i for i in range(start, end + 1)]))
        return output

    def handle_intervals(self, string, values, datatype):
        """
        INPUT: string = Value of parameter, values = Array of possible value for
        parameter.
        OUTPUT: String of all the values matching the specified interval in the
        possible range.
        """

        first, second = string.split("/")

        if first == "*":
            return ' '.join(
                map(str, [i for i in values
                          if i % int(second) == 0])
            )

        if first.isnumeric() is not True or second.isnumeric() is not True:
            raise Exception('Invalid input for {}'.format(datatype))
        else:
            return ' '.join(
                map(str, [i for i in range(int(first), values[-1])
                          if i % int(second) == 0])
            )

    def handle_lists(self, string, values, datatype, sub=None):
        """
        INPUT: string = Value of parameter, values = Array of possible value for
        parameter, datatype = Type of the parameter, sub = An optional parameter
        used when there are 2 possible input formats (e.g. JAN vs 1). We also
        verify that formats (i.e. JAN vs 1) are not mixed.
        OUTPUT: String of all the values listed in the input, if they are part
        of the range of possible values for that parameter.
        """

        inputs = string.split(',')
        type_value = None
        v = None
        for i in inputs:
            try:
                v = int(i)
            except ValueError:
                v = i

            if type_value is None:
                type_value = type(v)
            elif type_value != type(v):
                raise Exception(
                    '{} input combination is not valid. Please use either string or number syntax.'.format(datatype))

            if type(v) == str and v not in sub:
                raise Exception('Invalid {} data provided'.format(datatype))
            if type(v) == int and v not in values:
                raise Exception('Invalid {} data provided'.format(datatype))

        return string.replace(",", " ")

    def handle_last(self, string, datatype, days):
        """
        INPUT: string = Value of parameter, datatype = Type of the parameter.
        OUTPUT: String indicating the day of the week/month the command will run.
        """

        if datatype == 'week':
            if len(string) > 1:
                num, _ = string.split('L')
                print(num)
                return "Last {} of the Month".format(days[int(num) - 1])
            return days[-1]
        elif datatype == 'day':
            if string == "LW":
                return 'Last week day of the Month'
            elif "-" in string:
                _, day = string.split("-")
                return "{} days from the end of the month".format(day)
            return 'Last day of the Month'
        else:
            raise ValueError('L is not a valid {} input value'.format(datatype))

    def handle_weekday(self, string, datatype):
        """
        INPUT: string = Value of parameter, datatype = Type of the parameter.
        OUTPUT: String indicating the nearest weekday to which day of the month the
        command will run.
        """

        if datatype == 'day':
            date = string.split('W')[0]
            return 'Nearest weekday to day {} of the month'.format(date)
