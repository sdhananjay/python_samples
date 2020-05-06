class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def linked_list():
    head = None


def reverse_list(node):
    if node is None:
        return node

    if node.next is None:
        return node

    print(node.data)
    node1 = reverse_list(node.next)
    print(node1.data)
    print("--------------------------")
    node.next.next = node
    node.next = None
    return node1

def push(head_ref, data):
    new_node = Node(data)
    new_node.next = head_ref
    head_ref = new_node
    return head_ref

def print_list():
    temp = head
    while temp is not None:
        print(f'{temp.data} -> ', end='')
        temp = temp.next
    print(end='\n')

if __name__ == '__main__':
    head = linked_list()
    head = push(head, 5)
    head = push(head, 4)
    head = push(head, 3)
    head = push(head, 2)
    head = push(head, 1)
    print_list()
    head = reverse_list(head)
    print_list()
