from python.code_challenges.stack_and_queue.stack import Stack


def multi_bracket_validation(str):
    # bracket_dictionary = {'[' : ']', '{' : '}', '(':')'}
    brack_stack = Stack()
    for brack in range(len(str)):
        if brack == '[' or brack == '{' or brack == '(':
            brack_stack.push(brack)
            print('Here we are line 10', brack_stack.value)

        if brack == ']' or brack == '}' or brack == ')':
            if brack_stack.is_empty():
                return True

            else:
                brack_stack.pop()


        else:
            return True








