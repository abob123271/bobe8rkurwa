class Dispatcher:
    def message(self, message, filter):
        if filter(message):
            return True
        return False
    
def CommandStart(value):
    return 'start' == value


def cmd_start(message, decorator):
    if not decorator(message, CommandStart):
        return
    print("Привет!")
    print("Как дела? Я бот-попрошайка")
    
dp = Dispatcher()
cmd_start('start', dp.message)

