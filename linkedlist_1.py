class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def printlist(self):
        temp = self.head
        while temp:
            try:
                print(f'Data: {temp.data}, Next: {temp.next.data}')
                temp = temp.next
            except AttributeError:
                print(f'Data: {temp.data}, Next: None')
                temp = temp.next

    def append(self, node):
        if not self.head:
            self.head = node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = node


if __name__ == '__main__':
    list1 = LinkedList()

    first = Node('Data 1')
    second = Node('Data 2')
    third = Node('Data 3')
    fourth = Node('Data 4')
    fifth = Node('Data 5')

    list1.append(first)
    list1.append(second)
    list1.append(third)
    list1.append(fourth)
    list1.append(fifth)

    list1.printlist()


