class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        work_stack = []
        for item in tokens:
            if  item in {"+", "-", "*", "/"}:
                a = work_stack.pop()
                b = work_stack.pop()
                match item:
                    case "+":
                        work_stack.append(a + b)
                    case "*":
                        work_stack.append(a * b)
                    case "-":
                        work_stack.append(b - a)
                    case "/":
                        work_stack.append(int(b / a))
            else:
                work_stack.append(int(item))
        return work_stack.pop()
                        