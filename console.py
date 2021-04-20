class Console:

    @staticmethod
    def get_str_input_with_args(message, args):
        return input(message.format(*args))

 
    def get_int_input(message):
        return int(input(message))