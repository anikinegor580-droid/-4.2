class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data, next=None, prev=self.tail)
        if self.tail is not None:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node

    def prepend(self, data):
        new_node = Node(data, next=self.head, prev=None)
        if self.head is not None:
            self.head.prev = new_node
        else:
            self.tail = new_node
        self.head = new_node

    def delete(self, data):
        curr = self.head
        while curr is not None:
            if curr.data == data:
                if curr.prev is not None:
                    curr.prev.next = curr.next
                else:
                    self.head = curr.next

                if curr.next is not None:
                    curr.next.prev = curr.prev
                else:
                    self.tail = curr.prev
                return
            curr = curr.next

    def to_list(self):
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.data)
            curr = curr.next
        return result

    def to_list_reverse(self):
        result = []
        curr = self.tail
        while curr is not None:
            result.append(curr.data)
            curr = curr.prev
        return result
