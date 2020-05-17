class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class SLL(object):
    def __init__(self):
        self.head = None

    def reverse_linkedlist(self):
        cur = None
        n = self.head

        while n.next.next is not None:
            temp2 = n.next.next
            temp1 = n.next
            cur = n
            cur.next = None
            temp1.next = cur
            n = nextnext
        self.head = prev

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

    def search_item(self, x):
        if self.head is None:
            return False

        n = self.head
        while n is not None:
            if n.data == x:
                return True
            n = n.next

        return False

    def delete_at_start(self):
        if self.head is None:
            print("Empty List")
            return
        n = self.head
        self.head = n.next
        del n

    def delete_at_end(self):
        if self.head is None:
            print("Empty List")
            return

        n = self.head
        while n.next.next is not None:
            n = n.next

        m = n.next
        print(f"deleting ssl object {m} with data {m.data}") 
        del m
        n.next = None
        return

    def delete_at_index(self, idx):
        if self.head is None:
            print("empty list")
            return

        n = self.head
        i = 1
        if idx == 1:
            self.head = n.next
            del n
        
        while i < idx -1 and n is not None:
            i += 1
            n = n.next

        if n is None:
            print("index out of range")
            return
        else:
            m = n.next
            n.next = n.next.next
            del m

    def delete_item(self, x):
        if self.head == None:
            print("Empty List")
            return

        n = self.head
        if n.data == x:
            self.head = n.next
            del n
            return

        while n.next is not None:
            if n.next.data == x:
                break
            n = n.next

        if n is None:
            print(f"Item {x} not found")
            return

        m = n.next
        n.next = n.next.next
        del m
        return

if __name__ == '__main__':

    n = SLL()
    n.add_at_start(1)
    n.insert_after_this_data(1, 2)
    n.insert_after_this_data(2, 4)
    n.insert_before_this_data(4, 3)
    n.insert_at_index(5, 5)
    n.insert_at_index(6, 6)
    n.insert_at_index(7, 7)
    n.insert_at_index(8, 8)
    n.traverse_list()
    print(n.search_item(7))
    print(n.search_item(3))
    print(n.get_count())
    '''
    n.traverse_list()
    n.delete_at_start()
    n.traverse_list()
    n.delete_at_end()
    n.traverse_list()
    n.delete_at_index(3)
    n.traverse_list()
    n.delete_item(6)
    n.traverse_list()
    '''
    n.reverse_linkedlist()
    n.traverse_list()

