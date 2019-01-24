"""
Singly Linked List implementation
* Insert
* Delete
* Size
* Search
* Check if circular

To run the TestCases
 $ python -m unittest linked_list -v

"""
import unittest

class Node:
    val = None
    next = None
    
    def __init__(self, data):
        self.val = data
        self.next = None


class SinglyLinkedList:
    head = None

    def insert(self, data):
        """
        Create a new Node and insert it at the beginning of the Linked List
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def size(self):
        """
        Calculates the size of the Linked List
        """
        head = self.head
        curr = head
        
        while curr.next != None:
            curr = curr.next
    
    def delete(self, data):
        pass
    
    def search(self, data):
        pass
    
    def convert_to_str(self):
        head = self.head
        curr = head
        
        list = []
        while curr.next != None:
            list.append(str(curr.val))
            curr = curr.next
        
        list.append(str(curr.val))
        
        return "".join(list)


class TestLinkedList(unittest.TestCase):
    singly_linked_list = None
    
    def setUp(self):
        sll = self.singly_linked_list = SinglyLinkedList()
        
        for i in range(1, 6):
            sll.insert(i)

    def test_insert_node(self):
        sll = self.singly_linked_list
        
        sll.insert(6)
        
        self.assertEqual('654321', sll.convert_to_str())
    
    def tearDown(self):
        self.singly_linked_list = None


if __name__ == '__main__':
    # make linkedlist 5 -> 4 -> 3 -> 2 -> 1

    sll = SinglyLinkedList()
    
    for i in range(1, 6):
        sll.insert(i)
        
    print(sll.convert_to_str())


