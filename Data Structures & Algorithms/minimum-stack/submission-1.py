class MinStack:

    def __init__(self):
        self.length = 0
        self.stack = []
        self.min_list = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_list) == 0:
            self.min_list.append(self.length)
        else:
            if val<self.stack[self.min_list[-1]]:
                self.min_list.append(self.length)
        self.length += 1

    def pop(self) -> None:
        removed_item = self.stack.pop()
        self.length -= 1
        index = self.length
        if self.min_list[-1] == index:
            self.min_list.pop()

         

        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack[self.min_list[-1]]
        
