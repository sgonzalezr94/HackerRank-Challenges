class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build_stack(string_in: str):
            stack = list()
            for i in string_in:
                if i != "#":
                    stack.append(i)
                elif stack:
                    stack.pop()
            return stack

        print(build_stack(s), build_stack(t))
        return build_stack(s) == build_stack(t)


sol = Solution()
ans = sol.backspaceCompare("y#fo##f", "y#f#o##f")
print(ans)
ans2 = sol.backspaceCompare("a#c", "b")

print(ans2)
