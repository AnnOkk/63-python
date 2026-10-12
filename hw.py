# ## Write class MyStackInt with the following methods

# - push(num: int) adds number at top of the stack

# - pop() →int removes number from the top of stack with returning the number. Raises IndexError for empty stack

# - max() → int retuns maximal number in the stack. Raises IndexError for empty stack

# ## Note: all the above methods should have complexity O(1)

# ## Write tests for class MyStackInt\


class MyStackInt:
    def __init__(self):
        self.stack = []
        self.current_max = []

    def push(self, num):
        self.stack.append(num)
        if len(self.current_max) == 0:
            self.current_max.append(num)
        elif num >= self.current_max[-1]:
            self.current_max.append(num)
        else:
            self.current_max.append(self.current_max[-1])

    def pop(self):
        if len(self.stack) == 0:
            raise IndexError("Stack is empty")
        mx = self.stack.pop()
        self.current_max.pop()
        return mx


    def max(self):
        if len(self.stack) == 0 and len(self.current_max) == 0:
            raise IndexError("Stack is empty")
        return self.current_max[-1]

    def __len__(self):
        return len(self.stack)


