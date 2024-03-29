class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = []
        curly = []
        square = []
        for c in str:
            if c == "(":
                parentheses.append(c)
            if c == "{":
                curly.append(c)
            if c == "[":
                square.append(c)
                if c == ")":
                    try:
                        parentheses.pop()
                    except IndexError as e:
                        return False
            if c == "}":
                try:
                    curly.pop()
                except IndexError as e:
                    return False
        if c == "]":
            try:
                curly.pop()
            except IndexError as e:
                return False


        return True
