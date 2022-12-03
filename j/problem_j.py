class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class QueLinked:
    def __init__(self):
        self.current_size = 0
        self.head = None
        self.tail = None

    def get(self):
        if self.current_size == 0:
            print('error')
            return
        print(self.head.value)
        self.head = self.head.previous
        self.current_size -= 1
        if self.current_size > 0:
            self.head.next = None
        else:
            self.tail = None

    def put(self, x):
        next_node = self.tail
        self.tail = Node(x)
        self.tail.next = next_node
        if self.current_size == 0:
            self.head = self.tail
        else:
            next_node.previous = self.tail
        self.current_size += 1

    def size(self):
        print(self.current_size)


def main():
    commands_number = int(input())
    que = QueLinked()

    commands = {
        'put': que.put,
        'get': que.get,
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
    main()
