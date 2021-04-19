class Console:

    @staticmethod
    def get_str_input_with_args(message, args):
        return input(message.format(*args))