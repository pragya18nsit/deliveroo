from sys import argv

from cronParser.runner import Runner


def main():
    # Fetch the arguments; the first elements in sys.argv is this python file itself - so ignore
    args = argv[1:]
    cron_expression = ""
    if len(args) == 1:
        cron_expression = args[0]
    runner_obj = Runner()
    print(cron_expression)
    print(runner_obj.describe_cron(cron_expression))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

