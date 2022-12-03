def check_brackets(brackets):
    bracket_pair = {
        '(': ')',
        '{': '}',
        '[': ']',
    }
    stack = []
    try:
        for bracket in brackets:
            if bracket in bracket_pair:
                stack.append(bracket_pair[bracket])
            elif bracket != stack.pop():
                return False
        if len(stack) == 0:
            return True
        return False
    except IndexError:
        return False


if __name__ == '__main__':
    print(check_brackets(input()))
