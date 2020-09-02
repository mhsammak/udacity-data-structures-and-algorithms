class Node(object):
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


class LinkedList:
    def __init__(self, input_list=[]):
        self.__head = None
        self.__tail = None
        self.__size = 0

        for value in input_list:
            self.append(value)

    def append(self, value):
        if self.__head is None:
            self.__head = Node(value)
            self.__tail = head
        else:
            self.__tail.next = Node(value)
            self.__tail.next.prev = self.__tail
            self.__tail = self.__tail.next
        self.__size += 1
    
    def prepend(self, value):
        if self.__head is None:
            self.__head = Node(value)
            self.__tail = head
        else:
            self.__head.prev = Node(value)
            self.__head.prev.next = self.__head
            self.__head = self.__head.prev
        self.__size += 1
    
    def search(self, value):
        placeholder = self.__head
        while placeholder is not None:
            if placeholder.value == value:
                return placeholder
            placeholder = placeholder.next
        return None
    
    def remove(self, value):
        node = self.search(value)
        if node is None:
            return False
        
        if self.__size == 1:
            self.__head = self.__tail = None
        elif node is self.__head:
            self.__head = self.__head.next
            self.__head.prev = None
        elif node is self.__tail:
            self.__tail = self.__tail.prev
            self.__tail.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            node = None
        self.__size -= 1
    
    def pop_left(self):
        if self.__size == 0:
            raise IndexError('List is empty!')
        
        value = self.__head.value
        if self.__size == 1:
            self.__head = self.__tail = None
        else:
            self.__head = self.__head.next
            self.__head.prev = None
        return value
    
    def pop_right(self):
        if self.__size == 0:
            raise IndexError('List is empty!')
        
        value = self.__tail.value
        if self.__size == 1:
            self.__head = self.__tail = None
        else:
            self.__tail = self.__tail.prev
            self.__tail.next = None
        return value
    
    def insert(self, value, pos):
        if pos >= self.__size:
            self.append(value)
        elif pos == 0:
            self.prepend(value)
        else:
            placeholder = self.__head
            while pos > 0:
                placeholder = placeholder.next
                pos -= 1
            new_node = Node(value)
            new_node.next = placeholder
            new_node.prev = placeholder.prev
            new_node.prev.next = new_node
            placeholder.prev = new_node
            self.__size += 1
    
    def size(self):
        return self.__size
    
    def to_list(self):
        output = []
        placeholder = self.__head
        while placeholder is not None:
            output.append(placeholder.value)
            placeholder = placeholder.next
        return output
    
    def __str__(self):
        output = ''
        placeholder = self.__head
        while placeholder is not None:
            output += str(placeholder.value)
            output += ' '
        return output.strip()

