class DEQueue:
    def __init__(self, que_size):
        self.que = [None] * que_size
        self.current_size = 0
        self.max_size = que_size
        self.back = 0
        self.front = que_size - 1

    def pop(self, index):
        if self.current_size == 0:
            print('error')
            return False
        print(self.que[index])
        self.current_size -= 1
        return True

    def pop_back(self):
        if self.pop(self.back):
            self.back = (self.back + 1) % self.max_size

    def pop_front(self):
        if self.pop(self.front):
            self.front = self.front - 1
            if self.front == -1:
                self.front = self.max_size - 1

    def push(self, pointer, value):
        if self.current_size == self.max_size:
            print('error')
            return False
        self.que[pointer] = value
        self.current_size += 1
        return True

    def push_back(self, value):
        pointer = self.back - 1
        if pointer == -1:
            pointer = self.max_size - 1
        if self.push(pointer, value):
            self.back = pointer

    def push_front(self, value):
        pointer = (self.front + 1) % self.max_size
        if self.push(pointer, value):
            self.front = pointer


def main():
    f = open('input.txt')
    commands_number = int(f.readline())
    deq = DEQueue(int(f.readline()))
    commands = {
        'pop_back': deq.pop_back,
        'pop_front': deq.pop_front,
        'push_back': deq.push_back,
        'push_front': deq.push_front,
    }
    for n in range(commands_number):
        command = f.readline().split()
        if len(command) == 1:
            commands[command[0]]()
        else:
            commands[command[0]](int(command[1]))


if __name__ == '__main__':
    main()
