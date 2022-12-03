class MyQueSized:
    def __init__(self, max_size):
        self.max_size = max_size
        self.que = [None] * max_size
        self.head = 0
        self.tail = 0
        self.current_size = 0

    def push(self, x):
        if self.current_size == self.max_size:
            print('error')
            return
        self.que[self.tail] = x
        self.tail = (self.tail + 1) % self.max_size
        self.current_size += 1

    def pop(self):
        if self.current_size == 0:
            print('None')
            return
        x = self.que[self.head]
        self.head = (self.head + 1) % self.max_size
        self.current_size -= 1
        print(x)

    def peek(self):
        if self.current_size == 0:
            print('None')
            return
        print(self.que[self.head])

    def size(self):
        print(self.current_size)


def test():
    commands_number = int(input())
    que = MyQueSized(int(input()))

    commands = {
        'push': que.push,
        'pop': que.pop,
        'peek': que.peek,
        'size': que.size,
    }

    for n in range(commands_number):
        command_line = input().split()
        command = commands[command_line[0]]
        if len(command_line) == 1:
            command()
        else:
            command(command_line[1])


if __name__ == '__main__':
    test()
