class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next

    def appendCSLL(self, value):
        newNode = Node(value)
        if self.head is None:
            newNode.next = newNode
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.tail.next
            self.tail.next = newNode
            self.tail = newNode
        self.count += 1

    def deleteCSLL(self, location):
        if self.head is None:
            print("Linked List doesn't exist")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head

            elif location == -1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    currentNode = self.head
                    while currentNode:
                        if currentNode.next == self.tail:
                            break
                        currentNode = currentNode.next
                    currentNode.next = self.head
                    self.tail = currentNode

            else:
                currentNode = self.head
                index = 0
                while index < location - 1:
                    currentNode = currentNode.next
                    index += 1
                nextNode = currentNode.next
                currentNode.next = nextNode.next

                # to update the tail node
                if currentNode.next == self.head:
                    self.tail = currentNode


CSLinkedList = CircularSinglyLinkedList()
CSLinkedList.appendCSLL('hello')
CSLinkedList.appendCSLL('how')
CSLinkedList.appendCSLL('are')
CSLinkedList.appendCSLL('you?')
print([node.value for node in CSLinkedList])
CSLinkedList.deleteCSLL(3)
print([node.value for node in CSLinkedList])