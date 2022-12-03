class StackMaxEffective:
    def __init__(self):
        self.items = []

    def push(self, value):
        max_value = max(self.items[-1], value) if len(self.items) else value
        self.items.append(max_value)

    def pop(self):
        try:
            self.items.pop(-1)
        except IndexError:
            return 'error'

    def get_max(self):
        try:
            return self.items[-1]
        except IndexError:
            return 'None'


def test():
    stack = StackMaxEffective()
    commands = {
        'get_max': stack.get_max,
        'push': stack.push,
        'pop': stack.pop,
    }

    for n in range(int(input())):
        command_string = input().split()
        args = map(int, command_string[1:])
        command = commands[command_string[0]]
        result = command(*args)
        if result is not None:
            print(result)


if __name__ == '__main__':
    test()
