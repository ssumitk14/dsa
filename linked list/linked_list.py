class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_data = Node(new_data)
        new_data.next = self.head
        self.head = new_data

    def insert_at(self, prev_value, new_data):
        if prev_value is None:
            print("Previous value does not exist")
            return
        new_data = Node(new_data)
        new_data.next = prev_value.next
        prev_value.next = new_data

    def append(self, new_data):
        new_data = Node(new_data)

        if self.head is None:
            print("self.head is None")
            self.head = new_data
            return

        current = self.head
        while current.next:
            print(current.next)
            current = current.next
            print(current.next)

        current.next = new_data

    def delete_node(self, key):
        temp = self.head

        # Case-1 (Where First node is to be deleted)
        if temp:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        # Case-2 (Iterating over the elements to find the key to be deleted)
        while temp:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        # Checking of the key is present in the linked list
        if not temp:
            print("Key not present in the linked list")
            return
        prev.next = temp.next
        temp = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end="-->")
            temp = temp.next


if __name__ == "__main__":
    llist = LinkedList()
    llist.push(5)
    llist.push(3)
    llist.append(12)
    llist.insert_at(llist.head.next, 25)
    print("Linked list before deleting: ")
    llist.print_list()

    llist.delete_node(5)
    print("\nLinked list after deleting: ")
    llist.print_list()
