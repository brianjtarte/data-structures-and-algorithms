from python.code_challenges.stack_and_queue.stack import Stack


def multi_bracket_validation(text):
    brackets = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    brack_stack = Stack()
    for bracket in text:
        if bracket in brackets.values():
            brack_stack.push(bracket)
        elif bracket in brackets:
            if brack_stack.is_empty():
                return False
            elif brackets[bracket] != brack_stack.pop():
                return False
    return brack_stack.is_empty()
