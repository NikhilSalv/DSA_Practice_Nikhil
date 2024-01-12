class Node:

    def __init__(self,data = None, next_node = None):
        self.data = data
        self.next_node = next_node


class LinkedList:

    def __init__(self):
        self.head = None


    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return
        iterator = self.head
        list_str = " "
        while iterator:
            list_str += str(iterator.data) + "-->"
            iterator = iterator.next_node
        print(list_str)
        print(iterator)


    def insert_at_beginning(self,data):
        node = Node(data, self.head)
        self.head = node


    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        iterator = self.head
        while iterator.next_node:
            iterator = iterator.next_node

        iterator.next_node = Node(data,None)

    def count_length(self):
        count = 0
        iterator = self.head
        while iterator:
            count += 1
            iterator = iterator.next_node
        return count
    
    def insert_at_index(self, data, idx):
        if idx < 0 or idx == self.count_length():
            raise Exception("Invalid Index")
        
        elif idx == 0:
            self.insert_at_beginning(data)
            return
        
        count = 0
        iterator = self.head
        while iterator:
            if count == idx - 1:
                node = Node(data,iterator.next_node)
                iterator.next_node = node
                break

            iterator = iterator.next_node
            count += 1


    def insert_value(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def remove_at_inx(self,idx):
        if idx < 0 or idx == self.count_length():
            raise Exception("Invalid Index")
        
        elif idx == 0:
            self.head = self.head.next_node
            return
        
        count = 0
        iterator = self.head

        while iterator:
            if count == idx - 1:
                iterator.next_node = iterator.next_node.next_node
                break

            iterator = iterator.next_node
            count += 1



if __name__ == "__main__":
    list_1 = LinkedList()
    # list_1.insert_at_beginning(45)
    list_1.insert_at_beginning(50)
    list_1.insert_at_beginning(34)
    list_1.print()
    # list_1.remove_at_inx(1)
    # list_1.print()
    # list_1.insert_at_index(377,2)
    # list_1.print()


    list_2 = LinkedList()
    list_2.insert_at_beginning(50)
    list_2.insert_at_end(12)
    list_2.print()

    list_3 = LinkedList()
    list_3.print() 