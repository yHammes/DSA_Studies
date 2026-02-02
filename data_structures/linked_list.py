class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        node = Node(value)
        if not self.tail:
            self.head = node
            self.tail = node
            return

        self.tail.next = node
        self.tail = node

    def prepend(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
            return

        node.next = self.head
        self.head = node

    def find(self, value):
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next

        return False

    def remove(self, value):
        current = self.head

        # Empty
        if not current:
            return False

        # value is at the head
        if current.value == value:
            self.head = current.next
            if not self.head:
                self.tail = None
            return True

        # value is in the middle or tail
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                if not current.next:
                    self.tail = current

                return True
            current = current.next
        return False

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")


linked_list = LinkedList()
linked_list.append("a")
linked_list.append("b")
linked_list.prepend("z")
linked_list.append("c")

linked_list.remove("c")

linked_list.print_list()
