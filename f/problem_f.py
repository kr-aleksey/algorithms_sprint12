class StackMax:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        self.items.pop(-1)

    def get_max(self):
        return max(self.items)


def test():
    stack = StackMax()
    commands = {
        'get_max': stack.get_max,
        'push': stack.push,
        'pop': stack.pop,
    }

    for n in range(int(input())):
        command_string = input().split()
        args = map(int, command_string[1:])
        command = commands[command_string[0]]
        try:
            result = command(*args)
            if result is not None:
                print(result)
        except IndexError:
            print('error')
        except ValueError:
            print('None')


if __name__ == '__main__':
    test()
