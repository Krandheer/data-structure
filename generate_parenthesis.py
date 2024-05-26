def generateParenthesis(n):
    stack = []
    res = []

    def backtrack(openpar, closepar):
        if openpar == closepar == n:
            res.append("".join(stack))

        if openpar < n:
            stack.append("(")
            backtrack(openpar + 1, closepar)
            stack.pop()

        if openpar > closepar:
            stack.append(")")
            backtrack(openpar, closepar + 1)
            stack.pop()

    backtrack(0, 0)
    return res


ans = generateParenthesis(3)
print(ans)
