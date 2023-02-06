from collections import deque


def valid_parenthesis(str1):
    stack = deque()
    for parenthesis in str1:
        if parenthesis == "(" or parenthesis == "{" or parenthesis == "[":
            stack.append(parenthesis)

        elif parenthesis == ")":
            if not stack or stack.pop() != "(":
                return False

        elif parenthesis == "}":
            if not stack or stack.pop() != "{":
                return False

        elif parenthesis == "]":
            if not stack or stack.pop() != "[":
                return False

    return True


print(valid_parenthesis('({[]})'))
