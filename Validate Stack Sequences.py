from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        # fringe = []

        if len(pushed) != len(popped):
            return False

        def index_in_pushed(val: int):
            for idx, ele in enumerate(pushed):
                if ele == val:
                    return idx
            return None

        def append_nb(idx):
            fringe = []
            if idx >= 1: fringe.append(pushed[idx - 1])
            for i in range(idx + 1, len(pushed)):
                fringe.append(pushed[i])
            return fringe

        idx = index_in_pushed(popped[0])
        fringe = append_nb(idx)
        # print("idx is {}, fringe is {}".format(idx, fringe))
        pushed.pop(idx)

        for i in range(1, len(popped)):
            if popped[i] not in fringe:
                return False
            idx = index_in_pushed(popped[i])
            fringe = append_nb(idx)
            # print("idx is {}, fringe is {}".format(idx, fringe))
            pushed.pop(idx)
            # print("New pushed is {}".format(pushed))

        return True

    def alt_validate_stack_sequences(self, pushed, popped):
        stack = []
        i = 0
        for x in pushed:
            stack.append(x)
            while stack and stack[-1] == popped[i]:
                i += 1
                stack.pop()
        return len(stack) == 0


if __name__ == '__main__':
    sol = Solution()

    alt_pushed = [14, 3, 2, 1, 0, 4, 5]
    alt_popped = [1, 4, 0, 5, 2, 3, 14]
    
    assert (sol.validateStackSequences(pushed=[1, 2, 3, 4, 5], popped=[4, 5, 3, 2, 1])) == \
           sol.alt_validate_stack_sequences(pushed=[1, 2, 3, 4, 5], popped=[4, 5, 3, 2, 1])

    assert (sol.validateStackSequences(pushed=[1, 2, 3, 4, 5], popped=[4, 3, 5, 1, 2])) == \
           sol.alt_validate_stack_sequences(pushed=[1, 2, 3, 4, 5], popped=[4, 3, 5, 1, 2])

    assert (sol.validateStackSequences(alt_pushed, alt_popped)) == \
           sol.alt_validate_stack_sequences(alt_pushed, alt_popped)








