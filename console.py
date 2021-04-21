class Console:

    @staticmethod
    def get_str_input_with_args(message, args):
        return input(message.format(*args))

    @staticmethod
    def get_int_input(message):
        return int(input(message))

    @staticmethod
    def print_options():
        print("ACTIONS")
        print("General Actions:")
        print("1. Income")
        print("2. Foreign Aid")
        print("3. Coup")
        print("Card Actions:")
        print("4. Tax")
        print("5. Assasinate")
        print("6. Exchange")
        print("7. Steal")
        input("Select an action number(ex: 1): ")

