class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class SLL(object):
    def __init__(self):
        self.head = None


    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        n = self.head
        while n is not None:
            print(f"{n.data} -> ", end='')
            n = n.next
        print(end='\n')

    def reverse_list(self):
        prev = None
        current = self.head

        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

if __name__ == '__main__':
    l = SLL()
    l.push(1)
    l.push(2)
    l.push(3)
    l.push(4)
    l.print_list()
    l.reverse_list()
    l.print_list()

