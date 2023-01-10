class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_data = Node(new_data)
        temp = self.head
        new_data.next = self.head

        if self.head:
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_data
        else:
            new_data.next = new_data
        self.head = new_data

        # print(self.head)
        # print(new_data.data)
        # print(new_data.next)

    def print_list(self):
        temp = self.head
        if self.head:
            while True:
                print(temp.data, end="-->")
                temp = temp.next
                if temp == self.head:
                    break


if __name__ == "__main__":
    llist = CircularLinkedList()
    llist.push(5)
    llist.push(3)

    llist.print_list()
