class Stack:
    def __init__(self):
        self.container = list()

    def push(self, data):
        self.container.append(data)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

    def print_stack(self):
        print(self.container)


st = Stack()
st.push(5)
st.push(7)
st.push(3)
st.print_stack()
print("Popped Out Element from the stack")
print(st.pop())
print("Remaining Stack")
st.print_stack()
