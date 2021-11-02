class A:
    def print_msg(self, msg):
        print(f'Class A: {msg}')


class B:
    def print_msg(self, msg):
        print(f'Class B: {msg}')


class Log:
    def __init__(self):
        self.msg = 'LOGGER'

    def log(self, message, notify):
        notify().print_msg(f'{self.msg} {message}')
        # Enter class in method!!!

    def log_a(self, msg):
        A().print_msg(f'{self.msg} {msg}')

    def log_b(self, msg):
        A().print_msg(f'{self.msg} {msg}')

logger = Log()
logger.log('After A', A)
logger.log('After B', B)
logger.log_a('Before A')
logger.log_b('Before B')

"""
Class A: LOGGER After A
Class B: LOGGER After B
Class A: LOGGER Before A
Class A: LOGGER Before B
"""
#