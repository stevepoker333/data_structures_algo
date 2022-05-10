class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value=None):
        new_node = Node(value) if value else None
        self.head = new_node
        self.tail = new_node
        self.length = 1 if value else 0

    def print_list(self):
        temp = self.head
        if not temp:
            print('Linked list is empty.')

        while temp:
            print(temp.value)
            temp = temp.next

    def get(self, index):
        if index >= self.length or index < 0:
            return None

        temp = self.head
        for _ in range(index):
            temp = temp.next

        return temp

    def remove(self, index):
        if index < 0 or index > self.length:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        prev = self.get(index-1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        temp = self.get(index)
        if temp:
            new_node = Node(temp.value)
            new_node.next = temp.next
            self.set_value(index, value)
            self.get(index).next = new_node
            self.length += 1
            return True
        return False

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

        return True

    def pop(self):
        temp = self.head
        if not temp:
            return None

        self.length -= 1
        while temp:
            if temp.next == self.tail:
                popped_node = temp.next
                temp.next = None

                return popped_node.value
            elif self.length == 1:
                popped_node = self.head
                self.head, self.tail = None, None

                return popped_node.value

            temp = temp.next

    def prepend(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length += 1

        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

        return True

    def pop_first(self):
        if self.length == 0:
            return None

        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1

        if self.length == 0:
            self.tail = None

        return temp


if __name__ == '__main__':
    linked_list1 = LinkedList()
    linked_list1.append(1)
    linked_list1.append(2)
    linked_list1.append(3)

    linked_list1.remove(3)
    linked_list1.print_list()

