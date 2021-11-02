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

logger = Log()
logger.log('Test A', A)
logger.log('Test B', B)

"""
Class A: LOGGER Test A
Class B: LOGGER Test B
"""
#