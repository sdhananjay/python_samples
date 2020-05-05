class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class SLL(object):
    def __init__(self):
        self.head = None

    def traverse_list(self):
        if self.head == None:
            print("Empty List")
            return
        n = self.head
        while n is not None:
            print(f"{n.data} -> ", end='')
            n = n.next
        print(end='\n')
        return

    def get_count(self):
        count = 0
        n = self.head
        while n is not None:
            n = n.next
            count += 1
        return count

    def add_at_start(self, data):
        new_node = Node(data)
        self.head = new_node

    def add_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head == new_node
            return

        n = self.head
        while n is not None:
            n = n.next
        n.next = new_node

    def insert_after_this_data(self, x, data):
        if self.head is None:
            print("empty list")

        n = self.head
        print(n.next)
        while n is not None:
            if n.data == x:
                break
            n = n.next
        if n is None:
            print("Item {} is not present in the list".format(x))
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node

    def insert_before_this_data(self, x, data):
        if self.head is None:
            print("Empty List")
        
        if self.head.data == x:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

        n = self.head
        while n.next is not None:
            if n.next.data == x:
                break
            n = n.next

            if n.next is None:
                print("Item {} is not present in the list".format(x))
            
        new_node = Node(data)
        new_node.next = n.next
        n.next = new_node

    def insert_at_index(self, idx, data):
        if idx == 1:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

        i = 1
        n = self.head
        while i < idx -1 and n is not None:
            print(i, n)
            n = n.next 
            i += 1

        if n is None:
            print("index out of range")
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node


if __name__ == '__main__':

    n = SLL()
    n.add_at_start(1)
    n.insert_after_this_data(1, 2)
    n.insert_after_this_data(2, 4)
    n.insert_before_this_data(4, 3)
    n.insert_at_index(5, 5)
    n.traverse_list()
    print(n.get_count())
